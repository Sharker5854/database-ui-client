import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from config import *


class Database(QSqlDatabase):
    conn = None

    def __init__(self) -> None:
        super().__init__()
        self.__connect_database()

    @classmethod
    def __connect_database(cls) -> None:
        cls.conn = QSqlDatabase.addDatabase('QPSQL')
        cls.conn.setHostName(POSTGRES_HOST)
        cls.conn.setPort(POSTGRES_PORT)
        cls.conn.setDatabaseName(POSTGRES_DATABASE)
        cls.conn.setUserName(POSTGRES_USERNAME)
        cls.conn.setPassword(POSTGRES_PASSWORD)
        if not cls.conn.open():
            QtWidgets.QMessageBox.critical(None, "Database connection error", "Не удалось установить соединение с базой данных.", QtWidgets.QMessageBox.Cancel)
            sys.exit(1)

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