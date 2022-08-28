import aritmeticaPixeles 
from conversorRGBIYQ import rgb_yiq,yiq_rgb 
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from interfazAritmetica import Ui_MainWindow
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import sys

class ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super(ventana, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_salir.clicked.connect(self.salir)
        self.ui.btn_img_1.clicked.connect(self.subir_img_1)
        self.ui.btn_img_2.clicked.connect(self.subir_img_2)
        self.ui.cb_op.currentIndexChanged.connect(self.operar)
        self.ui.cb_formato.currentIndexChanged.connect(self.operar)

    def salir(self):
        self.close()

    def subir_img_1(self):
        global dir1
        archivo=QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','C:\\',"Images (*.png *.bmp)") #abre el explorador de archivos
        dir1=archivo[0]
        if archivo[0]:
            temp=mpimg.imread(archivo[0]) #Lee la imagen seleccionada
            h,w,c=temp.shape
            if  c>= 3:
                #Se muestra la imagen seleccionada en RGB
                rgb=temp[:,:,0:3]*255
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(im)
                self.ui.lbl_img_1.setPixmap(pix)
                if c>3:
                    QtWidgets.QMessageBox.about(self,"Advertencia", "La imagen subida contiene canal alfa (Imagen RGBA). Se ha quitado este canal de la visualización de la imagen original (se muestra la imagen en RGB)")
            else:
                QtWidgets.QMessageBox.about(self,"Advertencia","La imagen subida no es RGB o RGBA. Intente cambiar la imagen.")

    def subir_img_2(self):
        global dir2
        archivo=QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','C:\\',"Images (*.png *.bmp)") #abre el explorador de archivos
        dir2=archivo[0]
        if archivo[0]:
            temp=mpimg.imread(archivo[0]) #Lee la imagen seleccionada
            h,w,c=temp.shape
            if  c>= 3:
                #Se muestra la imagen seleccionada en RGB
                rgb=temp[:,:,0:3]*255
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(im)
                self.ui.lbl_img_2.setPixmap(pix)
                if c>3:
                    QtWidgets.QMessageBox.about(self,"Advertencia", "La imagen subida contiene canal alfa (Imagen RGBA). Se ha quitado este canal de la visualización de la imagen original (se muestra la imagen en RGB)")
            else:
                QtWidgets.QMessageBox.about(self,"Advertencia","La imagen subida no es RGB o RGBA. Intente cambiar la imagen.")

    def operar(self):
        op=self.ui.cb_op.currentText()
        form=self.ui.cb_formato.currentText()
        img1=mpimg.imread(dir1)[:,:,0:3]
        img2=mpimg.imread(dir2)[:,:,0:3]
        if(img1.shape[0:1]==img2.shape[0:1]):
            if op=="Cuasi-Suma":
                if form=="RGB clamping":
                    img=aritmeticaPixeles.cuasi_suma_RGB(img1,img2,True)
                    self.mostrar_resultado(img)
                elif form=="RGB promedio":
                    img=aritmeticaPixeles.cuasi_suma_RGB_prom(img1,img2,True)
                    self.mostrar_resultado(img)
                elif form=="YIQ clamping":
                    img=aritmeticaPixeles.cuasi_suma_YIQ(rgb_yiq(img1),rgb_yiq(img2))
                    self.mostrar_resultado(yiq_rgb(img))
                elif form=="YIQ promedio":
                    img=aritmeticaPixeles.cuasi_suma_YIQ_prom(rgb_yiq(img1),rgb_yiq(img2))
                    self.mostrar_resultado(yiq_rgb(img))
        else:
            QtWidgets.QMessageBox.about(self,"Advertencia","Las imagenes selecionadas no tienen el mismo tamaño. Busque otras imagenes")
    

    def mostrar_resultado(self,img):
        rgb=img*255
        rgb=np.minimum(rgb,255)
        h,w,_=rgb.shape
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        self.ui.lbl_img_out.setPixmap(pix)

app = QtWidgets.QApplication([])
application = ventana()
application.show()
sys.exit(app.exec())