# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1439, 773)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.img_org = QLabel(self.centralwidget)
        self.img_org.setObjectName(u"img_org")
        self.img_org.setMinimumSize(QSize(430, 450))
        font = QFont()
        font.setPointSize(10)
        self.img_org.setFont(font)
        self.img_org.setScaledContents(False)
        self.img_org.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.img_org)

        self.check_gris = QCheckBox(self.centralwidget)
        self.check_gris.setObjectName(u"check_gris")

        self.verticalLayout.addWidget(self.check_gris)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_subir = QPushButton(self.centralwidget)
        self.btn_subir.setObjectName(u"btn_subir")
        self.btn_subir.setMinimumSize(QSize(100, 50))
        self.btn_subir.setFont(font)

        self.horizontalLayout.addWidget(self.btn_subir)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.btn_procesar = QPushButton(self.centralwidget)
        self.btn_procesar.setObjectName(u"btn_procesar")
        self.btn_procesar.setMinimumSize(QSize(100, 50))
        self.btn_procesar.setFont(font)

        self.horizontalLayout.addWidget(self.btn_procesar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(1, 2)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(11)
        self.tabWidget.setFont(font1)
        self.tab_bin = QWidget()
        self.tab_bin.setObjectName(u"tab_bin")
        self.verticalLayout_6 = QVBoxLayout(self.tab_bin)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_mediana = QLabel(self.tab_bin)
        self.lbl_mediana.setObjectName(u"lbl_mediana")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lbl_mediana.setFont(font2)
        self.lbl_mediana.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_mediana)

        self.lbl_img_mediana = QLabel(self.tab_bin)
        self.lbl_img_mediana.setObjectName(u"lbl_img_mediana")
        self.lbl_img_mediana.setMinimumSize(QSize(270, 280))
        self.lbl_img_mediana.setScaledContents(True)
        self.lbl_img_mediana.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_img_mediana)

        self.verticalLayout_3.setStretch(1, 2)

        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_11 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_kmeans = QLabel(self.tab_bin)
        self.lbl_kmeans.setObjectName(u"lbl_kmeans")
        self.lbl_kmeans.setFont(font2)
        self.lbl_kmeans.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_kmeans)

        self.lbl_img_kmeans = QLabel(self.tab_bin)
        self.lbl_img_kmeans.setObjectName(u"lbl_img_kmeans")
        self.lbl_img_kmeans.setMinimumSize(QSize(270, 280))
        self.lbl_img_kmeans.setScaledContents(True)
        self.lbl_img_kmeans.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_img_kmeans)

        self.verticalLayout_4.setStretch(1, 2)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(2, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_18 = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_18)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_otsu = QLabel(self.tab_bin)
        self.lbl_otsu.setObjectName(u"lbl_otsu")
        self.lbl_otsu.setFont(font2)
        self.lbl_otsu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_otsu)

        self.lbl_img_otsu = QLabel(self.tab_bin)
        self.lbl_img_otsu.setObjectName(u"lbl_img_otsu")
        self.lbl_img_otsu.setMinimumSize(QSize(270, 280))
        self.lbl_img_otsu.setScaledContents(True)
        self.lbl_img_otsu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_img_otsu)

        self.verticalLayout_5.setStretch(1, 2)

        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_19 = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_bin, "")
        self.tab_bordes = QWidget()
        self.tab_bordes.setObjectName(u"tab_bordes")
        self.verticalLayout_7 = QVBoxLayout(self.tab_bordes)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.tab_bordes)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.rdb_4v = QRadioButton(self.tab_bordes)
        self.rdb_4v.setObjectName(u"rdb_4v")

        self.horizontalLayout_3.addWidget(self.rdb_4v)

        self.rdb_8v = QRadioButton(self.tab_bordes)
        self.rdb_8v.setObjectName(u"rdb_8v")
        self.rdb_8v.setChecked(True)

        self.horizontalLayout_3.addWidget(self.rdb_8v)

        self.horizontalLayout_3.setStretch(0, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.lbl_img_laplaciano = QLabel(self.tab_bordes)
        self.lbl_img_laplaciano.setObjectName(u"lbl_img_laplaciano")
        self.lbl_img_laplaciano.setMinimumSize(QSize(270, 280))
        self.lbl_img_laplaciano.setScaledContents(True)
        self.lbl_img_laplaciano.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_img_laplaciano)

        self.verticalLayout_2.setStretch(1, 2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_12 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.tab_bordes)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.lbl_img_marchine = QLabel(self.tab_bordes)
        self.lbl_img_marchine.setObjectName(u"lbl_img_marchine")
        self.lbl_img_marchine.setMinimumSize(QSize(270, 280))
        self.lbl_img_marchine.setScaledContents(True)
        self.lbl_img_marchine.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lbl_img_marchine)

        self.verticalLayout_8.setStretch(1, 2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(2, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.tab_bordes)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_16)

        self.lbl_img_front_ex = QLabel(self.tab_bordes)
        self.lbl_img_front_ex.setObjectName(u"lbl_img_front_ex")
        self.lbl_img_front_ex.setMinimumSize(QSize(270, 280))
        self.lbl_img_front_ex.setScaledContents(True)
        self.lbl_img_front_ex.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lbl_img_front_ex)

        self.verticalLayout_10.setStretch(1, 2)

        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_20 = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.tab_bordes)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.lbl_img_front_int = QLabel(self.tab_bordes)
        self.lbl_img_front_int.setObjectName(u"lbl_img_front_int")
        self.lbl_img_front_int.setMinimumSize(QSize(270, 280))
        self.lbl_img_front_int.setScaledContents(True)
        self.lbl_img_front_int.setAlignment(Qt.AlignCenter)

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
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Binarizaci\u00f3n y Fronteras", None))
        self.img_org.setText(QCoreApplication.translate("MainWindow", u"Seleccione una imagen para previsualizarla", None))
        self.check_gris.setText(QCoreApplication.translate("MainWindow", u"Escala de Grises", None))
        self.btn_subir.setText(QCoreApplication.translate("MainWindow", u"Subir Imagen", None))
        self.btn_procesar.setText(QCoreApplication.translate("MainWindow", u"Procesar", None))
        self.lbl_mediana.setText(QCoreApplication.translate("MainWindow", u"50% - 50% (Umbral Mediana)", None))
        self.lbl_img_mediana.setText(QCoreApplication.translate("MainWindow", u"Suba una imagen", None))
        self.lbl_kmeans.setText(QCoreApplication.translate("MainWindow", u"K-Means", None))
        self.lbl_img_kmeans.setText(QCoreApplication.translate("MainWindow", u"Suba una imagen", None))
        self.lbl_otsu.setText(QCoreApplication.translate("MainWindow", u"Otsu", None))
        self.lbl_img_otsu.setText(QCoreApplication.translate("MainWindow", u"Suba una imagen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bin), QCoreApplication.translate("MainWindow", u"Binarizaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Borde Laplaciano", None))
        self.rdb_4v.setText(QCoreApplication.translate("MainWindow", u"4V", None))
        self.rdb_8v.setText(QCoreApplication.translate("MainWindow", u"8V", None))
        self.lbl_img_laplaciano.setText(QCoreApplication.translate("MainWindow", u"Suba una imagen", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Marchine Square", None))
        self.lbl_img_marchine.setText(QCoreApplication.translate("MainWindow", u"Suba una imagen", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Frontera Exterior", None))
        self.lbl_img_front_ex.setText(QCoreApplication.translate("MainWindow", u"Suba una imagen", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frontera Interior", None))
        self.lbl_img_front_int.setText(QCoreApplication.translate("MainWindow", u"Suba una imagen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bordes), QCoreApplication.translate("MainWindow", u"Detecci\u00f3n de Bordes", None))
    # retranslateUi

