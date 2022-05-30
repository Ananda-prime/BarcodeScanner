# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_app_rc2ICyxbB.ui'
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
        MainWindow.resize(863, 641)
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
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.display_user_details.setFont(font)
        self.display_user_details.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.display_user_details.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(730, 20, 91, 48))
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

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 140, 531, 31))
        self.label_6.setStyleSheet(u"background-color: rgb(85, 85, 85);\n"
"font: 900 9pt \"Arial Black\";")
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setTextFormat(Qt.RichText)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.display_time = QLabel(self.frame)
        self.display_time.setObjectName(u"display_time")
        self.display_time.setGeometry(QRect(10, 10, 121, 41))
        self.display_time.setStyleSheet(u"background-color: rgb(85, 85, 85);")
        self.display_time.setAlignment(Qt.AlignCenter)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(260, 100, 321, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.scanbarcode = QLineEdit(self.layoutWidget1)
        self.scanbarcode.setObjectName(u"scanbarcode")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanbarcode.sizePolicy().hasHeightForWidth())
        self.scanbarcode.setSizePolicy(sizePolicy)
        self.scanbarcode.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.scanbarcode)

        self.enter = QPushButton(self.layoutWidget1)
        self.enter.setObjectName(u"enter")
        self.enter.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy1)
        self.enter.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";\n"
"")

        self.horizontalLayout.addWidget(self.enter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(132, 132, 132);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.frame_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 70, 371, 152))
        self.formLayout = QFormLayout(self.layoutWidget2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.serial_id = QLabel(self.layoutWidget2)
        self.serial_id.setObjectName(u"serial_id")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.serial_id)

        self.serialid_text = QLineEdit(self.layoutWidget2)
        self.serialid_text.setObjectName(u"serialid_text")
        self.serialid_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.serialid_text.setFrame(True)
        self.serialid_text.setCursorPosition(0)
        self.serialid_text.setReadOnly(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.serialid_text)

        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.uid_text = QLineEdit(self.layoutWidget2)
        self.uid_text.setObjectName(u"uid_text")
        self.uid_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.uid_text.setFrame(True)
        self.uid_text.setCursorPosition(0)
        self.uid_text.setReadOnly(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.uid_text)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.wwid_text = QLineEdit(self.layoutWidget2)
        self.wwid_text.setObjectName(u"wwid_text")
        self.wwid_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.wwid_text)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.model_text = QLineEdit(self.layoutWidget2)
        self.model_text.setObjectName(u"model_text")
        self.model_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.model_text)

        self.name_text = QLineEdit(self.layoutWidget2)
        self.name_text.setObjectName(u"name_text")
        self.name_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.name_text)

        self.update_key = QPushButton(self.frame_3)
        self.update_key.setObjectName(u"update_key")
        self.update_key.setGeometry(QRect(310, 230, 75, 24))
        self.update_key.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 361, 31))
        font1 = QFont()
        font1.setFamilies([u"Stencil"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"\n"
"font: 20pt \"Stencil\";\n"
"background-color: rgb(169,169,169);")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 381, 31))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"\n"
"font: 20pt \"Stencil\";\n"
"background-color: rgb(169,169,169);")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 70, 281, 71))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.display_user_details.setText("")
        self.in_time.setText(QCoreApplication.translate("MainWindow", u"IN", None))
        self.out_time.setText(QCoreApplication.translate("MainWindow", u"OUT", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Display Employee Details</span></p></body></html>", None))
        self.display_time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Time</span></p></body></html>", None))
        self.scanbarcode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scan the barcode", None))
        self.enter.setText(QCoreApplication.translate("MainWindow", u"     Enter      ", None))
        self.serial_id.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">SERIAL ID</span></p></body></html>", None))
        self.serialid_text.setInputMask("")
        self.serialid_text.setText("")
        self.serialid_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee Serial ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">UID</span></p></body></html>", None))
        self.uid_text.setInputMask("")
        self.uid_text.setText("")
        self.uid_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee UID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">NAME</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">WWID</span></p></body></html>", None))
        self.wwid_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee WWID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">LAPTOP MODEL</span></p></body></html>", None))
        self.model_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee Laptop Model", None))
        self.name_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Employee Name", None))
        self.update_key.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Create New Employee Details</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Create New EMPLOYEE Barcode </span></p></body></html>", None))
        self.label_8.setText("")
    # retranslateUi

