import numpy as np

def cuasi_suma_RGB(img1,img2,norm=False):
    '''
    img1:matriz nxn
    img2:matriz nxn
    norm: indica si los valores de las matrices estan normalizados o no. Por defecto tiene el valor falso
    Esta función realiza la cuasi-suma en RGB clampeada de dos imagenes
    '''
    img=np.ndarray(img1.shape)
    img[:,:,0]=img1[:,:,0]+img2[:,:,0]
    img[:,:,1]=img1[:,:,1]+img2[:,:,1]
    img[:,:,2]=img1[:,:,2]+img2[:,:,2]
    if norm:
        img=np.minimum(img,1)
        return img
    else:
        img=np.minimum(img,255)
        return img.astype(np.uint8)
