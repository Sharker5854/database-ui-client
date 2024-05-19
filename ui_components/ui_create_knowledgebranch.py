# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_knowledgebranch.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(383, 449)
        Dialog.setStyleSheet(u"background-color: rgb(27, 23, 38);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	color: #FFFFFF;\n"
"};")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 20pt;\n"
"	text-align: center;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(94, 92, 100);\n"
"	border-radius: 4px;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(94, 92, 100);\n"
"	border-radius: 4px;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"}")

        self.verticalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.dateEdit = QDateEdit(self.groupBox_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(130, 27))
        self.dateEdit.setMaximumSize(QSize(130, 27))
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"	color: #FFFFFF;\n"
"	background-color: rgb(61, 56, 70);\n"
"	border-radius: 4px;\n"
"};")

        self.verticalLayout_4.addWidget(self.dateEdit)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.dateEdit_2 = QDateEdit(self.groupBox_4)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(130, 27))
        self.dateEdit_2.setMaximumSize(QSize(130, 27))
        self.dateEdit_2.setStyleSheet(u"QDateEdit {\n"
"	color: #FFFFFF;\n"
"	background-color: rgb(61, 56, 70);\n"
"	border-radius: 4px;\n"
"};")

        self.verticalLayout_5.addWidget(self.dateEdit_2)


        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.addButton_6 = QPushButton(self.frame)
        self.addButton_6.setObjectName(u"addButton_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton_6.sizePolicy().hasHeightForWidth())
        self.addButton_6.setSizePolicy(sizePolicy)
        self.addButton_6.setMaximumSize(QSize(16777215, 40))
        self.addButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 162, 105);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"	color: #FFFFFF;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 186, 119);\n"
"}")

        self.verticalLayout_6.addWidget(self.addButton_6)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create KnowledgeBranch", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u043e\u0442\u0440\u0430\u0441\u043b\u044c \u0437\u043d\u0430\u043d\u0438\u0439", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEdit.setText("")
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.lineEdit_3.setText("")
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.groupBox_4.setTitle("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f", None))
        self.addButton_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

