# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoldCoinsTelaInfoDaConta.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelaInfoConta(object):
    def setupUi(self, TelaInfoConta):
        TelaInfoConta.setObjectName("TelaInfoConta")
        TelaInfoConta.resize(1005, 694)
        self.centralwidget = QtWidgets.QWidget(TelaInfoConta)
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.containerlogo)
        self.verticalLayout_4.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo_5 = QtWidgets.QFrame(self.containerlogo)
        self.logo_5.setMaximumSize(QtCore.QSize(281, 61))
        self.logo_5.setStyleSheet("background-image: url(:/Logo/Icone GoldCoins pqn.png);\n"
"background-repeat: norepeat;")
        self.logo_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_5.setObjectName("logo_5")
        self.verticalLayout_4.addWidget(self.logo_5)
        self.verticalLayout.addWidget(self.containerlogo)
        self.container_3 = QtWidgets.QFrame(self.centralwidget)
        self.container_3.setMaximumSize(QtCore.QSize(1000, 1200))
        self.container_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.container_3.setStyleSheet("background-color: #fff;")
        self.container_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_3.setObjectName("container_3")
        self.label_8 = QtWidgets.QLabel(self.container_3)
        self.label_8.setGeometry(QtCore.QRect(30, 93, 201, 51))
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);\n"
"font-weight: bold;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.container_3)
        self.label_9.setGeometry(QtCore.QRect(30, 173, 71, 31))
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.container_3)
        self.label_10.setGeometry(QtCore.QRect(30, 225, 221, 31))
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.container_3)
        self.label_11.setGeometry(QtCore.QRect(30, 275, 71, 31))
        self.label_11.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.container_3)
        self.label_12.setGeometry(QtCore.QRect(30, 20, 361, 31))
        self.label_12.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;")
        self.label_12.setObjectName("label_12")
        self.input_numerotelefone = QtWidgets.QLineEdit(self.container_3)
        self.input_numerotelefone.setGeometry(QtCore.QRect(399, 27, 281, 31))
        self.input_numerotelefone.setStyleSheet("border: 1px solid #81BAFD;\n"
"border-radius: 5px;")
        self.input_numerotelefone.setObjectName("input_numerotelefone")
        self.label_13 = QtWidgets.QLabel(self.container_3)
        self.label_13.setGeometry(QtCore.QRect(30, 344, 201, 31))
        self.label_13.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.container_3)
        self.label_14.setGeometry(QtCore.QRect(30, 394, 281, 31))
        self.label_14.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;")
        self.label_14.setObjectName("label_14")
        self.BotaoConfirmar = QtWidgets.QPushButton(self.container_3)
        self.BotaoConfirmar.setGeometry(QtCore.QRect(703, 22, 101, 41))
        self.BotaoConfirmar.setStyleSheet("QPushButton {\n"
"background-color: #81BAFD;\n"
"color: #fff;\n"
"border-radius: 5px;\n"
"border: none;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #738FF0 \n"
"}")
        self.BotaoConfirmar.setObjectName("BotaoConfirmar")
        self.BotaoAlterar = QtWidgets.QPushButton(self.container_3)
        self.BotaoAlterar.setGeometry(QtCore.QRect(580, 470, 101, 41))
        self.BotaoAlterar.setStyleSheet("QPushButton {\n"
"background-color: #81BAFD;\n"
"color: #fff;\n"
"border-radius: 5px;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #738FF0 \n"
"}")
        self.BotaoAlterar.setObjectName("BotaoAlterar")
        self.BotaoSalvar = QtWidgets.QPushButton(self.container_3)
        self.BotaoSalvar.setGeometry(QtCore.QRect(700, 470, 101, 41))
        self.BotaoSalvar.setStyleSheet("QPushButton {\n"
"background-color: #81BAFD;\n"
"color: #fff;\n"
"border-radius: 5px;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #738FF0 \n"
"}")
        self.BotaoSalvar.setObjectName("BotaoSalvar")
        self.BotaoDeletar = QtWidgets.QPushButton(self.container_3)
        self.BotaoDeletar.setGeometry(QtCore.QRect(860, 471, 101, 41))
        self.BotaoDeletar.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    background-color: #FF9090;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E75858;\n"
"}\n"
"")
        self.BotaoDeletar.setObjectName("BotaoDeletar")
        self.BotaoSair = QtWidgets.QPushButton(self.container_3)
        self.BotaoSair.setGeometry(QtCore.QRect(100, 479, 101, 41))
        self.BotaoSair.setStyleSheet("QPushButton {\n"
"background-color: #fff;\n"
"color: #81BAFD;\n"
"border-radius: 5px;\n"
"border: 2px solid #81BAFD;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"}\n"
"\n"
"")
        self.BotaoSair.setObjectName("BotaoSair")
        self.campoNome = QtWidgets.QLabel(self.container_3)
        self.campoNome.setGeometry(QtCore.QRect(110, 170, 651, 31))
        self.campoNome.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.campoNome.setText("")
        self.campoNome.setObjectName("campoNome")
        self.CampoNumero = QtWidgets.QLabel(self.container_3)
        self.CampoNumero.setGeometry(QtCore.QRect(250, 220, 511, 31))
        self.CampoNumero.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.CampoNumero.setText("")
        self.CampoNumero.setObjectName("CampoNumero")
        self.CampoEmail = QtWidgets.QLabel(self.container_3)
        self.CampoEmail.setGeometry(QtCore.QRect(110, 270, 651, 31))
        self.CampoEmail.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.CampoEmail.setText("")
        self.CampoEmail.setObjectName("CampoEmail")
        self.CampoMoedas = QtWidgets.QLabel(self.container_3)
        self.CampoMoedas.setGeometry(QtCore.QRect(236, 344, 531, 31))
        self.CampoMoedas.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.CampoMoedas.setText("")
        self.CampoMoedas.setObjectName("CampoMoedas")
        self.CampoFrequenciaMsg = QtWidgets.QLabel(self.container_3)
        self.CampoFrequenciaMsg.setGeometry(QtCore.QRect(320, 392, 451, 31))
        self.CampoFrequenciaMsg.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.CampoFrequenciaMsg.setText("")
        self.CampoFrequenciaMsg.setObjectName("CampoFrequenciaMsg")
        self.line = QtWidgets.QFrame(self.container_3)
        self.line.setGeometry(QtCore.QRect(30, 80, 941, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.container_3)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bottom.setStyleSheet("background-color: #fff;")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.label_4 = QtWidgets.QLabel(self.bottom)
        self.label_4.setGeometry(QtCore.QRect(820, 10, 178, 18))
        self.label_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.bottom)
        TelaInfoConta.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaInfoConta)
        self.BotaoSair.clicked.connect(TelaInfoConta.close) # type: ignore
        self.BotaoConfirmar.clicked.connect(self.input_numerotelefone.update) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TelaInfoConta)

    def retranslateUi(self, TelaInfoConta):
        _translate = QtCore.QCoreApplication.translate
        TelaInfoConta.setWindowTitle(_translate("TelaInfoConta", "MainWindow"))
        self.label_8.setText(_translate("TelaInfoConta", "Conta"))
        self.label_9.setText(_translate("TelaInfoConta", "Nome:"))
        self.label_10.setText(_translate("TelaInfoConta", "Número de telefone:"))
        self.label_11.setText(_translate("TelaInfoConta", "E-mail:"))
        self.label_12.setText(_translate("TelaInfoConta", "Informe o seu número de telefone:"))
        self.label_13.setText(_translate("TelaInfoConta", "Moedas escolhidas:"))
        self.label_14.setText(_translate("TelaInfoConta", "Frequência das mensagens:"))
        self.BotaoConfirmar.setText(_translate("TelaInfoConta", "Confirmar"))
        self.BotaoAlterar.setText(_translate("TelaInfoConta", "Alterar"))
        self.BotaoSalvar.setText(_translate("TelaInfoConta", "Salvar"))
        self.BotaoDeletar.setText(_translate("TelaInfoConta", "Deletar"))
        self.BotaoSair.setText(_translate("TelaInfoConta", "Sair"))
        self.label_4.setText(_translate("TelaInfoConta", "2022 CopyRight © Solutech"))
#import images_rc
