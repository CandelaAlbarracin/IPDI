from PyQt5 import QtWidgets
from PyQt5 import QtGui
from interfazTP4 import Ui_MainWindow
import matplotlib.image as mpimg
import numpy as np
import sys
from conversorRGBIYQ import rgb_yiq,yiq_rgb
import kernels

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.edt_frec.hide()
        self.ui.label_6.hide()
        self.ui.label_7.hide()
        self.ui.cbox_direccion.hide()
        self.ui.cbox_filtro.setEnabled(False)
        self.ui.btn_guardar.setEnabled(False)

        self.ui.btn_cargar.clicked.connect(self.cargar_img)
        self.ui.cbox_filtro.currentTextChanged.connect(self.aplicar_filtro)
        self.ui.cbox_direccion.currentTextChanged.connect(self.aplicar_filtro)
        self.ui.edt_frec.valueChanged.connect(self.aplicar_filtro)
        self.ui.btn_guardar.clicked.connect(self.guardar)
    
    def cargar_img(self):
        global dir
        archivo=QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','',"Images (*.png *.bmp)") #abre el explorador de archivos
        dir=archivo[0]
        if archivo[0]:
            temp=mpimg.imread(archivo[0]) #Lee la imagen seleccionada
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
                self.ui.lbl_img.setPixmap(pix)
                if c>3:
                    QtWidgets.QMessageBox.about(self,"Advertencia", "La imagen subida es posible que contenga canal alfa (Imagen RGBA). Se ha quitado este canal de la visualización de la imagen original (se muestra la imagen en RGB).")
            else:
                QtWidgets.QMessageBox.about(self,"Advertencia","La imagen subida no es RGB o RGBA. Intente cambiar la imagen.")
            self.ui.btn_guardar.setEnabled(False)
            self.ui.cbox_filtro.setEnabled(True)
        else:
            self.ui.lbl_img.setText('Seleccione una imagen para previsualizarla')
            self.ui.cbox_filtro.setEnabled(False)
            self.ui.btn_guardar.setEnabled(False)

    def aplicar_filtro(self):
        global img_mod
        img=mpimg.imread(dir)
        #Se genera el kernel según la elección del usuario
        opc=self.ui.cbox_filtro.currentText()
        if opc=="Pasabajo Plano 3x3":
            kernel=kernels.kernel_promedio(3)
        elif opc=="Pasabajo Plano 5x5":
            kernel=kernels.kernel_promedio(5)
        elif opc=="Pasabajo Plano 7x7":
            kernel=kernels.kernel_promedio(7)
        elif opc=="Pasabajo Bartlett 3x3":
            kernel=kernels.kernel_bartlett(3)
        elif opc=="Pasabajo Bartlett 5x5":
            kernel=kernels.kernel_bartlett(5)
        elif opc=="Pasabajo Bartlett 7x7":
            kernel=kernels.kernel_bartlett(7)
        elif opc=="Pasabajo Gaussiano 5x5":
            kernel=kernels.kernel_gaussiano(5)
        elif opc=="Pasabajo Gaussiano 7x7":
            kernel=kernels.kernel_gaussiano(7)
        elif opc=="Pasaalto Laplaciano v4" or opc=="Pasabanda Laplaciano v4":
            kernel=kernels.kernel_laplaciano(4)
        elif opc=="Pasaalto Laplaciano v8"or opc=="Pasabanda Laplaciano v8":
            kernel=kernels.kernel_laplaciano(8)
        elif opc=="Gradiente Sobel 3x3":
            direccion=self.ui.cbox_direccion.currentText()
            kernel=kernels.kernel_direccional(direccion)
        #Se convierte la imagen de RGB a YIQ
        if img.dtype!=np.float32:
            yiq=rgb_yiq(np.divide(img[:,:,0:3],255))
        else:
            yiq=rgb_yiq(img[:,:,0:3])
        #Se repiten las filas y columnas tanto iniciales como finales 
        n=kernel.shape[0]
        y=yiq[:,:,0]
        for _ in range(1,n//2+1):
            y=np.row_stack((y[0,:],y))
            y=np.row_stack((y,y[y.shape[0]-1,:])) 
            y=np.column_stack((y[:,0],y))
            y=np.column_stack((y,y[:,y.shape[1]-1])) 
        res=kernels.convolucionar(y,kernel) #Se realiza la convolución
        res=np.minimum(res,1)
        res=np.maximum(res,0)
        #Se muestran u ocultan los componentes de frecuencia de corte y direccion según corresponda
        if "Pasabanda" in opc:
            self.ui.edt_frec.show()
            self.ui.label_6.show()
            frec=self.ui.edt_frec.value()
            yiq[:,:,0]=yiq[:,:,0]+frec*res
            yiq[:,:,0]=np.minimum(yiq[:,:,0],1)
            yiq[:,:,0]=np.maximum(yiq[:,:,0],0)
        else:
            self.ui.edt_frec.hide()
            self.ui.label_6.hide()
            if "Sobel" in opc:
                self.ui.label_7.show()
                self.ui.cbox_direccion.show()
            else:
                self.ui.label_7.hide()
                self.ui.cbox_direccion.hide()
            yiq[:,:,0]=res
        #Se muestra la imagen en la interfaz gráfica
        img_mod=yiq_rgb(yiq)
        temp=img_mod
        h,w,_=temp.shape
        rgb=temp[:,:,0:3]*255
        rgb=np.minimum(rgb,255)
        rgb=np.maximum(rgb,0)
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        self.ui.lbl_img_mod.setPixmap(pix)
        self.ui.btn_guardar.setEnabled(True)
    
    def guardar(self):
        if self.ui.lbl_img_mod.pixmap():
            path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Guardar Imagen", "", "Imagen (*.png);;Imagen (*.bmp)") 
            if path != "":
                temp=img_mod
                h,w,_=temp.shape
                rgb=temp[:,:,0:3]*255
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                im.save(path)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())