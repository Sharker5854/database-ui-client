# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_article.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 519)
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
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 20pt;\n"
"	text-align: center;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

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


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.textEdit = QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 100))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(94, 92, 100);\n"
"	border-radius: 4px;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"}")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.frame)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.comboBox = QComboBox(self.groupBox_5)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(220, 27))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(94, 92, 100);\n"
"	border-radius: 4px;\n"
"	color: #FFFFFF;\n"
"}")

        self.verticalLayout_6.addWidget(self.comboBox)


        self.verticalLayout_7.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.groupBox_6)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(220, 27))
        self.comboBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(94, 92, 100);\n"
"	border-radius: 4px;\n"
"	color: #FFFFFF;\n"
"}")

        self.verticalLayout_8.addWidget(self.comboBox_2)


        self.verticalLayout_7.addWidget(self.groupBox_6)

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
"	background-color: rgb(129, 61, 156);\n"
"	border-radius: 3px;\n"
"	height: 35px;\n"
"	color: #FFFFFF;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 69, 176);\n"
"}")

        self.verticalLayout_7.addWidget(self.addButton_6)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Modify Article", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u0442\u0430\u0442\u044c\u044e", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEdit.setText("")
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.groupBox_5.setTitle("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0443\u043a\u0430", None))
        self.groupBox_6.setTitle("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.addButton_6.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

