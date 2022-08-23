import numpy as np

def cuasi_suma_RGB(img1,img2):
    img=np.ndarray(img1.shape)
    img[:,:,0]=img1[:,:,0]+img2[:,:,0]
    img[:,:,1]=img1[:,:,1]+img2[:,:,1]
    img[:,:,2]=img1[:,:,2]+img2[:,:,2]
    img=np.minimum(img,255)
    return img.astype(np.uint8)

def cuasi_suma_RGB_norm(img1,img2):
    img=np.ndarray(img1.shape)
    img[:,:,0]=img1[:,:,0]+img2[:,:,0]
    img[:,:,1]=img1[:,:,1]+img2[:,:,1]
    img[:,:,2]=img1[:,:,2]+img2[:,:,2]
    img=np.minimum(img,1)
    return img



