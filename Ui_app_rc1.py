# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_app_rc1AQDJma.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(863, 620)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 85);\n"
"\n"
"border: 1px solid #4a4a4a;\n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;\n"
"border-bottom-right-radius: 4px;\n"
"border-bottom-left-radius: 4px;")
        MainWindow.setDocumentMode(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(132, 132, 132);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.display_user_details = QLabel(self.frame)
        self.display_user_details.setObjectName(u"display_user_details")
        self.display_user_details.setGeometry(QRect(40, 160, 771, 101))
        self.display_user_details.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.display_user_details.setAlignment(Qt.AlignCenter)
        self.display_date = QLabel(self.frame)
        self.display_date.setObjectName(u"display_date")
        self.display_date.setGeometry(QRect(30, 50, 61, 16))
        self.display_date.setStyleSheet(u"background-color: rgb(85, 85, 85);")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(720, 40, 91, 48))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.in_time = QRadioButton(self.layoutWidget)
        self.in_time.setObjectName(u"in_time")
        self.in_time.setStyleSheet(u"background-color: rgb(193,205,205);")

        self.verticalLayout_2.addWidget(self.in_time)

        self.out_time = QRadioButton(self.layoutWidget)
        self.out_time.setObjectName(u"out_time")
        self.out_time.setStyleSheet(u"background-color: rgb(193,205,205);")

        self.verticalLayout_2.addWidget(self.out_time)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 20, 59, 20))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.display_time = QLabel(self.layoutWidget1)
        self.display_time.setObjectName(u"display_time")
        self.display_time.setStyleSheet(u"background-color: rgb(85, 85, 85);")

        self.horizontalLayout.addWidget(self.display_time)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 140, 531, 31))
        self.label_6.setStyleSheet(u"background-color: rgb(85, 85, 85);\n"
"font: 900 9pt \"Arial Black\";")
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setTextFormat(Qt.RichText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(132, 132, 132);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 20, 481, 41))
        font = QFont()
        font.setFamilies([u"Stencil"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"\n"
"font: 20pt \"Stencil\";\n"
"background-color: rgb(169,169,169);")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 80, 401, 211))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.frame_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 20, 371, 121))
        self.formLayout = QFormLayout(self.layoutWidget2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.uid_text = QLineEdit(self.layoutWidget2)
        self.uid_text.setObjectName(u"uid_text")
        self.uid_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.uid_text.setFrame(True)
        self.uid_text.setCursorPosition(0)
        self.uid_text.setReadOnly(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.uid_text)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.name_text = QLineEdit(self.layoutWidget2)
        self.name_text.setObjectName(u"name_text")
        self.name_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_text)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.wwid_text = QLineEdit(self.layoutWidget2)
        self.wwid_text.setObjectName(u"wwid_text")
        self.wwid_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.wwid_text)

        self.model_text = QLineEdit(self.layoutWidget2)
        self.model_text.setObjectName(u"model_text")
        self.model_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.model_text)

        self.update_key = QPushButton(self.frame_3)
        self.update_key.setObjectName(u"update_key")
        self.update_key.setGeometry(QRect(310, 150, 75, 24))
        self.update_key.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(419, 80, 411, 211))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.display_user_details.setText("")
        self.display_date.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Date</span></p></body></html>", None))
        self.in_time.setText(QCoreApplication.translate("MainWindow", u"IN", None))
        self.out_time.setText(QCoreApplication.translate("MainWindow", u"OUT", None))
        self.display_time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Time</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Display Employee Details</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Create New User ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">UID</span></p></body></html>", None))
        self.uid_text.setInputMask("")
        self.uid_text.setText("")
        self.uid_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee UID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">NAME</span></p></body></html>", None))
        self.name_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">WWID</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">LAPTOP MODEL</span></p></body></html>", None))
        self.wwid_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee WWID", None))
        self.model_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee Laptop Model", None))
        self.update_key.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

