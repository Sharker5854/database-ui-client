import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog , QTableView
from PySide6.QtSql import QSqlQueryModel

from db import Database, KnowledgeBranchTable, ScienceTable, AuthorTable, ArticleTable, MonographyTable

from utils import MainWindowUtils

from ui_components.ui_mainwindow import Ui_MainWindow
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


# TO DO:
# - Баг с датой 14.09.1752 при автозаполнении полей created_at и birth_date в modify dialog'ах
# - Не забыть сохранять ID текущей редактируемой записи в self.current_record_id атрибуте класса ModifyDialog, чтобы потом в методе который непосредственно работает с БД знать какую запись редачить
# - Подумать как однозначно идентифицировать авторов статьи/монографии исходя из выбранных имени_фамилии в comboBox при создании/редактировании


class LibraryCataloger(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()

        self.ui.tabWidget.currentChanged.connect(self.on_tab_changed)

        MainWindowUtils.make_tabs_current_consistently(self.ui)
        MainWindowUtils.make_all_delete_buttons_disabled(self.ui)
        MainWindowUtils.make_all_edit_buttons_disabled(self.ui)
        
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

    def open_modify_dialog(self):
        match self.ui.tabWidget.currentIndex():
            case 0:
                dialog = ModifyDialog(Ui_ModifyKnowledgeBranch_Dialog, self.ui.tableView)
                dialog.exec()
            case 1:
                dialog = ModifyDialog(Ui_ModifyScience_Dialog, self.ui.tableView_2)
                dialog.exec()
            case 2:
                dialog = ModifyDialog(Ui_ModifyAuthor_Dialog, self.ui.tableView_3)
                dialog.exec()
            case 3:
                dialog = ModifyDialog(Ui_ModifyArticle_Dialog, self.ui.tableView_4)
                dialog.exec()
            case 4:
                dialog = ModifyDialog(Ui_ModifyMonography_Dialog, self.ui.tableView_5)
                dialog.exec()

    def open_create_dialog(self):
        match self.ui.tabWidget.currentIndex():
            case 0:
                dialog = CreateDialog(Ui_CreateKnowledgeBranch_Dialog)
                dialog.exec()
            case 1:
                dialog = CreateDialog(Ui_CreateScience_Dialog)
                dialog.exec()
            case 2:
                dialog = CreateDialog(Ui_CreateAuthor_Dialog)
                dialog.exec()
            case 3:
                dialog = CreateDialog(Ui_CreateArticle_Dialog)
                dialog.exec()
            case 4:
                dialog = CreateDialog(Ui_CreateMonography_Dialog)
                dialog.exec()
                
        

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


    def fill_input_fields(self):
        current_model = self.current_tableview.model()
        selected_record = self.current_tableview.selectionModel().selectedRows()[0].row()
        match self.ui:
            case Ui_ModifyKnowledgeBranch_Dialog():
                id_value = current_model.data(current_model.index(selected_record, 0))
                name_value = current_model.data(current_model.index(selected_record, 1))
                description_value = current_model.data(current_model.index(selected_record, 2))
                created_at_value = current_model.data(current_model.index(selected_record, 3))
                updated_at_value = current_model.data(current_model.index(selected_record, 4))
                self.ui.lineEdit.setText(name_value)
                self.ui.lineEdit_3.setText(description_value)
                self.ui.dateEdit.setDate(created_at_value)
                self.ui.dateEdit_2.setDate(updated_at_value)
            case Ui_ModifyScience_Dialog():
                id_value = current_model.data(current_model.index(selected_record, 0))
                name_value = current_model.data(current_model.index(selected_record, 1))
                description_value = current_model.data(current_model.index(selected_record, 2))
                knowledge_name_value = current_model.data(current_model.index(selected_record, 3))
                created_at_value = current_model.data(current_model.index(selected_record, 4))
                updated_at_value = current_model.data(current_model.index(selected_record, 5))
                self.ui.lineEdit.setText(name_value)
                self.ui.lineEdit_3.setText(description_value)
                knowledge_branch_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name FROM KnowledgeBranch;")
                kbr_names = []
                while knowledge_branch_names_query.next():
                    kbr_names.append(knowledge_branch_names_query.value(0))
                self.ui.comboBox.addItems(kbr_names)
                self.ui.comboBox.setCurrentText(knowledge_name_value)
                self.ui.dateEdit.setDate(created_at_value)
                self.ui.dateEdit_2.setDate(updated_at_value)
            case Ui_ModifyAuthor_Dialog():
                id_value = current_model.data(current_model.index(selected_record, 0))
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
                id_value = current_model.data(current_model.index(selected_record, 0))
                title_value = current_model.data(current_model.index(selected_record, 1))
                content_value = current_model.data(current_model.index(selected_record, 2))
                published_at_value = current_model.data(current_model.index(selected_record, 3))
                science_name_value = current_model.data(current_model.index(selected_record, 4))
                author_name_surname_value = current_model.data(current_model.index(selected_record, 5))
                self.ui.lineEdit.setText(title_value)
                self.ui.textEdit.setText(content_value)
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append(science_names_query.value(0))
                self.ui.comboBox.addItems(science_names)
                self.ui.comboBox.setCurrentText(science_name_value)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append(author_names_surnames_query.value(0))
                self.ui.comboBox_2.addItems(author_names_surnames)
                self.ui.comboBox_2.setCurrentText(author_name_surname_value)
            case Ui_ModifyMonography_Dialog():
                id_value = current_model.data(current_model.index(selected_record, 0))
                title_value = current_model.data(current_model.index(selected_record, 1))
                content_value = current_model.data(current_model.index(selected_record, 2))
                published_at_value = current_model.data(current_model.index(selected_record, 3))
                science_name_value = current_model.data(current_model.index(selected_record, 4))
                author_name_surname_value = current_model.data(current_model.index(selected_record, 5))
                self.ui.lineEdit.setText(title_value)
                self.ui.textEdit.setText(content_value)
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append(science_names_query.value(0))
                self.ui.comboBox.addItems(science_names)
                self.ui.comboBox.setCurrentText(science_name_value)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append(author_names_surnames_query.value(0))
                self.ui.comboBox_2.addItems(author_names_surnames)
                self.ui.comboBox_2.setCurrentText(author_name_surname_value)



class CreateDialog(QDialog):
    def __init__(
            self, 
            ui_cls: Ui_CreateKnowledgeBranch_Dialog | Ui_CreateScience_Dialog | Ui_CreateAuthor_Dialog | Ui_CreateArticle_Dialog | Ui_CreateMonography_Dialog,
        ) -> None:
        super().__init__()
        self.ui = ui_cls()
        self.ui.setupUi(self)

        self.fill_input_fields()


    def fill_input_fields(self):
        match self.ui:
            case Ui_CreateScience_Dialog():
                knowledge_branch_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name FROM KnowledgeBranch;")
                kbr_names = []
                while knowledge_branch_names_query.next():
                    kbr_names.append(knowledge_branch_names_query.value(0))
                self.ui.comboBox.addItems(kbr_names)
                self.ui.comboBox.setCurrentIndex(0)
            case Ui_CreateArticle_Dialog():
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append(science_names_query.value(0))
                self.ui.comboBox.addItems(science_names)
                self.ui.comboBox.setCurrentIndex(0)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append(author_names_surnames_query.value(0))
                self.ui.comboBox_2.addItems(author_names_surnames)
                self.ui.comboBox_2.setCurrentIndex(0)
            case Ui_CreateMonography_Dialog():
                science_names_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT name FROM Science;")
                science_names = []
                while science_names_query.next():
                    science_names.append(science_names_query.value(0))
                self.ui.comboBox.addItems(science_names)
                self.ui.comboBox.setCurrentIndex(0)
                author_names_surnames_query = KnowledgeBranchTable.execute_query_with_parameters("SELECT (name || ' ' || surname) as nameSurname FROM Author;")
                author_names_surnames = []
                while author_names_surnames_query.next():
                    author_names_surnames.append(author_names_surnames_query.value(0))
                self.ui.comboBox_2.addItems(author_names_surnames)
                self.ui.comboBox_2.setCurrentIndex(0)
                
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryCataloger()
    window.show()

    sys.exit(app.exec())