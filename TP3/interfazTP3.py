from PyQt5 import QtWidgets,QtCore
from PyQt5 import QtGui
from gui_principal import Ui_MainWindow
from gui_histograma import Ui_Histograma
from gui_filtro import Ui_Filtro
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from conversorRGBIYQ import rgb_yiq, yiq_rgb
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import operacionesLuminancia
import sys

class ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super(ventana, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_hist_org.clicked.connect(self.abrir_ventana)
        self.ui.btn_subir.clicked.connect(self.subir_img)
        self.ui.btn_filtro.clicked.connect(self.abrir_filtro)
        self.ui.btn_hist_filtro.clicked.connect(self.abrir_hist)
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_hist_org.setEnabled(False)
        self.ui.btn_filtro.setEnabled(False)
        self.ui.btn_hist_filtro.setEnabled(False)
        self.ui.btn_guardar.setEnabled(False)
        global pixmap_filtro
        global lbl_titulo
        global lbl_ajustes
        global histo_filtro
        global guardar
        histo_filtro=self.ui.btn_hist_filtro
        guardar=self.ui.btn_guardar
        lbl_ajustes=self.ui.lbl_ajustes
        lbl_titulo=self.ui.label_4
        pixmap_filtro=self.ui.lbl_img_filtro
        self.ui.btn_salir.clicked.connect(self.close)

    def guardar(self):
        if self.ui.lbl_img_filtro.pixmap():
            path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Guardar Imagen", "", "Images (*.png *.bmp)") 
            if path != "":
                temp=img1
                h,w,_=temp.shape
                rgb=temp[:,:,0:3]*255
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                im.save(path)

    def abrir_hist(self):
        img=img1
        yiq=rgb_yiq(img)
        histo=Histograma(yiq[:,:,0],self)
        histo.show()

    def subir_img(self):
        global dir
        archivo=QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','',"Images (*.png *.bmp)") #abre el explorador de archivos
        dir=archivo[0]
        if archivo[0]:
            temp=mpimg.imread(archivo[0]) #Lee la imagen seleccionada
            h,w,c=temp.shape
            if  c>= 3:
                #Se muestra la imagen seleccionada en RGB
                if temp.dtype==np.float32:
                    rgb=temp[:,:,0:3]*255
                else:
                    rgb=temp[:,:,0:3]
                im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(im)
                self.ui.lbl_img_org.setPixmap(pix)
                self.ui.lbl_img_filtro.setPixmap(pix)
                if c>3:
                    QtWidgets.QMessageBox.about(self,"Advertencia", "La imagen subida contiene canal alfa (Imagen RGBA). Se ha quitado este canal de la visualización de la imagen original (se muestra la imagen en RGB)")
            else:
                QtWidgets.QMessageBox.about(self,"Advertencia","La imagen subida no es RGB o RGBA. Intente cambiar la imagen.")
            self.ui.btn_hist_org.setEnabled(True)
            self.ui.btn_filtro.setEnabled(True)
            self.ui.btn_hist_filtro.setEnabled(False)
            self.ui.btn_guardar.setEnabled(False)
        else:
            self.ui.lbl_img_org.setText('Seleccione una imagen para previsualizarla')
            self.ui.btn_hist_org.setEnabled(False)
            self.ui.btn_filtro.setEnabled(False)
            self.ui.btn_hist_filtro.setEnabled(False)
            self.ui.btn_guardar.setEnabled(False)

    def abrir_filtro(self):
        filtro=Filtro(self)
        filtro.show()

    def abrir_ventana(self):
        img=mpimg.imread(dir)[:,:,0:3]
        if img.dtype!=np.float32:
            img=np.divide(img,255)
        yiq=rgb_yiq(img)
        histo=Histograma(yiq[:,:,0],self)
        histo.show()

class Filtro(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(Filtro, self).__init__(parent)
        self.ui = Ui_Filtro()
        self.ui.setupUi(self)
        self.ui.rdb_raiz_cuadrada.setChecked(True)
        self.x=np.linspace(0,1,num=100)
        self.grafica =Canvas_Filtro(self.x,np.sqrt(self.x),self)
        self.ui.grafico.addWidget(self.grafica)
        self.ui.rdb_cuadrado.toggled.connect(self.modificar)
        self.ui.rdb_cubo.toggled.connect(self.modificar)
        self.ui.rdb_lineal.toggled.connect(self.modificar)
        self.ui.rdb_raiz_cuadrada.toggled.connect(self.modificar)
        self.ui.rdb_raiz_cubica.toggled.connect(self.modificar)
        self.ui.spin_sv_max.valueChanged.connect(self.modificar)
        self.ui.spin_sh_min.valueChanged.connect(self.modificar)
        self.ui.spin_sh_max.valueChanged.connect(self.modificar)
        self.ui.sv_max.valueChanged.connect(self.sinc)
        self.ui.sh_der.valueChanged.connect(self.sinc)
        self.ui.sh_izq.valueChanged.connect(self.sinc)
        self.ui.btn_aplicar.clicked.connect(self.aplicar)

    def aplicar(self):
        global img1
        img1=mpimg.imread(dir)[:,:,0:3]
        if dir[-3:]=="bmp":
            img1=np.divide(img1,255)

        if self.ui.rdb_cuadrado.isChecked():
            img1=operacionesLuminancia.cuadrado(img1)
            lbl_titulo.setText("Imagen con Filtro Cuadrado")
            lbl_ajustes.setText("Coef: "+self.ui.spin_sv_max.text())
        elif self.ui.rdb_cubo.isChecked():
            img1=operacionesLuminancia.cubo(img1)
            lbl_titulo.setText("Imagen con Filtro Cubo")
            lbl_ajustes.setText("Coef: "+self.ui.spin_sv_max.text())
        elif self.ui.rdb_raiz_cuadrada.isChecked():
            img1=operacionesLuminancia.raiz_cuadrada(img1)
            lbl_titulo.setText("Imagen con Filtro Raíz Cuadrada")
            lbl_ajustes.setText("Coef: "+self.ui.spin_sv_max.text())
        elif self.ui.rdb_raiz_cubica.isChecked():
            img1=operacionesLuminancia.raiz_cubica(img1)
            lbl_titulo.setText("Imagen con Filtro Raíz Cúbica")
            lbl_ajustes.setText("Coef: "+self.ui.spin_sv_max.text())
        elif self.ui.rdb_lineal.isChecked():
            img1=operacionesLuminancia.lineal_trozos(img1,self.ui.spin_sh_min.value(),self.ui.spin_sh_max.value())
            lbl_titulo.setText("Imagen con Filtro Lineal a Trozos")
            lbl_ajustes.setText("Coef: "+self.ui.spin_sv_max.text()+"|Min: "+self.ui.spin_sh_min.text()+"|Max: "+self.ui.spin_sh_max.text())
        
        img1=np.maximum(img1,0)
        img1=np.minimum(img1,1)
        limy=float(self.ui.spin_sv_max.value())
        img1=np.multiply(img1,limy)
        temp=img1
        h,w,_=temp.shape
        rgb=temp[:,:,0:3]*255
        rgb=np.minimum(rgb,255)
        rgb=np.maximum(rgb,0)
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3*w,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        pixmap_filtro.setPixmap(pix)
        histo_filtro.setEnabled(True)
        guardar.setEnabled(True)
        self.close()

    def actualizar(self):
        limy=10*float(self.ui.spin_sv_max.value())
        #limsupx=10*float(self.ui.spin_sh_max.value())
        liminfx=10*float(self.ui.spin_sh_min.value())
        self.ui.sv_max.setSliderPosition(int(limy))
        self.ui.sh_izq.setSliderPosition(int(liminfx))
        #self.ui.sh_der.setSliderPosition(int(limsupx))

    def sinc(self):
        limy=0.1*float(self.ui.sv_max.value())
        limsupx=0.1*(10-float(self.ui.sh_der.value()))
        liminfx=0.1*float(self.ui.sh_izq.value())
        self.ui.spin_sv_max.setValue(limy)
        self.ui.spin_sh_min.setValue(liminfx)
        self.ui.spin_sh_max.setValue(limsupx)
    
    def modificar(self):
        self.actualizar()
        limy=float((self.ui.spin_sv_max.text()).replace(',', '.'))
        liminfx=float((self.ui.spin_sh_min.text()).replace(',', '.'))
        limsupx=float((self.ui.spin_sh_max.text()).replace(',', '.'))
        if self.ui.rdb_cuadrado.isChecked():
            self.grafica.cambiary(limy*np.square(self.x))
        elif self.ui.rdb_cubo.isChecked():
            self.grafica.cambiary(limy*np.power(self.x,3))
        elif self.ui.rdb_raiz_cuadrada.isChecked():
            self.grafica.cambiary(limy*np.sqrt(self.x))
        elif self.ui.rdb_raiz_cubica.isChecked():
            self.grafica.cambiary(limy*np.cbrt(self.x))
        elif self.ui.rdb_lineal.isChecked():
            y=np.copy(self.x)
            y = np.piecewise(y, [y<liminfx,np.logical_and(y>=liminfx,y<=limsupx) ,y>limsupx], [lambda y: 0, lambda y:(y-liminfx)/(limsupx-liminfx) ,lambda y: 1])
            self.grafica.cambiary(limy*y)

class Canvas_Filtro(FigureCanvas):
    def __init__(self,x,y,parent=None):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(15, 15), facecolor='white')
        super().__init__(self.fig)
        self.x=x
        self.y=y
        self.grafica_datos()

    def cambiary(self,y):
        self.y=y

    def grafica_datos(self):
        self.ax.clear()
        self.ax.plot(self.x,self.y)
        self.ax.set_xlabel("Luminancia de Entrada")
        self.ax.set_ylabel("Luminancia de Salida")
        self.ax.set_ylim(0,1)
        self.ax.set_xlim(0,1)
        self.ax.set_yticks(np.arange(0,1.1,0.1))
        self.ax.set_xticks(np.linspace(0.0,1.0,num=11))
        self.ax.grid(True,axis='y')
        self.draw()
        QtCore.QTimer.singleShot(800, self.grafica_datos)

class Histograma(QtWidgets.QMainWindow):
    def __init__(self,datos,parent=None):
        super(Histograma, self).__init__(parent)
        self.ui = Ui_Histograma()
        self.ui.setupUi(self)
        self.grafica = Canvas_grafica(datos)
        self.ui.grafico_histograma.addWidget(self.grafica)
        self.ui.rdb_10.setChecked(True)
        self.ui.rdb_10.toggled.connect(self.modificar)
        self.ui.rdb_20.toggled.connect(self.modificar)
        self.ui.rdb_50.toggled.connect(self.modificar)
        self.ui.rdb_personalizado.toggled.connect(self.modificar)
        self.ui.edt_personalizado.valueChanged.connect(self.modificar)

    def modificar(self):
        if self.ui.rdb_10.isChecked():
            self.grafica.cambiar(10)
        elif self.ui.rdb_20.isChecked():
            self.grafica.cambiar(20)
        elif self.ui.rdb_50.isChecked():
            self.grafica.cambiar(50)
        elif self.ui.rdb_personalizado.isChecked():
            self.grafica.cambiar(int(self.ui.edt_personalizado.text()))

class Canvas_grafica(FigureCanvas):
    def __init__(self,datos,parent=None):     #Aqui pasar ajustes de histograma
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(15, 15), facecolor='white')
        super().__init__(self.fig)
        self.barras=10
        self.data=datos
        self.grafica_datos()

    def cambiar(self,b):
        self.barras=b

    def grafica_datos(self):
        self.ax.clear()
        res=np.histogram(self.data,self.barras,(0,1))
        h=res[0]
        x=res[1]
        self.ax.bar(x[:len(x)-1],h/sum(h),bottom=0,width=1/self.barras,align='edge',linewidth=0.5, edgecolor="black")
        self.ax.set_xlabel("Luminancia")
        self.ax.set_ylabel("Frecuencia Relativa")
        self.ax.set_xlim(0,1)
        self.ax.set_yticks(np.arange(0,1.1,0.1))
        self.ax.set_xticks(np.linspace(0.0,1.0,num=11))
        self.ax.grid(True,axis='y')
        self.draw()
        QtCore.QTimer.singleShot(800, self.grafica_datos)

app = QtWidgets.QApplication([])
application = ventana()
application.show()
sys.exit(app.exec())