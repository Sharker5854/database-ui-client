import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from config import *


class Database(QSqlDatabase):
    conn = None

    def __init__(self, username, password) -> None:
        super().__init__()
        self.__connect_database(username, password)

    @classmethod
    def __connect_database(cls, username, password) -> None:
        cls.conn = QSqlDatabase.addDatabase('QPSQL')
        cls.conn.setHostName(POSTGRES_HOST)
        cls.conn.setPort(POSTGRES_PORT)
        cls.conn.setDatabaseName(POSTGRES_DATABASE)
        cls.conn.setUserName(username)
        cls.conn.setPassword(password)
        if not cls.conn.open():
            QtWidgets.QMessageBox.critical(None, "Database connection error", "Неверный логин или пароль.", QtWidgets.QMessageBox.Cancel)

    @classmethod
    def execute_query_with_parameters(cls, sql_query, *args) -> QSqlQuery:
        query = QSqlQuery()
        query.prepare(sql_query)
        if args:
            for value in args:
                query.addBindValue(value)
        query.exec()
        return query
    
    @classmethod
    def get_all_table_accesses(cls) -> QSqlQuery:
        return cls.execute_query_with_parameters(
            """
            WITH privileges AS (
            SELECT
            'KnowledgeBranch' AS table_name,
            has_table_privilege(current_user, 'KnowledgeBranch', 'INSERT') AS can_insert,
            has_table_privilege(current_user, 'KnowledgeBranch', 'UPDATE') AS can_update,
            has_table_privilege(current_user, 'KnowledgeBranch', 'DELETE') AS can_delete
            UNION
            SELECT
            'Science' AS table_name,
            has_table_privilege(current_user, 'Science', 'INSERT') AS can_insert,
            has_table_privilege(current_user, 'Science', 'UPDATE') AS can_update,
            has_table_privilege(current_user, 'Science', 'DELETE') AS can_delete
            UNION
            SELECT
            'Author' AS table_name,
            has_table_privilege(current_user, 'Author', 'INSERT') AS can_insert,
            has_table_privilege(current_user, 'Author', 'UPDATE') AS can_update,
            has_table_privilege(current_user, 'Author', 'DELETE') AS can_delete
            UNION
            SELECT
            'Article' AS table_name,
            has_table_privilege(current_user, 'Article', 'INSERT') AS can_insert,
            has_table_privilege(current_user, 'Article', 'UPDATE') AS can_update,
            has_table_privilege(current_user, 'Article', 'DELETE') AS can_delete
            UNION
            SELECT
            'Monography' AS table_name,
            has_table_privilege(current_user, 'Monography', 'INSERT') AS can_insert,
            has_table_privilege(current_user, 'Monography', 'UPDATE') AS can_update,
            has_table_privilege(current_user, 'Monography', 'DELETE') AS can_delete
            )
            SELECT
            table_name,
            can_insert::int AS can_insert,
            can_update::int AS can_update,
            can_delete::int AS can_delete
            FROM
            privileges;
            """
        )

    @classmethod
    def __close_connection(cls) -> None:
        cls.conn.close()


class KnowledgeBranchTable(Database):

    @classmethod
    def get_all(cls):
        return cls.execute_query_with_parameters(
            "SELECT * FROM KnowledgeBranch ORDER BY id;"
        )
    
    @classmethod
    def create(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT add_knowledgebranch(?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def modify(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT update_knowledgebranch(?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def delete(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT delete_knowledgebranch(?)",
            *[arg if bool(arg) else None for arg in args]
        )
    

class ScienceTable(Database):

    @classmethod
    def get_all(cls):
        return cls.execute_query_with_parameters(
            """
            SELECT sci.id, sci.name, sci.description, (kbr.name) as knowledgeName, sci.created_at, sci.updated_at
            FROM Science sci 
            JOIN KnowledgeBranch kbr ON sci.knowledge_id = kbr.id 
            ORDER BY sci.id;
            """
        )
    
    @classmethod
    def create(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT add_science(?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def modify(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT update_science(?, ?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def delete(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT delete_science(?)",
            *[arg if bool(arg) else None for arg in args]
        )
    

class AuthorTable(Database):

    @classmethod
    def get_all(cls):
        return cls.execute_query_with_parameters(
            "SELECT * FROM Author ORDER BY id;"
        )
    
    @classmethod
    def create(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT add_author(?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def modify(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT update_author(?, ?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def delete(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT delete_author(?)",
            *[arg if bool(arg) else None for arg in args]
        )
    

class ArticleTable(Database):

    @classmethod
    def get_all(cls):
        return cls.execute_query_with_parameters(
            """
            SELECT art.id, title, content, published_at, (sci.name) as scienceName, (aut.name || ' ' || aut.surname) as authorNameSurname 
            FROM Article art 
            JOIN Science sci ON art.science_id = sci.id 
            JOIN Author aut ON art.author_id = aut.id
            ORDER BY art.id;
            """
        )
    
    @classmethod
    def create(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT add_article(?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def modify(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT update_article(?, ?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def delete(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT delete_article(?)",
            *[arg if bool(arg) else None for arg in args]
        )
    

class MonographyTable(Database):

    @classmethod
    def get_all(cls):
        return cls.execute_query_with_parameters(
            """
            SELECT mon.id, title, content, published_at, (sci.name) as scienceName, (aut.name || ' ' || aut.surname) as authorNameSurname 
            FROM Monography mon 
            LEFT JOIN Science sci ON mon.science_id = sci.id 
            JOIN Author aut ON mon.author_id = aut.id
            ORDER BY mon.id;
            """
        )
    
    @classmethod
    def create(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT add_monography(?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )
    
    @classmethod
    def modify(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT update_monography(?, ?, ?, ?, ?, ?)",
            *[arg if bool(arg) else None for arg in args]
        )

    @classmethod
    def delete(cls, *args):
        return cls.execute_query_with_parameters(
            "SELECT delete_monography(?)",
            *[arg if bool(arg) else None for arg in args]
        )