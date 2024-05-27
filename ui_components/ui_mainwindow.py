# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 509)
        MainWindow.setStyleSheet(u"background-color: rgb(27, 23, 38);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(27, 23, 38);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(23, 20, 33);\n"
"color: #FFFFFF;")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.KnowledgeBranch = QWidget()
        self.KnowledgeBranch.setObjectName(u"KnowledgeBranch")
        self.verticalLayout = QVBoxLayout(self.KnowledgeBranch)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.KnowledgeBranch)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.groupBox = QGroupBox(self.KnowledgeBranch)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deleteButton = QPushButton(self.groupBox)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(192, 28, 40);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 31, 43);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_2.addWidget(self.deleteButton)

        self.editButton = QPushButton(self.groupBox)
        self.editButton.setObjectName(u"editButton")
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(129, 61, 156);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 69, 176);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_2.addWidget(self.editButton)

        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 162, 105);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 186, 119);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_2.addWidget(self.addButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.tabWidget.addTab(self.KnowledgeBranch, "")
        self.Science = QWidget()
        self.Science.setObjectName(u"Science")
        self.verticalLayout_3 = QVBoxLayout(self.Science)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView_2 = QTableView(self.Science)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_3.addWidget(self.tableView_2)

        self.groupBox_2 = QGroupBox(self.Science)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.deleteButton_3 = QPushButton(self.groupBox_2)
        self.deleteButton_3.setObjectName(u"deleteButton_3")
        sizePolicy.setHeightForWidth(self.deleteButton_3.sizePolicy().hasHeightForWidth())
        self.deleteButton_3.setSizePolicy(sizePolicy)
        self.deleteButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(192, 28, 40);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 31, 43);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_4.addWidget(self.deleteButton_3)

        self.editButton_3 = QPushButton(self.groupBox_2)
        self.editButton_3.setObjectName(u"editButton_3")
        sizePolicy.setHeightForWidth(self.editButton_3.sizePolicy().hasHeightForWidth())
        self.editButton_3.setSizePolicy(sizePolicy)
        self.editButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(129, 61, 156);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 69, 176);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_4.addWidget(self.editButton_3)

        self.addButton_3 = QPushButton(self.groupBox_2)
        self.addButton_3.setObjectName(u"addButton_3")
        sizePolicy.setHeightForWidth(self.addButton_3.sizePolicy().hasHeightForWidth())
        self.addButton_3.setSizePolicy(sizePolicy)
        self.addButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 162, 105);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 186, 119);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_4.addWidget(self.addButton_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.Science, "")
        self.Author = QWidget()
        self.Author.setObjectName(u"Author")
        self.verticalLayout_2 = QVBoxLayout(self.Author)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView_3 = QTableView(self.Author)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_2.addWidget(self.tableView_3)

        self.groupBox_3 = QGroupBox(self.Author)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.deleteButton_4 = QPushButton(self.groupBox_3)
        self.deleteButton_4.setObjectName(u"deleteButton_4")
        sizePolicy.setHeightForWidth(self.deleteButton_4.sizePolicy().hasHeightForWidth())
        self.deleteButton_4.setSizePolicy(sizePolicy)
        self.deleteButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(192, 28, 40);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 31, 43);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_5.addWidget(self.deleteButton_4)

        self.editButton_4 = QPushButton(self.groupBox_3)
        self.editButton_4.setObjectName(u"editButton_4")
        sizePolicy.setHeightForWidth(self.editButton_4.sizePolicy().hasHeightForWidth())
        self.editButton_4.setSizePolicy(sizePolicy)
        self.editButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(129, 61, 156);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 69, 176);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_5.addWidget(self.editButton_4)

        self.addButton_4 = QPushButton(self.groupBox_3)
        self.addButton_4.setObjectName(u"addButton_4")
        sizePolicy.setHeightForWidth(self.addButton_4.sizePolicy().hasHeightForWidth())
        self.addButton_4.setSizePolicy(sizePolicy)
        self.addButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 162, 105);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 186, 119);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_5.addWidget(self.addButton_4)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.Author, "")
        self.Article = QWidget()
        self.Article.setObjectName(u"Article")
        self.verticalLayout_5 = QVBoxLayout(self.Article)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView_4 = QTableView(self.Article)
        self.tableView_4.setObjectName(u"tableView_4")

        self.verticalLayout_5.addWidget(self.tableView_4)

        self.groupBox_4 = QGroupBox(self.Article)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.deleteButton_5 = QPushButton(self.groupBox_4)
        self.deleteButton_5.setObjectName(u"deleteButton_5")
        sizePolicy.setHeightForWidth(self.deleteButton_5.sizePolicy().hasHeightForWidth())
        self.deleteButton_5.setSizePolicy(sizePolicy)
        self.deleteButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(192, 28, 40);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 31, 43);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_6.addWidget(self.deleteButton_5)

        self.editButton_5 = QPushButton(self.groupBox_4)
        self.editButton_5.setObjectName(u"editButton_5")
        sizePolicy.setHeightForWidth(self.editButton_5.sizePolicy().hasHeightForWidth())
        self.editButton_5.setSizePolicy(sizePolicy)
        self.editButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(129, 61, 156);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 69, 176);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_6.addWidget(self.editButton_5)

        self.addButton_5 = QPushButton(self.groupBox_4)
        self.addButton_5.setObjectName(u"addButton_5")
        sizePolicy.setHeightForWidth(self.addButton_5.sizePolicy().hasHeightForWidth())
        self.addButton_5.setSizePolicy(sizePolicy)
        self.addButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 162, 105);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 186, 119);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_6.addWidget(self.addButton_5)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.tabWidget.addTab(self.Article, "")
        self.Monography = QWidget()
        self.Monography.setObjectName(u"Monography")
        self.verticalLayout_4 = QVBoxLayout(self.Monography)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableView_5 = QTableView(self.Monography)
        self.tableView_5.setObjectName(u"tableView_5")

        self.verticalLayout_4.addWidget(self.tableView_5)

        self.groupBox_5 = QGroupBox(self.Monography)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.deleteButton_6 = QPushButton(self.groupBox_5)
        self.deleteButton_6.setObjectName(u"deleteButton_6")
        sizePolicy.setHeightForWidth(self.deleteButton_6.sizePolicy().hasHeightForWidth())
        self.deleteButton_6.setSizePolicy(sizePolicy)
        self.deleteButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(192, 28, 40);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 31, 43);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_7.addWidget(self.deleteButton_6)

        self.editButton_6 = QPushButton(self.groupBox_5)
        self.editButton_6.setObjectName(u"editButton_6")
        sizePolicy.setHeightForWidth(self.editButton_6.sizePolicy().hasHeightForWidth())
        self.editButton_6.setSizePolicy(sizePolicy)
        self.editButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(129, 61, 156);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 69, 176);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_7.addWidget(self.editButton_6)

        self.addButton_6 = QPushButton(self.groupBox_5)
        self.addButton_6.setObjectName(u"addButton_6")
        sizePolicy.setHeightForWidth(self.addButton_6.sizePolicy().hasHeightForWidth())
        self.addButton_6.setSizePolicy(sizePolicy)
        self.addButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 162, 105);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 186, 119);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(154, 153, 150);\n"
"	color: rgb(61, 61, 61);\n"
"}")

        self.horizontalLayout_7.addWidget(self.addButton_6)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.Monography, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library Cataloger", None))
        self.groupBox.setTitle("")
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.KnowledgeBranch), QCoreApplication.translate("MainWindow", u"KnowledgeBranch", None))
        self.groupBox_2.setTitle("")
        self.deleteButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.editButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.addButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Science), QCoreApplication.translate("MainWindow", u"Science", None))
        self.groupBox_3.setTitle("")
        self.deleteButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.editButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.addButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Author), QCoreApplication.translate("MainWindow", u"Author", None))
        self.groupBox_4.setTitle("")
        self.deleteButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.editButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.addButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Article), QCoreApplication.translate("MainWindow", u"Article", None))
        self.groupBox_5.setTitle("")
        self.deleteButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.editButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.addButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Monography), QCoreApplication.translate("MainWindow", u"Monography", None))
    # retranslateUi

