# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ceshi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 477)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.plainTextEdit_data = QPlainTextEdit(Form)
        self.plainTextEdit_data.setObjectName(u"plainTextEdit_data")

        self.verticalLayout_2.addWidget(self.plainTextEdit_data)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_image_result = QLabel(Form)
        self.label_image_result.setObjectName(u"label_image_result")
        self.label_image_result.setMinimumSize(QSize(180, 80))
        self.label_image_result.setMaximumSize(QSize(180, 80))

        self.verticalLayout.addWidget(self.label_image_result)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.plainTextEdit_re_data = QPlainTextEdit(Form)
        self.plainTextEdit_re_data.setObjectName(u"plainTextEdit_re_data")

        self.verticalLayout.addWidget(self.plainTextEdit_re_data)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u6570\u636e\u5305", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u56fe\u50cf\u4fe1\u606f", None))
        self.label_image_result.setText(QCoreApplication.translate("Form", u"\u56fe\u50cf\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5339\u914d\u6570\u636e", None))
    # retranslateUi

