# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1439, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.img_org = QtWidgets.QLabel(self.centralwidget)
        self.img_org.setMinimumSize(QtCore.QSize(430, 450))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.img_org.setFont(font)
        self.img_org.setScaledContents(True)
        self.img_org.setAlignment(QtCore.Qt.AlignCenter)
        self.img_org.setObjectName("img_org")
        self.verticalLayout.addWidget(self.img_org)
        self.check_gris = QtWidgets.QCheckBox(self.centralwidget)
        self.check_gris.setObjectName("check_gris")
        self.verticalLayout.addWidget(self.check_gris)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_subir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subir.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_subir.setFont(font)
        self.btn_subir.setObjectName("btn_subir")
        self.horizontalLayout.addWidget(self.btn_subir)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_procesar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_procesar.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_procesar.setFont(font)
        self.btn_procesar.setObjectName("btn_procesar")
        self.horizontalLayout.addWidget(self.btn_procesar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_bin = QtWidgets.QWidget()
        self.tab_bin.setObjectName("tab_bin")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_bin)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_mediana = QtWidgets.QLabel(self.tab_bin)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_mediana.setFont(font)
        self.lbl_mediana.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mediana.setObjectName("lbl_mediana")
        self.verticalLayout_3.addWidget(self.lbl_mediana)
        self.lbl_img_mediana = QtWidgets.QLabel(self.tab_bin)
        self.lbl_img_mediana.setMinimumSize(QtCore.QSize(270, 280))
        self.lbl_img_mediana.setScaledContents(True)
        self.lbl_img_mediana.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_mediana.setObjectName("lbl_img_mediana")
        self.verticalLayout_3.addWidget(self.lbl_img_mediana)
        self.verticalLayout_3.setStretch(1, 2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(304, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_kmeans = QtWidgets.QLabel(self.tab_bin)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_kmeans.setFont(font)
        self.lbl_kmeans.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_kmeans.setObjectName("lbl_kmeans")
        self.verticalLayout_4.addWidget(self.lbl_kmeans)
        self.lbl_img_kmeans = QtWidgets.QLabel(self.tab_bin)
        self.lbl_img_kmeans.setMinimumSize(QtCore.QSize(270, 280))
        self.lbl_img_kmeans.setScaledContents(True)
        self.lbl_img_kmeans.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_kmeans.setObjectName("lbl_img_kmeans")
        self.verticalLayout_4.addWidget(self.lbl_img_kmeans)
        self.verticalLayout_4.setStretch(1, 2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_otsu = QtWidgets.QLabel(self.tab_bin)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_otsu.setFont(font)
        self.lbl_otsu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_otsu.setObjectName("lbl_otsu")
        self.verticalLayout_5.addWidget(self.lbl_otsu)
        self.lbl_img_otsu = QtWidgets.QLabel(self.tab_bin)
        self.lbl_img_otsu.setMinimumSize(QtCore.QSize(270, 280))
        self.lbl_img_otsu.setScaledContents(True)
        self.lbl_img_otsu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_otsu.setObjectName("lbl_img_otsu")
        self.verticalLayout_5.addWidget(self.lbl_img_otsu)
        self.verticalLayout_5.setStretch(1, 2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_bin, "")
        self.tab_bordes = QtWidgets.QWidget()
        self.tab_bordes.setObjectName("tab_bordes")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_bordes)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab_bordes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.rdb_4v = QtWidgets.QRadioButton(self.tab_bordes)
        self.rdb_4v.setObjectName("rdb_4v")
        self.horizontalLayout_3.addWidget(self.rdb_4v)
        self.rdb_8v = QtWidgets.QRadioButton(self.tab_bordes)
        self.rdb_8v.setChecked(True)
        self.rdb_8v.setObjectName("rdb_8v")
        self.horizontalLayout_3.addWidget(self.rdb_8v)
        self.horizontalLayout_3.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.lbl_img_laplaciano = QtWidgets.QLabel(self.tab_bordes)
        self.lbl_img_laplaciano.setMinimumSize(QtCore.QSize(270, 280))
        self.lbl_img_laplaciano.setScaledContents(True)
        self.lbl_img_laplaciano.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_laplaciano.setObjectName("lbl_img_laplaciano")
        self.verticalLayout_2.addWidget(self.lbl_img_laplaciano)
        self.verticalLayout_2.setStretch(1, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(304, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.tab_bordes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.lbl_img_marchine = QtWidgets.QLabel(self.tab_bordes)
        self.lbl_img_marchine.setMinimumSize(QtCore.QSize(270, 280))
        self.lbl_img_marchine.setScaledContents(True)
        self.lbl_img_marchine.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_marchine.setObjectName("lbl_img_marchine")
        self.verticalLayout_8.addWidget(self.lbl_img_marchine)
        self.verticalLayout_8.setStretch(1, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(2, 2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_16 = QtWidgets.QLabel(self.tab_bordes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_10.addWidget(self.label_16)
        self.lbl_img_front_ex = QtWidgets.QLabel(self.tab_bordes)
        self.lbl_img_front_ex.setMinimumSize(QtCore.QSize(270, 280))
        self.lbl_img_front_ex.setScaledContents(True)
        self.lbl_img_front_ex.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_front_ex.setObjectName("lbl_img_front_ex")
        self.verticalLayout_10.addWidget(self.lbl_img_front_ex)
        self.verticalLayout_10.setStretch(1, 2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_10)
        spacerItem9 = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.tab_bordes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.lbl_img_front_int = QtWidgets.QLabel(self.tab_bordes)
        self.lbl_img_front_int.setMinimumSize(QtCore.QSize(270, 280))
        self.lbl_img_front_int.setScaledContents(True)
        self.lbl_img_front_int.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_front_int.setObjectName("lbl_img_front_int")
        self.verticalLayout_9.addWidget(self.lbl_img_front_int)
        self.verticalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(2, 2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab_bordes, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binarizaci??n y Fronteras"))
        self.img_org.setText(_translate("MainWindow", "Seleccione una imagen para previsualizarla"))
        self.check_gris.setText(_translate("MainWindow", "Escala de Grises"))
        self.btn_subir.setText(_translate("MainWindow", "Subir Imagen"))
        self.btn_procesar.setText(_translate("MainWindow", "Procesar"))
        self.lbl_mediana.setText(_translate("MainWindow", "50% - 50% (Umbral Mediana)"))
        self.lbl_img_mediana.setText(_translate("MainWindow", "Suba una imagen"))
        self.lbl_kmeans.setText(_translate("MainWindow", "K-Means"))
        self.lbl_img_kmeans.setText(_translate("MainWindow", "Suba una imagen"))
        self.lbl_otsu.setText(_translate("MainWindow", "Otsu"))
        self.lbl_img_otsu.setText(_translate("MainWindow", "Suba una imagen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bin), _translate("MainWindow", "Binarizaci??n"))
        self.label_5.setText(_translate("MainWindow", "Borde Laplaciano"))
        self.rdb_4v.setText(_translate("MainWindow", "4V"))
        self.rdb_8v.setText(_translate("MainWindow", "8V"))
        self.lbl_img_laplaciano.setText(_translate("MainWindow", "Suba una imagen"))
        self.label_6.setText(_translate("MainWindow", "Marchine Square"))
        self.lbl_img_marchine.setText(_translate("MainWindow", "Suba una imagen"))
        self.label_16.setText(_translate("MainWindow", "Frontera Exterior"))
        self.lbl_img_front_ex.setText(_translate("MainWindow", "Suba una imagen"))
        self.label_7.setText(_translate("MainWindow", "Frontera Interior"))
        self.lbl_img_front_int.setText(_translate("MainWindow", "Suba una imagen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bordes), _translate("MainWindow", "Detecci??n de Bordes"))
