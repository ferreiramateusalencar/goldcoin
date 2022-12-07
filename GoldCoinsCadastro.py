# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoldCoinsCadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GoldCoinsTelaSMS import Ui_TelaSMS


class Ui_TelaCadastro(object):
    def OpenMessagesConfig(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TelaSMS()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, TelaCadastro):
        TelaCadastro.setObjectName("TelaCadastro")
        TelaCadastro.resize(1005, 750)
        self.centralwidget = QtWidgets.QWidget(TelaCadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.centralwidget)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setStyleSheet("background-color: #fff;")
        self.top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.verticalLayout.addWidget(self.top)
        self.containerlogo = QtWidgets.QFrame(self.centralwidget)
        self.containerlogo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.containerlogo.setStyleSheet("background-color: #fff;")
        self.containerlogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.containerlogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.containerlogo.setObjectName("containerlogo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.containerlogo)
        self.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo_3 = QtWidgets.QFrame(self.containerlogo)
        self.logo_3.setMaximumSize(QtCore.QSize(281, 61))
        self.logo_3.setStyleSheet("background-repeat: norepeat;\n"
"background-image: url(:/Logo/Icone GoldCoins pqn.png);")
        self.logo_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_3.setObjectName("logo_3")
        self.verticalLayout_2.addWidget(self.logo_3)
        self.verticalLayout.addWidget(self.containerlogo)
        self.container = QtWidgets.QFrame(self.centralwidget)
        self.container.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.container.setStyleSheet("background-color: #fff;")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.container)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.container_3 = QtWidgets.QFrame(self.container)
        self.container_3.setMaximumSize(QtCore.QSize(1000, 1200))
        self.container_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.container_3.setStyleSheet("background-color: #fff;")
        self.container_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_3.setObjectName("container_3")
        self.label_4 = QtWidgets.QLabel(self.container_3)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 201, 61))
        self.label_4.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.container_3)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 71, 31))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);")
        self.label_5.setObjectName("label_5")
        self.BotaoSair = QtWidgets.QPushButton(self.container_3)
        self.BotaoSair.setGeometry(QtCore.QRect(120, 470, 112, 51))
        self.BotaoSair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotaoSair.setStyleSheet("QPushButton {\n"
"    color: #81BAFD;\n"
"    background-color: #fff;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #81BAFD;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #738FF0;\n"
"    border: 2px solid#738FF0;\n"
"}\n"
"")
        self.BotaoSair.setObjectName("BotaoSair")
        self.frame = QtWidgets.QFrame(self.container_3)
        self.frame.setGeometry(QtCore.QRect(20, 70, 961, 20))
        self.frame.setStyleSheet("background-image: url(:/Line/Line.png);\n"
"background-repeat: norepeat;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.input_nome = QtWidgets.QTextEdit(self.container_3)
        self.input_nome.setGeometry(QtCore.QRect(30, 150, 481, 31))
        self.input_nome.setAutoFillBackground(True)
        self.input_nome.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.input_nome.setObjectName("input_nome")
        self.label_6 = QtWidgets.QLabel(self.container_3)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 221, 31))
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);")
        self.label_6.setObjectName("label_6")
        self.input_numero = QtWidgets.QTextEdit(self.container_3)
        self.input_numero.setGeometry(QtCore.QRect(30, 260, 481, 31))
        self.input_numero.setObjectName("input_numero")
        self.input_email = QtWidgets.QTextEdit(self.container_3)
        self.input_email.setGeometry(QtCore.QRect(30, 370, 481, 31))
        self.input_email.setObjectName("input_email")
        self.label_7 = QtWidgets.QLabel(self.container_3)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 221, 31))
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);")
        self.label_7.setObjectName("label_7")
        self.BotaoProsseguir = QtWidgets.QPushButton(self.container_3, clicked = lambda: self.OpenMessagesConfig())
        self.BotaoProsseguir.setGeometry(QtCore.QRect(690, 470, 151, 51))
        self.BotaoProsseguir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotaoProsseguir.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    background-color: #81BAFD;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #738FF0;\n"
"}\n"
"")
        self.BotaoProsseguir.setObjectName("BotaoProsseguir")
        self.horizontalLayout_2.addWidget(self.container_3)
        self.verticalLayout.addWidget(self.container)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bottom.setStyleSheet("background-color: #fff;")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.label_8 = QtWidgets.QLabel(self.bottom)
        self.label_8.setGeometry(QtCore.QRect(820, 10, 178, 18))
        self.label_8.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);\n"
"font-weight: bold;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.bottom)
        TelaCadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaCadastro)
        self.BotaoSair.clicked.connect(TelaCadastro.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TelaCadastro)

    def retranslateUi(self, TelaCadastro):
        _translate = QtCore.QCoreApplication.translate
        TelaCadastro.setWindowTitle(_translate("TelaCadastro", "MainWindow"))
        self.label_4.setText(_translate("TelaCadastro", "Cadastro"))
        self.label_5.setText(_translate("TelaCadastro", "Nome:"))
        self.BotaoSair.setText(_translate("TelaCadastro", "Sair"))
        self.input_nome.setHtml(_translate("TelaCadastro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("TelaCadastro", "Número de telefone:"))
        self.label_7.setText(_translate("TelaCadastro", "E-mail:"))
        self.BotaoProsseguir.setText(_translate("TelaCadastro", "Prosseguir"))
        self.label_8.setText(_translate("TelaCadastro", "2022 CopyRight © Solutech"))
#import images_rc
