# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_entrada = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_entrada.setObjectName("plainTextEdit_entrada")
        self.gridLayout.addWidget(self.plainTextEdit_entrada, 1, 1, 1, 1)
        self.plainTextEdit_salida = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_salida.setEnabled(True)
        self.plainTextEdit_salida.setReadOnly(True)
        self.plainTextEdit_salida.setObjectName("plainTextEdit_salida")
        self.gridLayout.addWidget(self.plainTextEdit_salida, 1, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_abrir = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_abrir.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_abrir.setObjectName("pushButton_abrir")
        self.verticalLayout.addWidget(self.pushButton_abrir)
        self.pushButton_analizar = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_analizar.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_analizar.setObjectName("pushButton_analizar")
        self.verticalLayout.addWidget(self.pushButton_analizar)
        self.gridLayout.addWidget(self.groupBox, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 26))
        self.menubar.setObjectName("menubar")
        self.menuAnalizador_Lexico = QtWidgets.QMenu(self.menubar)
        self.menuAnalizador_Lexico.setObjectName("menuAnalizador_Lexico")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAnalizador_Lexico.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Botones"))
        self.pushButton_abrir.setText(_translate("MainWindow", "Abrir Archivo"))
        self.pushButton_analizar.setText(_translate("MainWindow", "Analizar"))
        self.label.setText(_translate("MainWindow", "Entrada"))
        self.label_2.setText(_translate("MainWindow", "Salida"))
        self.menuAnalizador_Lexico.setTitle(_translate("MainWindow", "Analizador Lexico"))
