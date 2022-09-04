import numpy as np
from conversorRGBIYQ import rgb_yiq,yiq_rgb

def raiz_cuadrada(img:np.ndarray):
    '''
    Recibe una imagen (matriz) en RGB normalizado y devuelve la matriz con Valores RGB normalizados, luego de aplicar el filtro raiz cuadrada a la lumninancia de la misma 
    '''
    yiq=rgb_yiq(img)
    yiq[:,:,0]=np.sqrt(yiq[:,:,0])
    rgb=yiq_rgb(yiq)
    return rgb

def cuadrado(img:np.ndarray):
    '''
    Recibe una imagen (matriz) en RGB normalizado y devuelve la matriz con Valores RGB normalizados, luego de aplicar el filtro cuadrado a la lumninancia de la misma 
    '''
    yiq=rgb_yiq(img)
    yiq[:,:,0]=np.square(yiq[:,:,0])
    rgb=yiq_rgb(yiq)
    return rgb

def raiz_cubica(img:np.ndarray):
    '''
    Recibe una imagen (matriz) en RGB normalizado y devuelve la matriz con Valores RGB normalizados, luego de aplicar el filtro raiz cubica a la lumninancia de la misma 
    '''
    yiq=rgb_yiq(img)
    yiq[:,:,0]=np.cbrt(yiq[:,:,0])
    rgb=yiq_rgb(yiq)
    return rgb

def cubo(img:np.ndarray):
    '''
    Recibe una imagen (matriz) en RGB normalizado y devuelve la matriz con Valores RGB normalizados, luego de aplicar el filtro cubo a la lumninancia de la misma 
    '''
    yiq=rgb_yiq(img)
    yiq[:,:,0]=np.power(yiq[:,:,0],3)
    rgb=yiq_rgb(yiq)
    return rgb

def lineal_trozos(img:np.ndarray,minimo:float,maximo:float):
    '''
    Recibe una imagen (matriz) en RGB normalizado y devuelve la matriz con Valores RGB normalizados, luego de aplicar el filtro lineal a trozos a la lumninancia de la misma 
    '''
    yiq=rgb_yiq(img)
    y=yiq[:,:,0]
    np.piecewise(y, [y<minimo,np.logical_and(y>=minimo,y<=maximo) ,y>maximo], [lambda y: 0, lambda y:(y-minimo)/(maximo-minimo) ,lambda y: 1])
    yiq[:,:,0]=y
    rgb=yiq_rgb(yiq)
    return rgb

