<h1> Trabajo Práctico N°2 </h1>
<p align="left">
   <img src="https://img.shields.io/badge/Estado-Terminado-green">
   </p>
🎯 <b>Objetivo:</b> Este trabajo consiste en realizar una GUI en donde se permita subir dos imagenes para realizar operaciones entre pixeles: suma (clampeada-promedio), resta(clampeada-promedio), producto, cociente, if-ligther, if-darker en los espacios de colores RGB e YIQ.
<br></br>

🛠️ **¿Como funciona?**

<ul>
  <li>aritmeticaPixeles.py: Contiene la definición de las funciones que permite operar con los pixeles de dos imágenes en RGB e YIQ</li>
  <li>conversorRGBYIQ.py: Contiene la definición de dos funciones</li>
  <ul>
    <li>rgb_yiq: Realiza la conversión del espacio RGB normalizado a YIQ</li>
    <li>yiq_rgb: Realiza la conversión del espacio YIQ a RGB normalizado [0; 1]</li> 
  </ul>
  <li>interfazAritmetica.py: contiene la definición de la interfaz gráfica en Python.</li>
  <li>interfazAritmetica.ui: es el archivo que contiene la definición de la interfaz gráfica en XML(diseñado en QTDesigner).</li>
  <li>interfazTP2.py: archivo a ejecutar. Aqui se encuentra la lógica del programa y la ejecución de la GUI.</li>
</ul>

📦 **Paquetes Utilizados**<br>
   -Numpy<br>
   -Matplotlib<br>
   -PyQt5<br>
   -PySide 2 y 6<br>
