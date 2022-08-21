<h1> Trabajo Práctico N°1 </h1>
<p align="left">
   <img src="https://img.shields.io/badge/Estado-Terminado-green">
   </p>
🎯 <b>Objetivo:</b> Este trabajo consiste en realizar una GUI en donde se permita subir una imagen para realizar una manipulación independiente de la luminancia y saturación de la misma.
<br></br>

🛠️ **¿Como funciona?**

<ul>
  <li>conversorRGBYIQ.py: Contiene la definición de dos funciones</li>
  <ul>
    <li>rgb_yiq: Realiza la conversión del espacio RGB normalizado a YIQ</li>
    <li>yiq_rgb: Realiza la conversión del espacio YIQ a RGB normalizado [0; 1]</li> 
  </ul>
  <li>interfazLS.py: contiene la definición de la interfaz gráfica en Python.</li>
  <li>interfazLS.ui: es el archivo que contiene la definición de la interfaz gráfica en XML(diseñado en QTDesigner).</li>
  <li>interfazTP1.py: archivo a ejecutar. Aqui se encuentra la lógica del programa y la ejecución de la GUI.</li>
  <li>lena.png, pub.png, stinkbug.png, tiger.png: Imágenes .png de prueba</li>
</ul>

📦 **Paquetes Utilizados**
   -Numpy
   -Matplotlib
   -PyQt5
   -PySide 2 y 6
