# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazLS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_subir_img = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subir_img.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_subir_img.setObjectName("btn_subir_img")
        self.horizontalLayout.addWidget(self.btn_subir_img)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.edt_luminancia = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edt_luminancia.setMinimumSize(QtCore.QSize(70, 30))
        self.edt_luminancia.setMinimum(0.0)
        self.edt_luminancia.setMaximum(999.99)
        self.edt_luminancia.setSingleStep(0.1)
        self.edt_luminancia.setObjectName("edt_luminancia")
        self.verticalLayout.addWidget(self.edt_luminancia)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.edt_saturacion = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edt_saturacion.setMinimumSize(QtCore.QSize(70, 30))
        self.edt_saturacion.setMinimum(-99.99)
        self.edt_saturacion.setMaximum(999.99)
        self.edt_saturacion.setSingleStep(0.1)
        self.edt_saturacion.setProperty("value", 1.0)
        self.edt_saturacion.setObjectName("edt_saturacion")
        self.verticalLayout_2.addWidget(self.edt_saturacion)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lbl_img_org = QtWidgets.QLabel(self.centralwidget)
        self.lbl_img_org.setMinimumSize(QtCore.QSize(500, 500))
        self.lbl_img_org.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_org.setObjectName("lbl_img_org")
        self.verticalLayout_3.addWidget(self.lbl_img_org)
        self.verticalLayout_3.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.lbl_img_mod = QtWidgets.QLabel(self.centralwidget)
        self.lbl_img_mod.setMinimumSize(QtCore.QSize(350, 350))
        self.lbl_img_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_mod.setObjectName("lbl_img_mod")
        self.verticalLayout_4.addWidget(self.lbl_img_mod)
        self.verticalLayout_4.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_5.setBuddy(self.edt_luminancia)
        self.label_6.setBuddy(self.edt_saturacion)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jugando con la Luminancia y Saturaci??n"))
        self.btn_subir_img.setText(_translate("MainWindow", "Subir Imagen"))
        self.label_5.setText(_translate("MainWindow", "Luminancia"))
        self.label_6.setText(_translate("MainWindow", "Saturaci??n"))
        self.label_2.setText(_translate("MainWindow", "Imagen Original"))
        self.lbl_img_org.setText(_translate("MainWindow", "Seleccione una imagen para ver una vista previa"))
        self.label_3.setText(_translate("MainWindow", "Imagen Modificada"))
        self.lbl_img_mod.setText(_translate("MainWindow", "Seleccione una imagen para ver una vista previa"))
