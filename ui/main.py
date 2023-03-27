# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 600)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBox_methods = QComboBox(self.centralwidget)
        self.comboBox_methods.addItem("")
        self.comboBox_methods.addItem("")
        self.comboBox_methods.setObjectName(u"comboBox_methods")

        self.horizontalLayout_5.addWidget(self.comboBox_methods)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.label_2)

        self.comboBox_encode = QComboBox(self.centralwidget)
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.setObjectName(u"comboBox_encode")
        self.comboBox_encode.setMinimumSize(QSize(100, 0))
        self.comboBox_encode.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_encode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.lineEdit_post_2 = QLineEdit(self.frame)
        self.lineEdit_post_2.setObjectName(u"lineEdit_post_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_post_2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label_9)

        self.comboBox_content_type_2 = QComboBox(self.frame)
        self.comboBox_content_type_2.addItem("")
        self.comboBox_content_type_2.addItem("")
        self.comboBox_content_type_2.addItem("")
        self.comboBox_content_type_2.setObjectName(u"comboBox_content_type_2")

        self.horizontalLayout_6.addWidget(self.comboBox_content_type_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_type = QComboBox(self.centralwidget)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setMinimumSize(QSize(100, 0))
        self.comboBox_type.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.comboBox_type)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_type_text = QLineEdit(self.centralwidget)
        self.lineEdit_type_text.setObjectName(u"lineEdit_type_text")
        self.lineEdit_type_text.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_type_text)

        self.pushButton_ceshi = QPushButton(self.centralwidget)
        self.pushButton_ceshi.setObjectName(u"pushButton_ceshi")
        self.pushButton_ceshi.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.pushButton_ceshi)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_ip = QLabel(self.centralwidget)
        self.label_ip.setObjectName(u"label_ip")

        self.horizontalLayout_3.addWidget(self.label_ip)

        self.lineEdit_url = QLineEdit(self.centralwidget)
        self.lineEdit_url.setObjectName(u"lineEdit_url")
        self.lineEdit_url.setMinimumSize(QSize(200, 26))
        self.lineEdit_url.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_url.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lineEdit_url)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(80, 28))
        self.pushButton_start.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.pushButton_start)

        self.pushButton_path = QPushButton(self.centralwidget)
        self.pushButton_path.setObjectName(u"pushButton_path")
        self.pushButton_path.setMinimumSize(QSize(80, 28))

        self.horizontalLayout_3.addWidget(self.pushButton_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_web = QPushButton(self.centralwidget)
        self.pushButton_web.setObjectName(u"pushButton_web")
        self.pushButton_web.setMinimumSize(QSize(100, 28))
        self.pushButton_web.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton_web)

        self.label_code_result = QLabel(self.centralwidget)
        self.label_code_result.setObjectName(u"label_code_result")
        self.label_code_result.setMinimumSize(QSize(180, 0))
        self.label_code_result.setMaximumSize(QSize(180, 80))

        self.verticalLayout.addWidget(self.label_code_result)


        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget_result = QTableWidget(self.centralwidget)
        if (self.tableWidget_result.columnCount() < 4):
            self.tableWidget_result.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_result.setObjectName(u"tableWidget_result")
        self.tableWidget_result.setMinimumSize(QSize(0, 0))
        self.tableWidget_result.setSortingEnabled(True)
        self.tableWidget_result.horizontalHeader().setVisible(True)
        self.tableWidget_result.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_result.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_result.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.tableWidget_result)

        self.plainTextEdit_log = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_log.setObjectName(u"plainTextEdit_log")
        self.plainTextEdit_log.setMinimumSize(QSize(180, 0))
        self.plainTextEdit_log.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_2.addWidget(self.plainTextEdit_log)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Code Identify v1.1 by \u6d45\u7b11996 ", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u4f5c\u8005", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u6c42\u65b9\u6cd5", None))
        self.comboBox_methods.setItemText(0, QCoreApplication.translate("MainWindow", u"GET", None))
        self.comboBox_methods.setItemText(1, QCoreApplication.translate("MainWindow", u"POST", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u65b9\u6cd5", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ddddocr", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Muggle Ocr", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Easyocr", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u6570\u636e\u7f16\u7801", None))
        self.comboBox_encode.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.comboBox_encode.setItemText(1, QCoreApplication.translate("MainWindow", u"Base64", None))
        self.comboBox_encode.setItemText(2, QCoreApplication.translate("MainWindow", u"Hex", None))
        self.comboBox_encode.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e8c\u8fdb\u5236", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Post Data:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Content-Type:", None))
        self.comboBox_content_type_2.setItemText(0, QCoreApplication.translate("MainWindow", u"application/x-www-form-urlencoded", None))
        self.comboBox_content_type_2.setItemText(1, QCoreApplication.translate("MainWindow", u"application/ison", None))
        self.comboBox_content_type_2.setItemText(2, QCoreApplication.translate("MainWindow", u"multipart/form-data", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u7801\u6570\u636e\u5339\u914d", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Response", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Re Match", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("MainWindow", u"JSON Match", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u89c4\u5219", None))
        self.pushButton_ceshi.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u5339\u914d", None))
        self.label_ip.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.lineEdit_url.setText("")
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.pushButton_path.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u56fe\u7247", None))
        self.pushButton_web.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542fWEB\u63a5\u53e3", None))
        self.label_code_result.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem1 = self.tableWidget_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247", None));
        ___qtablewidgetitem2 = self.tableWidget_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u7ed3\u679c", None));
        ___qtablewidgetitem3 = self.tableWidget_result.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u65b9\u6cd5", None));
        self.plainTextEdit_log.setPlainText("")
    # retranslateUi

