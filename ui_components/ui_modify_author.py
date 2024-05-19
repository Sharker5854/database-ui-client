# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_author.ui'
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
        Dialog.resize(374, 538)
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


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.frame)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(94, 92, 100);\n"
"	border-radius: 4px;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"}")

        self.verticalLayout_6.addWidget(self.lineEdit_4)


        self.verticalLayout_7.addWidget(self.groupBox_5)

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


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.groupBox_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(94, 92, 100);\n"
"	border-radius: 4px;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"}")

        self.verticalLayout_8.addWidget(self.lineEdit_5)


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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Modify Author", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0430\u0432\u0442\u043e\u0440\u0430", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.lineEdit.setText("")
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_3.setText("")
        self.groupBox_5.setTitle("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e (\u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)", None))
        self.lineEdit_4.setText("")
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.groupBox_6.setTitle("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"E-mail (\u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)", None))
        self.lineEdit_5.setText("")
        self.addButton_6.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

