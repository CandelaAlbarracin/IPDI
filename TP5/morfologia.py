import numpy as np

def repetir_filas(img,kernel):
    n=kernel.shape[0]
    for _ in range(1,n//2+1):
        img=np.row_stack((img[0,:],img))
        img=np.row_stack((img,img[img.shape[0]-1,:])) 
        img=np.column_stack((img[:,0],img))
        img=np.column_stack((img,img[:,img.shape[1]-1])) 
    return img

def dilatacion(img,kernel=np.ones((3,3))):
    dim_k=kernel.shape
    res=np.zeros((np.array(img.shape)-np.array(kernel.shape)+1))
    for x in range(res.shape[0]):
        for y in range(res.shape[1]):
            res[x,y]=np.max(img[x:x+dim_k[0],y:y+dim_k[1]]*kernel)
    return res

def erosion(img,kernel=np.ones((3,3))):
    dim_k=kernel.shape
    res=np.zeros((np.array(img.shape)-np.array(kernel.shape)+1))
    for x in range(res.shape[0]):
        for y in range(res.shape[1]):
            res[x,y]=np.min(img[x:x+dim_k[0],y:y+dim_k[1]]*kernel)
    return res

def apertura(img,kernel=np.ones((3,3))):
    return dilatacion(erosion(img,kernel),kernel)

def cierre(img,kernel=np.ones((3,3))):
    return erosion(dilatacion(img,kernel),kernel)

def borde_exterior(img,kernel=np.ones((3,3))):
    dil=dilatacion(img,kernel)
    out=repetir_filas(dil,kernel)-img
    out=np.maximum(0,out)
    return out

def borde_interior(img,kernel=np.ones((3,3))):
    ero=erosion(img,kernel)
    out=img-repetir_filas(ero,kernel)
    out=np.maximum(0,out)
    return out

def gradiente(img,kernel=np.ones((3,3))):
    dil=dilatacion(img,kernel)
    ero=erosion(img,kernel)
    out=dil-ero
    out=np.maximum(0,out)
    return out

def mediana(img,kernel=np.ones((3,3))):
    dim_k=kernel.shape
    res=np.zeros((np.array(img.shape)-np.array(kernel.shape)+1))
    for x in range(res.shape[0]):
        for y in range(res.shape[1]):
            res[x,y]=np.median(img[x:x+dim_k[0],y:y+dim_k[1]]*kernel)
    return res

def top_hat(img, kernel=np.ones((3,3))):
    ap=apertura(img,kernel)
    ap=repetir_filas(repetir_filas(ap,kernel),kernel)
    return np.maximum(img-ap,0)

def bottom_hat(img,kernel=np.ones((3,3))):
    ci=cierre(img,kernel)
    ci=repetir_filas(repetir_filas(ci,kernel),kernel)
    return np.maximum(ci-img,0)