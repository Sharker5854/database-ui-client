import sys
from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog , QTableView
from PySide6.QtSql import QSqlQueryModel, QSqlQuery

from db import Database, KnowledgeBranchTable, ScienceTable, AuthorTable, ArticleTable, MonographyTable

from utils import MainWindowUtils

from ui_components.ui_mainwindow import Ui_MainWindow
from ui_components.ui_auth import Ui_Dialog as Ui_Auth_Dialog
from ui_components.ui_create_knowledgebranch import Ui_Dialog as Ui_CreateKnowledgeBranch_Dialog
from ui_components.ui_modify_knowledgebranch import Ui_Dialog as Ui_ModifyKnowledgeBranch_Dialog
from ui_components.ui_create_science import Ui_Dialog as Ui_CreateScience_Dialog
from ui_components.ui_modify_science import Ui_Dialog as Ui_ModifyScience_Dialog
from ui_components.ui_create_author import Ui_Dialog as Ui_CreateAuthor_Dialog
from ui_components.ui_modify_author import Ui_Dialog as Ui_ModifyAuthor_Dialog
from ui_components.ui_create_article import Ui_Dialog as Ui_CreateArticle_Dialog
from ui_components.ui_modify_article import Ui_Dialog as Ui_ModifyArticle_Dialog
from ui_components.ui_create_monography import Ui_Dialog as Ui_CreateMonography_Dialog
from ui_components.ui_modify_monography import Ui_Dialog as Ui_ModifyMonography_Dialog



class AuthDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Auth_Dialog()
        self.ui.setupUi(self)

        self.ui.addButton_6.clicked.connect(self.auth_to_database)

    
    def auth_to_database(self):
        self.db = Database(
            self.ui.lineEdit.text().strip(),
            self.ui.lineEdit_3.text().strip()
        )
        if self.db.conn.isOpen():
            self.accept()
        else:
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_3.setText("")



class LibraryCataloger(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database
        self.ui.tabWidget.currentChanged.connect(self.on_tab_changed)

        MainWindowUtils.make_tabs_current_consistently(self.ui)
        MainWindowUtils.make_all_delete_buttons_disabled(self.ui)
        MainWindowUtils.make_all_edit_buttons_disabled(self.ui)

        self.ui.deleteButton.clicked.connect(self.run_delete_controller)
        self.ui.deleteButton_3.clicked.connect(self.run_delete_controller)
        self.ui.deleteButton_4.clicked.connect(self.run_delete_controller)
        self.ui.deleteButton_5.clicked.connect(self.run_delete_controller)
        self.ui.deleteButton_6.clicked.connect(self.run_delete_controller)
        
        self.ui.editButton.clicked.connect(self.open_modify_dialog)
        self.ui.editButton_3.clicked.connect(self.open_modify_dialog)
        self.ui.editButton_4.clicked.connect(self.open_modify_dialog)
        self.ui.editButton_5.clicked.connect(self.open_modify_dialog)
        self.ui.editButton_6.clicked.connect(self.open_modify_dialog)

        self.ui.addButton.clicked.connect(self.open_create_dialog)
        self.ui.addButton_3.clicked.connect(self.open_create_dialog)
        self.ui.addButton_4.clicked.connect(self.open_create_dialog)
        self.ui.addButton_5.clicked.connect(self.open_create_dialog)
        self.ui.addButton_6.clicked.connect(self.open_create_dialog)


    def on_tab_changed(self, tab_index: int) -> None:
        match tab_index:
            case 0:
                self.reload_table_data(self.ui.tableView, KnowledgeBranchTable)
            case 1:
                self.reload_table_data(self.ui.tableView_2, ScienceTable)
            case 2:
                self.reload_table_data(self.ui.tableView_3, AuthorTable)
            case 3:
                self.reload_table_data(self.ui.tableView_4, ArticleTable)
            case 4:
                self.reload_table_data(self.ui.tableView_5, MonographyTable)

    def reload_table_data(
            self, tableViewObj: QTableView, 
            databaseTableObj: KnowledgeBranchTable | ScienceTable | AuthorTable | ArticleTable | MonographyTable
        ) -> None:
        MainWindowUtils.make_all_delete_buttons_disabled(self.ui)
        MainWindowUtils.make_all_edit_buttons_disabled(self.ui)
        model = QSqlQueryModel(self)
        model.setQuery(databaseTableObj.get_all())
        tableViewObj.setModel(model)
        tableViewObj.setColumnHidden(0, True)
        tableViewObj.setSelectionMode(QTableView.SingleSelection)
        tableViewObj.setSelectionBehavior(QTableView.SelectRows)
        tableViewObj.selectionModel().selectionChanged.connect(self.change_delete_update_button_states)
        tableViewObj.show()

    def change_delete_update_button_states(self, selected, deselected):
        match self.ui.tabWidget.currentIndex():
            case 0:
                self.ui.deleteButton.setEnabled(True)
                self.ui.editButton.setEnabled(True)
            case 1:
                self.ui.deleteButton_3.setEnabled(True)
                self.ui.editButton_3.setEnabled(True)
            case 2:
                self.ui.deleteButton_4.setEnabled(True)
                self.ui.editButton_4.setEnabled(True)
            case 3:
                self.ui.deleteButton_5.setEnabled(True)
                self.ui.editButton_5.setEnabled(True)
            case 4:
                self.ui.deleteButton_6.setEnabled(True)
                self.ui.editButton_6.setEnabled(True)

    def run_delete_controller(self):
        match self.ui.tabWidget.currentIndex():
            case 0:
                DeleteController(self.ui.tableView, self.ui.tabWidget.currentIndex())
                self.reload_table_data(self.ui.tableView, KnowledgeBranchTable)
            case 1:
                DeleteController(self.ui.tableView_2, self.ui.tabWidget.currentIndex())
                self.reload_table_data(self.ui.tableView_2, ScienceTable)
            case 2:
                DeleteController(self.ui.tableView_3, self.ui.tabWidget.currentIndex())
                self.reload_table_data(self.ui.tableView_3, AuthorTable)
            case 3:
                DeleteController(self.ui.tableView_4, self.ui.tabWidget.currentIndex())
                self.reload_table_data(self.ui.tableView_4, ArticleTable)
            case 4:
                DeleteController(self.ui.tableView_5, self.ui.tabWidget.currentIndex())
                self.reload_table_data(self.ui.tableView_5, MonographyTable)

    def open_modify_dialog(self):
        match self.ui.tabWidget.currentIndex():
            case 0:
                dialog = ModifyDialog(Ui_ModifyKnowledgeBranch_Dialog, self.ui.tableView)
                dialog.exec()
                self.reload_table_data(self.ui.tableView, KnowledgeBranchTable)
            case 1:
                dialog = ModifyDialog(Ui_ModifyScience_Dialog, self.ui.tableView_2)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_2, ScienceTable)
            case 2:
                dialog = ModifyDialog(Ui_ModifyAuthor_Dialog, self.ui.tableView_3)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_3, AuthorTable)
            case 3:
                dialog = ModifyDialog(Ui_ModifyArticle_Dialog, self.ui.tableView_4)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_4, ArticleTable)
            case 4:
                dialog = ModifyDialog(Ui_ModifyMonography_Dialog, self.ui.tableView_5)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_5, MonographyTable)

    def open_create_dialog(self):
        match self.ui.tabWidget.currentIndex():
            case 0:
                dialog = CreateDialog(Ui_CreateKnowledgeBranch_Dialog)
                dialog.exec()
                self.reload_table_data(self.ui.tableView, KnowledgeBranchTable)
            case 1:
                dialog = CreateDialog(Ui_CreateScience_Dialog)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_2, ScienceTable)
            case 2:
                dialog = CreateDialog(Ui_CreateAuthor_Dialog)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_3, AuthorTable)
            case 3:
                dialog = CreateDialog(Ui_CreateArticle_Dialog)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_4, ArticleTable)
            case 4:
                dialog = CreateDialog(Ui_CreateMonography_Dialog)
                dialog.exec()
                self.reload_table_data(self.ui.tableView_5, MonographyTable)
                
        

class ModifyDialog(QDialog):
    def __init__(
            self, 
            ui_cls: Ui_ModifyKnowledgeBranch_Dialog | Ui_ModifyScience_Dialog | Ui_ModifyAuthor_Dialog | Ui_ModifyArticle_Dialog | Ui_ModifyMonography_Dialog, 
            current_tableview: QTableView
        ) -> None:
        super().__init__()
        self.ui = ui_cls()
        self.ui.setupUi(self)
        self.current_tableview = current_tableview

        self.fill_input_fields()

        self.ui.addButton_6.clicked.connect(self.modify_record)


    def fill_input_fields(self):
        current_model = self.current_tableview.model()
        selected_record = self.current_tableview.selectionModel().selectedRows()[0].row()
        match self.ui:
            case Ui_ModifyKnowledgeBranch_Dialog():
                self.record_id_value = current_model.data(current_model.index(selected_record, 0))
                name_value = current_model.data(current_model.index(selected_record, 1))
                description_value = current_model.data(current_model.index(selected_record, 2))
                created_at_value = current_model.data(current_model.index(selected_record, 3))
                updated_at_value = current_model.data(current_model.index(selected_record, 4))
                self.ui.lineEdit.setText(name_value)
                self.ui.lineEdit_3.setText(description_value)
                self.ui.dateEdit.setDate(created_at_value)
                self.ui.dateEdit_2.setDate(updated_at_value)
            case Ui_ModifyScience_Dialog():
                self.record_id_value = current_model.data(current_model.index(selected_record, 0))
                name_value = current_model.data(current_model.index(selected_record, 1))
                description_value = current_model.data(current_model.index(selected_record, 2))
                knowledge_name_value = current_model.data(current_model.index(selected_record, 3))
                created_at_value = current_model.data(current_model.index(selected_record, 4))
                updated_at_value = current_model.data(current_model.index(selected_record, 5))
                self.ui.lineEdit.setText(name_value)
                self.ui.lineEdit_3.setText(description_value)
                knowledge_branch_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name, id FROM KnowledgeBranch;")
                kbr_names = []
                while knowledge_branch_names_query.next():
                    kbr_names.append( (knowledge_branch_names_query.value(0), knowledge_branch_names_query.value(1)) )
                for record_seq_num in range(len(kbr_names)):
                    self.ui.comboBox.addItem(kbr_names[record_seq_num][0])
                setattr(self.ui.comboBox, "record_ids", [record[1] for record in kbr_names])
                self.ui.comboBox.setCurrentText(knowledge_name_value)
                self.ui.dateEdit.setDate(created_at_value)
                self.ui.dateEdit_2.setDate(updated_at_value)
            case Ui_ModifyAuthor_Dialog():
                self.record_id_value = current_model.data(current_model.index(selected_record, 0))
                name_value = current_model.data(current_model.index(selected_record, 1))
                surname_value = current_model.data(current_model.index(selected_record, 2))
                patronymic_value = current_model.data(current_model.index(selected_record, 3))
                birth_date_value = current_model.data(current_model.index(selected_record, 4))
                email_value = current_model.data(current_model.index(selected_record, 5))
                self.ui.lineEdit.setText(name_value)
                self.ui.lineEdit_3.setText(surname_value)
                self.ui.lineEdit_4.setText(patronymic_value)
                self.ui.dateEdit.setDate(birth_date_value)
                self.ui.lineEdit_5.setText(email_value)
            case Ui_ModifyArticle_Dialog():
                self.record_id_value = current_model.data(current_model.index(selected_record, 0))
                title_value = current_model.data(current_model.index(selected_record, 1))
                content_value = current_model.data(current_model.index(selected_record, 2))
                published_at_value = current_model.data(current_model.index(selected_record, 3))
                science_name_value = current_model.data(current_model.index(selected_record, 4))
                author_name_surname_value = current_model.data(current_model.index(selected_record, 5))
                self.ui.lineEdit.setText(title_value)
                self.ui.textEdit.setText(content_value)
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name, id FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append( (science_names_query.value(0), science_names_query.value(1)) )
                for record_seq_num in range(len(science_names)):
                    self.ui.comboBox.addItem(science_names[record_seq_num][0])
                setattr(self.ui.comboBox, "record_ids", [record[1] for record in science_names])
                self.ui.comboBox.setCurrentText(science_name_value)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname, id FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append( (author_names_surnames_query.value(0), author_names_surnames_query.value(1)) )
                for record_seq_num in range(len(author_names_surnames)):
                    self.ui.comboBox_2.addItem(author_names_surnames[record_seq_num][0])
                setattr(self.ui.comboBox_2, "record_ids", [record[1] for record in author_names_surnames])
                self.ui.comboBox_2.setCurrentText(author_name_surname_value)
            case Ui_ModifyMonography_Dialog():
                self.record_id_value = current_model.data(current_model.index(selected_record, 0))
                title_value = current_model.data(current_model.index(selected_record, 1))
                content_value = current_model.data(current_model.index(selected_record, 2))
                published_at_value = current_model.data(current_model.index(selected_record, 3))
                science_name_value = current_model.data(current_model.index(selected_record, 4))
                author_name_surname_value = current_model.data(current_model.index(selected_record, 5))
                self.ui.lineEdit.setText(title_value)
                self.ui.textEdit.setText(content_value)
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name, id FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append( (science_names_query.value(0), science_names_query.value(1)) )
                for record_seq_num in range(len(science_names)):
                    self.ui.comboBox.addItem(science_names[record_seq_num][0])
                setattr(self.ui.comboBox, "record_ids", [record[1] for record in science_names])
                self.ui.comboBox.setCurrentText(science_name_value)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname, id FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append( (author_names_surnames_query.value(0), author_names_surnames_query.value(1)) )
                for record_seq_num in range(len(author_names_surnames)):
                    self.ui.comboBox_2.addItem(author_names_surnames[record_seq_num][0])
                setattr(self.ui.comboBox_2, "record_ids", [record[1] for record in author_names_surnames])
                self.ui.comboBox_2.setCurrentText(author_name_surname_value)

    def modify_record(self) -> None:
        match self.ui:
            case Ui_ModifyKnowledgeBranch_Dialog():
                result = KnowledgeBranchTable.modify(
                    self.record_id_value,
                    self.ui.lineEdit.text().strip(),
                    self.ui.lineEdit_3.text().strip(),
                    self.ui.dateEdit.date().toString("yyyy-MM-dd").strip(),
                    self.ui.dateEdit_2.date().toString("yyyy-MM-dd").strip()
                )
                self.complete_modifying_process(result)
            case Ui_ModifyScience_Dialog():
                result = ScienceTable.modify(
                    self.record_id_value,
                    self.ui.lineEdit.text().strip(),
                    self.ui.lineEdit_3.text().strip(),
                    self.ui.comboBox.record_ids[self.ui.comboBox.currentIndex()],
                    self.ui.dateEdit.date().toString("yyyy-MM-dd").strip(),
                    self.ui.dateEdit_2.date().toString("yyyy-MM-dd").strip()
                )
                self.complete_modifying_process(result)
            case Ui_ModifyAuthor_Dialog():
                result = AuthorTable.modify(
                    self.record_id_value,
                    self.ui.lineEdit.text().strip(),
                    self.ui.lineEdit_3.text().strip(),
                    self.ui.lineEdit_4.text().strip(),
                    self.ui.dateEdit.date().toString("yyyy-MM-dd").strip(),
                    self.ui.lineEdit_5.text().strip()
                )
                self.complete_modifying_process(result)
            case Ui_ModifyArticle_Dialog():
                result = ArticleTable.modify(
                    self.record_id_value,
                    self.ui.lineEdit.text().strip(),
                    self.ui.textEdit.toPlainText().strip(),
                    datetime.now().strftime("%Y-%m-%d"),
                    self.ui.comboBox.record_ids[self.ui.comboBox.currentIndex()],
                    self.ui.comboBox_2.record_ids[self.ui.comboBox_2.currentIndex()]
                )
                self.complete_modifying_process(result)
            case Ui_ModifyMonography_Dialog():
                result = MonographyTable.modify(
                    self.record_id_value,
                    self.ui.lineEdit.text().strip(),
                    self.ui.textEdit.toPlainText().strip(),
                    datetime.now().strftime("%Y-%m-%d"),
                    self.ui.comboBox.record_ids[self.ui.comboBox.currentIndex()],
                    self.ui.comboBox_2.record_ids[self.ui.comboBox_2.currentIndex()]
                )
                self.complete_modifying_process(result)

    def complete_modifying_process(self, query_result: QSqlQuery):
        if query_result.isActive():
            self.accept()
            QtWidgets.QMessageBox.information(None, "Record successfully modified", "Запись успешно отредактирована!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(None, "Error while modifying a record", query_result.lastError().text(), QtWidgets.QMessageBox.Cancel)



class CreateDialog(QDialog):
    def __init__(
            self, 
            ui_cls: Ui_CreateKnowledgeBranch_Dialog | Ui_CreateScience_Dialog | Ui_CreateAuthor_Dialog | Ui_CreateArticle_Dialog | Ui_CreateMonography_Dialog,
        ) -> None:
        super().__init__()
        self.ui: Ui_CreateKnowledgeBranch_Dialog | Ui_CreateScience_Dialog | Ui_CreateAuthor_Dialog | Ui_CreateArticle_Dialog | Ui_CreateMonography_Dialog = ui_cls()
        self.ui.setupUi(self)

        self.fill_input_fields()

        self.ui.addButton_6.clicked.connect(self.create_record)


    def fill_input_fields(self):
        match self.ui:
            case Ui_CreateScience_Dialog():
                knowledge_branch_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name, id FROM KnowledgeBranch;")
                kbr_names = []
                while knowledge_branch_names_query.next():
                    kbr_names.append( (knowledge_branch_names_query.value(0), knowledge_branch_names_query.value(1)) )
                for record_seq_num in range(len(kbr_names)):
                    self.ui.comboBox.addItem(kbr_names[record_seq_num][0])
                setattr(self.ui.comboBox, "record_ids", [record[1] for record in kbr_names])
                self.ui.comboBox.setCurrentIndex(0)
            case Ui_CreateArticle_Dialog():
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name, id FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append( (science_names_query.value(0), science_names_query.value(1)) )
                for record_seq_num in range(len(science_names)):
                    self.ui.comboBox.addItem(science_names[record_seq_num][0])
                setattr(self.ui.comboBox, "record_ids", [record[1] for record in science_names])
                self.ui.comboBox.setCurrentIndex(0)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname, id FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append( (author_names_surnames_query.value(0), author_names_surnames_query.value(1)) )
                for record_seq_num in range(len(author_names_surnames)):
                    self.ui.comboBox_2.addItem(author_names_surnames[record_seq_num][0])
                setattr(self.ui.comboBox_2, "record_ids", [record[1] for record in author_names_surnames])
                self.ui.comboBox_2.setCurrentIndex(0)
            case Ui_CreateMonography_Dialog():
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name, id FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append( (science_names_query.value(0), science_names_query.value(1)))
                for record_seq_num in range(len(science_names)):
                    self.ui.comboBox.addItem(science_names[record_seq_num][0])
                setattr(self.ui.comboBox, "record_ids", [record[1] for record in science_names])
                self.ui.comboBox.setCurrentIndex(0)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname, id FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append( (author_names_surnames_query.value(0), author_names_surnames_query.value(1)) )
                for record_seq_num in range(len(author_names_surnames)):
                    self.ui.comboBox_2.addItem(author_names_surnames[record_seq_num][0])
                setattr(self.ui.comboBox_2, "record_ids", [record[1] for record in author_names_surnames])
                self.ui.comboBox_2.setCurrentIndex(0)

    
    def create_record(self) -> None:
        match self.ui:
            case Ui_CreateKnowledgeBranch_Dialog():
                result = KnowledgeBranchTable.create(
                    self.ui.lineEdit.text().strip(),
                    self.ui.lineEdit_3.text().strip(),
                    self.ui.dateEdit.date().toString("yyyy-MM-dd").strip(),
                    self.ui.dateEdit_2.date().toString("yyyy-MM-dd").strip()
                )
                self.complete_creation_process(result)
            case Ui_CreateScience_Dialog():
                result = ScienceTable.create(
                    self.ui.lineEdit.text().strip(),
                    self.ui.lineEdit_3.text().strip(),
                    self.ui.comboBox.record_ids[self.ui.comboBox.currentIndex()],
                    self.ui.dateEdit.date().toString("yyyy-MM-dd").strip(),
                    self.ui.dateEdit_2.date().toString("yyyy-MM-dd").strip()
                )
                self.complete_creation_process(result)
            case Ui_CreateAuthor_Dialog():
                result = AuthorTable.create(
                    self.ui.lineEdit.text().strip(),
                    self.ui.lineEdit_3.text().strip(),
                    self.ui.dateEdit.date().toString("yyyy-MM-dd").strip(),
                    self.ui.lineEdit_4.text() if bool(self.ui.lineEdit_4.text().strip()) else None,
                    self.ui.lineEdit_5.text() if bool(self.ui.lineEdit_5.text().strip()) else None,
                )
                self.complete_creation_process(result)
            case Ui_CreateArticle_Dialog():
                result = ArticleTable.create(
                    self.ui.lineEdit.text().strip(),
                    self.ui.textEdit.toPlainText().strip(),
                    datetime.now().strftime("%Y-%m-%d").strip(),
                    self.ui.comboBox.record_ids[self.ui.comboBox.currentIndex()],
                    self.ui.comboBox_2.record_ids[self.ui.comboBox_2.currentIndex()]
                )
                self.complete_creation_process(result)
            case Ui_CreateMonography_Dialog():
                result = MonographyTable.create(
                    self.ui.lineEdit.text().strip(),
                    self.ui.textEdit.toPlainText().strip(),
                    datetime.now().strftime("%Y-%m-%d").strip(),
                    self.ui.comboBox.record_ids[self.ui.comboBox.currentIndex()],
                    self.ui.comboBox_2.record_ids[self.ui.comboBox_2.currentIndex()]
                )
                self.complete_creation_process(result)

    def complete_creation_process(self, query_result: QSqlQuery):
        if query_result.isActive():
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(None, "Error when creating a record", query_result.lastError().text(), QtWidgets.QMessageBox.Cancel)



class DeleteController():
    def __init__(self, current_tableview: QTableView, currentTabIndex: int) -> None:
        self.current_tableview = current_tableview
        self.currentTabIndex = currentTabIndex
        self.delete_record()
            
    def delete_record(self) -> None:
        current_model = self.current_tableview.model()
        selected_record = self.current_tableview.selectionModel().selectedRows()[0].row()
        record_id_value = current_model.data(current_model.index(selected_record, 0))
        match self.currentTabIndex:
            case 0:
                result = KnowledgeBranchTable.delete(
                    record_id_value
                )
                self.complete_deletion_process(result)
            case 1:
                result = ScienceTable.delete(
                    record_id_value
                )
                self.complete_deletion_process(result)
            case 2:
                result = AuthorTable.delete(
                    record_id_value
                )
                self.complete_deletion_process(result)
            case 3:
                result = ArticleTable.delete(
                    record_id_value
                )
                self.complete_deletion_process(result)
            case 4:
                result = MonographyTable.delete(
                    record_id_value
                )
                self.complete_deletion_process(result)

    def complete_deletion_process(self, query_result: QSqlQuery):
        if query_result.isActive():
            QtWidgets.QMessageBox.information(None, "Record successfully deleted", "Запись успешно удалена!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(None, "Error while deleting a record", query_result.lastError().text(), QtWidgets.QMessageBox.Cancel)


        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = AuthDialog()
    if start_window.exec() == 1:
        mainwindow = LibraryCataloger()
        mainwindow.show()
    sys.exit(app.exec())