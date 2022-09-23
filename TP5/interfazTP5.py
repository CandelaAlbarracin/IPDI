from PyQt5 import QtWidgets
from PyQt5 import QtGui
from gui_principal import Ui_MainWindow
import matplotlib.image as mpimg
import numpy as np
import sys
from os import remove
from conversorRGBIYQ import rgb_yiq,yiq_rgb
import morfologia

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cbox_filtro.setEnabled(False)
        self.ui.btn_guardar.setEnabled(False)
        self.ui.btn_copiar.setEnabled(False)
        self.ui.btn_cargar.clicked.connect(self.cargar_img)
        self.ui.cbox_filtro.currentTextChanged.connect(self.aplicar_filtro)
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_copiar.clicked.connect(self.copiar)
    
    def cargar_img(self):
        global dir
        archivo=QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','',"Images (*.png *.bmp)") #abre el explorador de archivos
        dir=archivo[0]
        if archivo[0]:
            temp=mpimg.imread(archivo[0]) #Lee la imagen seleccionada
            try:
                h,w,c=temp.shape
            except:
                temp=np.dstack((temp,temp,temp))
                h,w,c=temp.shape
            if  c>= 3:
                #Se muestra la imagen seleccionada en RGB
                if temp.dtype==np.float32:
                    rgb=temp[:,:,0:3]*255 #Para el caso de imagenes .png se debe transformar los valores normalizados [0;1] a [0;255]
                else:
                    rgb=temp[:,:,0:3] #Para el caso de imagenes .bpm (la matriz contiene valores entre [0;255])
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(im)
                self.ui.lbl_img.setPixmap(pix)
                if c>3:
                    QtWidgets.QMessageBox.about(self,"Advertencia", "La imagen subida es posible que contenga canal alfa (Imagen RGBA). Se ha quitado este canal de la visualización de la imagen original (se muestra la imagen en RGB).")
            else:
                QtWidgets.QMessageBox.about(self,"Advertencia","La imagen subida no es RGB o RGBA. Intente cambiar la imagen.")
            self.ui.btn_guardar.setEnabled(False)
            self.ui.cbox_filtro.setEnabled(True)
            self.ui.btn_copiar.setEnabled(False)
            self.ui.lbl_img_filtro.setText("Seleccione un filtro para previsualizar la imagen")
            self.ui.cbox_filtro.setCurrentIndex(0)
        else:
            self.ui.lbl_img.setText('Seleccione una imagen para previsualizarla')
            self.ui.cbox_filtro.setEnabled(False)
            self.ui.btn_guardar.setEnabled(False)
            self.ui.btn_copiar.setEnabled(False)
            self.ui.lbl_img_filtro.setText("Seleccione un filtro para previsualizar la imagen")
            self.ui.cbox_filtro.setCurrentIndex(0)
    
    def aplicar_filtro(self):
        global img_mod
        opc=self.ui.cbox_filtro.currentText()
        if not dir:
            return
        img=mpimg.imread(dir)
        try:
            h,w,c=img.shape
            img=img[:,:,0:3]
            if img.dtype==np.uint8:
                img=np.divide(img,255)
        except:
            img=np.dstack((img,img,img))
            img=np.divide(img,255)

        yiq=rgb_yiq(img)
        y=yiq[:,:,0]

        if opc=='Erosión 3x3':
            y=morfologia.repetir_filas(y,np.ones((3,3)))
            img_filtro=morfologia.erosion(y)
        elif opc=="Dilatación 3x3":
            y=morfologia.repetir_filas(y,np.ones((3,3)))
            img_filtro=morfologia.dilatacion(y)
        elif opc=="Apertura 3x3":
            y=morfologia.repetir_filas(y,np.ones((3,3)))
            img_filtro=morfologia.apertura(morfologia.repetir_filas(y,np.ones((3,3))))
        elif opc=="Cierre 3x3":
            y=morfologia.repetir_filas(y,np.ones((3,3)))
            img_filtro=morfologia.cierre(morfologia.repetir_filas(y,np.ones((3,3))))
        elif opc=="Gradiente 3x3":
            y=morfologia.repetir_filas(y,np.ones((3,3)))
            img_filtro=morfologia.gradiente(y)
        elif opc=="Borde Exterior 3x3":
            img_filtro=morfologia.borde_exterior(y)
        elif opc=="Borde Interior 3x3":
            img_filtro=morfologia.borde_interior(y)
        elif opc=="Mediana 3x3":
            y=morfologia.repetir_filas(y,np.ones((3,3)))
            img_filtro=morfologia.mediana(y)

        try:
            yiq[:,:,0]=img_filtro
            img_mod=yiq_rgb(yiq)
            self.mostrar_resultado(img_mod)
        except:
            pass
    
    def mostrar_resultado(self,temp):
        h,w,_=temp.shape
        rgb=temp[:,:,0:3]*255
        rgb=np.minimum(rgb,255)
        rgb=np.maximum(rgb,0)
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        self.ui.lbl_img_filtro.setPixmap(pix)
        self.ui.btn_copiar.setEnabled(True)
        self.ui.btn_guardar.setEnabled(True)

    def guardar(self):
        if self.ui.lbl_img_filtro.pixmap():
            path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Guardar Imagen", "", "Imagen (*.png);;Imagen (*.bmp)") 
            if path != "":
                temp=img_mod
                h,w,_=temp.shape
                if np.max(temp)<=2:
                    rgb=temp[:,:,0:3]*255
                else:
                    rgb=temp[:,:,0:3]
                rgb=np.minimum(255,rgb)
                rgb=np.maximum(0,rgb)
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                im.save(path)

    def copiar(self):
        global dir
        dir="temp.png"
        if self.ui.lbl_img_filtro.pixmap():
            temp=img_mod
            h,w,_=temp.shape
            if np.max(temp)<=2:
                rgb=temp[:,:,0:3]*255
            else:
                rgb=temp[:,:,0:3]
            rgb=np.minimum(255,rgb)
            rgb=np.maximum(0,rgb)
            im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
            im.save(dir)
            temp=mpimg.imread(dir)
            if temp.dtype==np.float32:
                rgb=temp[:,:,0:3]*255
            else:
                rgb=temp[:,:,0:3]
            im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(im)
            self.ui.lbl_img.setPixmap(pix)
    
    def closeEvent(self, event):
        remove("temp.png")
        event.accept()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
