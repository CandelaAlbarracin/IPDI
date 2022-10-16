import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage import filters
from skimage import color
from sklearn.cluster import KMeans
from skimage import measure

def rgb_yiq(matriz):
    yiq = np.ndarray(matriz.shape)
    cte=np.array([[0.299,0.587,0.114],[0.595716,-0.274453,-0.321263],[0.211456,-0.522591,0.311135]])
    yiq[:,:,0]=np.dot(matriz,cte[0,:])
    yiq[:,:,1]=np.dot(matriz,cte[1,:])
    yiq[:,:,2]=np.dot(matriz,cte[2,:])
    return yiq

def yiq_rgb(matriz):
    cte=np.array([[1,0.9663,0.6210],[1,-0.2721,-0.6474],[1,-1.1070,1.7046]])
    rgb=np.ndarray(matriz.shape)
    rgb[:,:,0]=np.dot(matriz,cte[0,:])
    rgb[:,:,1]=np.dot(matriz,cte[1,:])
    rgb[:,:,2]=np.dot(matriz,cte[2,:])
    return rgb

def segmentacion_mediana(img):
    img=rgb_yiq(img)
    mediana=np.median(img[:,:,0])
    img[:,:,0]=np.where(img[:,:,0]>mediana,1,0)
    return yiq_rgb(img)

def seg_mediana(img):
    """
    Permite segmentar la imagen con un umbral global igual a la mediana
    img: array que contiene la imagen a segmentar
    """
    if img.ndim!=2: #si la imagen no es binaria (RGB) se convierte a escala de grises
        img=color.rgb2gray(img)
    mediana=np.median(img)
    img=np.where(img>mediana,1,0)
    return img

def seg_kmeans(img,n):
    if img.ndim!=2: #si la imagen no es binaria (RGB) se convierte a escala de grises
        img=color.rgb2gray(img)
    image_gray= img.reshape(img.shape[0] * img.shape[1], 1)
    kmeans = KMeans(n_clusters=n).fit(image_gray)
    clustered = kmeans.cluster_centers_[kmeans.labels_]
    labels = kmeans.labels_
    for n in range(n):
        image_cluster = []
        for i in range(len(labels)):
            if(labels[i]) == n:
                image_cluster.append(float(clustered[i]))
            else:
                image_cluster.append(1)
        if(n==1):
            image_fix= np.array(image_cluster).reshape(img.shape)
        reshape_clustered = np.array(image_cluster).reshape(img.shape)
    umbral=np.unique(reshape_clustered)
    return reshape_clustered>umbral[0]

def seg_otsu(img):
    if img.ndim!=2: #si la imagen no es binaria (RGB) se convierte a escala de grises
        img=color.rgb2gray(img)
    val = filters.threshold_otsu(img)
    return img>val

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

def kernel_laplaciano(n):
    if n==4:
        return np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    elif n==8:
        return np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    else:
        ValueError("Solo puede introducir el valor 4 u 8")

def convolucionar(img,kernel=np.ones((1,1))):
    res=np.zeros((np.array(img.shape)-np.array(kernel.shape)+1))
    for x in range(res.shape[0]):
        for y in range(res.shape[1]):
            res[x,y]=np.sum(img[x:x+kernel.shape[0],y:y+kernel.shape[1]]*kernel)
    return res

def seg_marchine_square(img):
    if img.ndim>2:
        img=color.rgb2gray(img)
    contours = measure.find_contours(img)

    fig, ax = plt.subplots()
    ax.imshow(np.zeros(img.shape), cmap="gray")

    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=1,color="white")
    ax.axis('off')
    plt.savefig("out_ms.png", bbox_inches='tight',dpi=500,pad_inches = 0)
    return mpimg.imread("out_ms.png")
