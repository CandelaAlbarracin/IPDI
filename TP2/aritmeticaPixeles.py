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

def cuasi_suma_RGB_prom(img1,img2,norm=False):
    '''
    img1:matriz nxn
    img2:matriz nxn
    norm: indica si los valores de las matrices estan normalizados o no. Por defecto tiene el valor falso
    Esta función realiza la cuasi-suma en RGB promedio de dos imagenes
    '''
    img=np.ndarray(img1.shape)
    img[:,:,0]=(img1[:,:,0]+img2[:,:,0])/2
    img[:,:,1]=(img1[:,:,1]+img2[:,:,1])/2
    img[:,:,2]=(img1[:,:,2]+img2[:,:,2])/2
    if norm:
        return img
    else:
        return img.astype(np.uint8)

def cuasi_suma_YIQ(img1,img2):
    '''
    img1:matriz nxn
    img2:matriz nxn
    Esta función realiza la cuasi-suma en YIQ clampeada de dos imagenes
    '''
    img=np.ndarray(img1.shape)
    img[:,:,0]=img1[:,:,0]+img2[:,:,0]
    img[:,:,0]=np.minimum(img[:,:,0],1)
    img[:,:,1]=(img1[:,:,0]*img1[:,:,1]+img2[:,:,0]*img2[:,:,1])/(img1[:,:,0]+img2[:,:,0])
    img[:,:,2]=(img1[:,:,0]*img1[:,:,2]+img2[:,:,0]*img2[:,:,2])/(img1[:,:,0]+img2[:,:,0])
    return img

def cuasi_suma_YIQ_prom(img1,img2):
    '''
    img1:matriz nxn
    img2:matriz nxn
    Esta función realiza la cuasi-suma en YIQ promedio de dos imagenes
    '''
    img=np.ndarray(img1.shape)
    img[:,:,0]=(img1[:,:,0]+img2[:,:,0])/2
    img[:,:,1]=(img1[:,:,0]*img1[:,:,1]+img2[:,:,0]*img2[:,:,1])/(img1[:,:,0]+img2[:,:,0])
    img[:,:,2]=(img1[:,:,0]*img1[:,:,2]+img2[:,:,0]*img2[:,:,2])/(img1[:,:,0]+img2[:,:,0])
    return img
