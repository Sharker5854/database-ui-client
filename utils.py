from ui_components.ui_mainwindow import Ui_MainWindow


class MainWindowUtils:
    @staticmethod
    def make_tabs_current_consistently(ui: Ui_MainWindow):
        ui.tabWidget.setCurrentIndex(0)
        ui.tabWidget.setCurrentIndex(4)
        ui.tabWidget.setCurrentIndex(3)
        ui.tabWidget.setCurrentIndex(2)
        ui.tabWidget.setCurrentIndex(1)
        ui.tabWidget.setCurrentIndex(0)
    
    @staticmethod
    def make_all_delete_buttons_disabled(ui: Ui_MainWindow):
        ui.deleteButton.setEnabled(False)
        ui.deleteButton_3.setEnabled(False)
        ui.deleteButton_4.setEnabled(False)
        ui.deleteButton_5.setEnabled(False)
        ui.deleteButton_6.setEnabled(False)


    @staticmethod
    def make_all_edit_buttons_disabled(ui: Ui_MainWindow):
        ui.editButton.setEnabled(False)
        ui.editButton_3.setEnabled(False)
        ui.editButton_4.setEnabled(False)
        ui.editButton_5.setEnabled(False)
        ui.editButton_6.setEnabled(False)        