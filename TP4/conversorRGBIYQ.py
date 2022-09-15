import numpy as np

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


