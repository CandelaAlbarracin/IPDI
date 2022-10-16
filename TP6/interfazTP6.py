from PyQt5 import QtWidgets
from PyQt5 import QtGui
from gui_principal import Ui_MainWindow
import matplotlib.image as mpimg
import numpy as np
import sys,os
import utilidades
from skimage import color

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_procesar.setEnabled(False)
        self.ui.check_gris.setCheckable(False)
        self.ui.btn_subir.clicked.connect(self.cargar_img)
        self.ui.btn_procesar.clicked.connect(self.procesar)
        self.ui.rdb_8v.toggled.connect(self.laplaciano)
        self.ui.check_gris.toggled.connect(self.escala_gris)

    def escala_gris(self):
        global dir
        dirnew="temp.png"
        if self.ui.check_gris.isChecked():
            img=mpimg.imread(dir)
            if img.ndim>2:
                img=img[:,:,0:3]
                gris=color.rgb2gray(img)
                if self.ui.img_org.pixmap():
                    temp=np.dstack((gris,gris,gris))
                h,w,_=temp.shape
                if np.max(temp)<=2:
                    rgb=temp*255
                else:
                    rgb=temp
                rgb=np.minimum(255,rgb)
                rgb=np.maximum(0,rgb)
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                im.save(dirnew)
                temp=mpimg.imread(dirnew)
                if temp.dtype==np.float32:
                    rgb=temp[:,:,0:3]*255
                else:
                    rgb=temp[:,:,0:3]
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(im)
                self.ui.img_org.setPixmap(pix)
                dir=dirnew
            else:
                QtWidgets.QMessageBox.information(self,"Información","La imagen subida ya está en escala de grises")
        else:
            dir=archivo[0]
            temp=mpimg.imread(dir) #Lee la imagen seleccionada
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
                self.ui.img_org.setPixmap(pix)

    def cargar_img(self):
        global dir
        global archivo
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
                self.ui.img_org.setPixmap(pix)
                if c>3:
                    QtWidgets.QMessageBox.warning(self,"Advertencia", "La imagen subida es posible que contenga canal alfa (Imagen RGBA). Se ha quitado este canal de la visualización de la imagen original (se muestra la imagen en RGB).")
            else:
                QtWidgets.QMessageBox.warning(self,"Advertencia","La imagen subida no es RGB o RGBA. Intente cambiar la imagen.")
            self.ui.btn_procesar.setEnabled(True)
            self.ui.check_gris.setCheckable(True)
        else:
            self.ui.img_org.setText('Seleccione una imagen para previsualizarla')
            self.ui.btn_procesar.setEnabled(False)
            self.ui.check_gris.setCheckable(False)
        self.ui.check_gris.setChecked(False)
    
    def procesar(self):
        img=mpimg.imread(dir)
        if img.ndim>2:
            img=img[:,:,0:3]
        umbral_med=utilidades.seg_mediana(img)
        temp=np.dstack((umbral_med,umbral_med,umbral_med))
        self.mostrar_resultado(temp,self.ui.lbl_img_mediana)
        unos=np.count_nonzero(umbral_med)
        ceros=umbral_med.size-unos
        self.ui.lbl_mediana.setText("{:.2f}%px Blancos - {:.2f}%px Negros".format(unos/umbral_med.size*100,ceros/umbral_med.size*100))

        umbral_kmeans=utilidades.seg_kmeans(img,2)
        temp=np.dstack((umbral_kmeans,umbral_kmeans,umbral_kmeans))
        self.mostrar_resultado(temp,self.ui.lbl_img_kmeans)

        umbral_otsu=utilidades.seg_otsu(img)
        temp=np.dstack((umbral_otsu,umbral_otsu,umbral_otsu))
        self.mostrar_resultado(temp,self.ui.lbl_img_otsu)
        
        self.laplaciano(img)
        self.borde_ext(img)
        self.borde_int(img)

        ms=utilidades.seg_marchine_square(img)
        self.mostrar_resultado(ms,self.ui.lbl_img_marchine)
        

    def borde_ext(self,img):
        if img.ndim>2:
            if img.dtype!=np.float32:
                img=img/255
            yiq=utilidades.rgb_yiq(img)
            y=yiq[:,:,0]
        else:
            y=img
        borde_ext=utilidades.borde_exterior(y)
        if img.ndim>2:
            yiq[:,:,0]=borde_ext
            img_mod=utilidades.yiq_rgb(yiq)
        else:
            img_mod=np.dstack((borde_ext,borde_ext,borde_ext))
        self.mostrar_resultado(img_mod,self.ui.lbl_img_front_ex)
    
    def borde_int(self,img):
        if img.ndim>2:
            if img.dtype!=np.float32:
                img=img/255
            yiq=utilidades.rgb_yiq(img)
            y=yiq[:,:,0]
        else:
            y=img
        borde_int=utilidades.borde_interior(y)
        if img.ndim>2:
            yiq[:,:,0]=borde_int
            img_mod=utilidades.yiq_rgb(yiq)
        else:
            img_mod=np.dstack((borde_int,borde_int,borde_int))
        self.mostrar_resultado(img_mod,self.ui.lbl_img_front_int)

    def laplaciano(self,img):
        img=mpimg.imread(dir)
        if img.ndim>2:
            img=img[:,:,0:3]
            if img.dtype!=np.float32:
                img=img/255
            yiq2=utilidades.rgb_yiq(img)
            y2=yiq2[:,:,0]
        else:
            y2=img
        if self.ui.rdb_8v.isChecked():
            res=utilidades.convolucionar(utilidades.repetir_filas(y2,np.ones((3,3))),utilidades.kernel_laplaciano(8))
        else:
            res=utilidades.convolucionar(utilidades.repetir_filas(y2,np.ones((3,3))),utilidades.kernel_laplaciano(4))
        if img.ndim>2:
            res=np.minimum(res,1)
            res=np.maximum(res,0)
            yiq2[:,:,0]=res
            lap=utilidades.yiq_rgb(yiq2)
        else:
            lap=np.dstack((res,res,res))

        self.mostrar_resultado(lap,self.ui.lbl_img_laplaciano)

    def mostrar_resultado(self,temp,comp_img):
        h,w,_=temp.shape
        rgb=temp[:,:,0:3]*255
        rgb=np.minimum(rgb,255)
        rgb=np.maximum(rgb,0)
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        comp_img.setPixmap(pix)
    
    def closeEvent(self, event):
        try:
            os.remove("temp.png")
            os.remove("out_ms.png")
        except:
            pass
        event.accept()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())