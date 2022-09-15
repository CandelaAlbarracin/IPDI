import numpy as np
from math import factorial

def convolucionar(img,kernel=np.ones((1,1))):
    res=np.zeros((np.array(img.shape)-np.array(kernel.shape)+1))
    for x in range(res.shape[0]):
        for y in range(res.shape[1]):
            res[x,y]=np.sum(img[x:x+kernel.shape[0],y:y+kernel.shape[1]]*kernel)
    return res

def kernel_promedio(n):
    kernel=np.ones((n,n))
    divisor=np.sum(kernel)
    return np.divide(kernel,divisor)

def kernel_bartlett(n):
    sec=np.concatenate((np.arange(1,n//2+1),np.array(n//2+1),np.arange(n//2,0,-1)),axis=None)
    kernel=np.outer(sec,sec)
    return kernel/np.sum(sec)**2

def kernel_gaussiano(n):
    pascal=np.ndarray(n,dtype=int)
    for i in range(0,n):
        pascal[i]=factorial(n-1)//(factorial(i)*factorial(n-1-i))
    kernel=np.outer(pascal,pascal)
    return kernel/np.sum(pascal)**2

def kernel_laplaciano(n):
    if n==4:
        return np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    elif n==8:
        return np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    else:
        ValueError("Solo puede introducir el valor 4 u 8")

def kernel_direccional(dir):
    if dir=="N":
        return np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    elif dir=="NE":
        return np.array([[0,-1,-2],[1,0,-1],[2,1,0]])
    elif dir=="E":
        return np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    elif dir=="SE":
        return np.array([[2,1,0],[1,0,-1],[0,-1,-2]])
    elif dir=="S":
        return np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    elif dir=="SO":
        return np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
    elif dir=="O":
        return np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    elif dir=="NO":
        return np.array([[-2,-1,0],[-1,0,1],[0,1,2]])