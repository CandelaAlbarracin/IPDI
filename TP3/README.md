<h1> Trabajo Práctico N°3</h1>
<p align="left">
   <img src="https://img.shields.io/badge/Estado-Terminado-green">
   </p>
🎯 <b>Objetivo:</b> Este trabajo consiste en realizar una GUI en donde se permita subir una imagen para poder visualizar su histograma y poder aplicarle diversos filtros: raíz cuadrada, raíz cúbica, cuadrado, cubo, lineal a trozos.
<br></br>

🛠️ **¿Como funciona?**

<ul>
  <li>conversorRGBYIQ.py: Contiene la definición de dos funciones</li>
  <ul>
    <li>rgb_yiq: Realiza la conversión del espacio RGB normalizado a YIQ</li>
    <li>yiq_rgb: Realiza la conversión del espacio YIQ a RGB normalizado [0; 1]</li> 
  </ul>
  <li>gui_filtro.py: contiene la definición de la interfaz gráfica de la pantalla de filtros en Python.</li>
  <li>gui_filtro.ui: es el archivo que contiene la definición de la interfaz gráfica de la pantalla de filtros en XML(diseñado en QTDesigner).</li>
  <li>gui_histograma.py: contiene la definición de la interfaz gráfica de la pantalla del histograma en Python.</li>
  <li>gui_histograma.ui: es el archivo que contiene la definición de la interfaz gráfica de la pantalla del histograma en XML(diseñado en QTDesigner).</li>
  <li>gui_principal.py: contiene la definición de la interfaz gráfica de la pantalla principal en Python.</li>
  <li>gui_principal.ui: es el archivo que contiene la definición de la interfaz gráfica de la pantalla principal en XML(diseñado en QTDesigner).</li>
  <li>interfazTP2.py: archivo a ejecutar. Aqui se encuentra la lógica del programa y la ejecución de la GUI.</li>
  <li>operacionesLuminanacia.py: Contiene la definición de las funciones que permite aplicar filtros a la luminancia de las imágenes</li>
</ul>

📦 **Paquetes Utilizados**<br>
   -Numpy<br>
   -Matplotlib<br>
   -PyQt5<br>
   -PySide 2 y 6<br>
