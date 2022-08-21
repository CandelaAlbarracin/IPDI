from PyQt5 import QtWidgets
from PyQt5 import QtGui
from interfazLS import Ui_MainWindow
from conversorRGBIYQ import rgb_yiq,yiq_rgb
import matplotlib.image as img
import numpy as np
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_subir_img.clicked.connect(self.subir_img)
        self.ui.edt_luminancia.setValue(1.00)
        self.ui.edt_luminancia.valueChanged.connect(self.modificar_img)
        self.ui.edt_saturacion.valueChanged.connect(self.modificar_img)
        self.ui.edt_luminancia.setReadOnly(True)
        self.ui.edt_saturacion.setReadOnly(True)

    def subir_img(self):
        global archivo
        archivo=QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','C:\\',"Images (*.png *.bmp)") #abre el explorador de archivos
        if archivo[0]: #Controla que se haya seleccionado algun archivo
            self.ui.edt_luminancia.setReadOnly(False)
            self.ui.edt_saturacion.setReadOnly(False)
            temp=img.imread(archivo[0]) #Lee la imagen seleccionada
            h,w,c=temp.shape
            if  c>= 3:
                #Se muestra la imagen seleccionada en RGB
                rgb=temp[:,:,0:3]*255
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(im)
                self.ui.lbl_img_org.setPixmap(pix)
                self.ui.lbl_img_mod.setPixmap(pix)
                if c>3:
                    QtWidgets.QMessageBox.about(self,"Advertencia", "La imagen subida contiene canal alfa (Imagen RGBA). Se ha quitado este canal de la visualización de la imagen original (se muestra la imagen en RGB)")
            else:
                QtWidgets.QMessageBox.about(self,"Advertencia","La imagen subida no es RGB o RGBA. Intente cambiar la imagen.")
        else:
            self.ui.lbl_img_org.setText('Seleccione una imagen para ver una vista previa')
            self.ui.lbl_img_mod.setText('Seleccione una imagen para ver una vista previa')
            self.ui.edt_luminancia.setReadOnly(True)
            self.ui.edt_saturacion.setReadOnly(True)

    def modificar_img(self):
        lum=self.ui.edt_luminancia.value()
        sat=self.ui.edt_saturacion.value()
        image = img.imread(archivo[0]) #La matriz que representa a la imagen ya se encuentra en RGB normalizado [0;1]
        imagen=rgb_yiq(image[:,:,0:3]) #Realiza la conversión de la imagen de RGB a YIQ
        imagen[:,:,0]=lum*imagen[:,:,0] #Multiplica por un escalar la luminancia(Y)
        imagen[:,:,0]=np.minimum(imagen[:,:,0],1) #Si existen valores de Y>1 son colocados como Y=1
        imagen[:,:,0]=np.maximum(imagen[:,:,0],0) #Si existen valores de Y<0 son colocados como Y=0
        imagen[:,:,1:3]=sat*imagen[:,:,1:3] #Multiplica las componentes I y Q por un escalar
        imagen[:,:,1]=np.maximum(imagen[:,:,1],-0.5957) #Se controla que los valores de I no sean menores a -0.5957, si sucese de reemplaza por dicho valor
        imagen[:,:,1]=np.minimum(imagen[:,:,1],0.5957) #Se controla que los valores de I no sean mayores a 0.5957, si sucese de reemplaza por dicho valor
        imagen[:,:,2]=np.maximum(imagen[:,:,2],-0.5226) #Se controla que los valores de Q no sean menores a -0.5226, si sucese de reemplaza por dicho valor
        imagen[:,:,2]=np.minimum(imagen[:,:,2],0.5226) #Se controla que los valores de Q no sean mayores a 0.5226, si sucese de reemplaza por dicho valor
        img_mod=yiq_rgb(imagen)*255 #Se convierte a RGB (en bytes,por eso la multiplicación por 255) desde YIQ 
        img_mod=img_mod.round(0) 
        img_mod=img_mod.astype(np.uint8)
        h,w,_=img_mod.shape
        im = QtGui.QImage(img_mod, w, h, 3*w,QtGui.QImage.Format_RGB888) #Se muestra la imagen modificada en la interfaz
        pix = QtGui.QPixmap.fromImage(im)
        self.ui.lbl_img_mod.setPixmap(pix)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())