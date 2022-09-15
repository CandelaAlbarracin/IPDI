<h1> Trabajo Práctico N°4</h1>
<p align="left">
   <img src="https://img.shields.io/badge/Estado-Terminado-green">
   </p>
🎯 <b>Objetivo:</b> Este trabajo consiste en realizar una GUI en donde se permita subir una imagen para poder visualizar el resultado luego de aplicar filtros pasabajos, pasaaltos, direccionales y pasabanda mediante la aplicación de la convolución.
<br></br>

🛠️ **¿Como funciona?**

<ul>
  <li>conversorRGBYIQ.py: Contiene la definición de dos funciones</li>
  <ul>
    <li>rgb_yiq: Realiza la conversión del espacio RGB normalizado a YIQ</li>
    <li>yiq_rgb: Realiza la conversión del espacio YIQ a RGB normalizado [0; 1]</li> 
  </ul>
  <li>interfazTP4.py: contiene la definición de la interfaz gráfica en Python.</li>
  <li>interfazTP4.ui: es el archivo que contiene la definición de la interfaz gráfica de la pantalla principal en XML(diseñado en QTDesigner).</li>
  <li>gui_principal.py: archivo a ejecutar. Aqui se encuentra la lógica del programa y la ejecución de la GUI.</li>
  <li>kenerls.py: Contiene la definición de las funciones que permiten generar diferentes kernels en base a un tamaño n pasado como parámetro en los casos de 
  kernel promedio, bartlett,gaussiano. En base a n vecinos para kernels laplacianos y en base a la dirección (N, NE, E, SE, S, SO, O, NO) para kernels sobels. También se define la función de convolución</li>
</ul>

📦 **Paquetes Utilizados**<br>
   -Numpy<br>
   -Matplotlib<br>
   -PyQt5<br>
   -math<br>
   -PySide 2 y 6<br>
