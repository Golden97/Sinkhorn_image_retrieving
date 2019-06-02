import numpy as np
import SinkhornAlgorithm
import ReadRGB
from pyemd import emd



def crateCostMatrix(nr):#nr=number of colors in histogram for example if histogram is [4][4][4] nr=4
    M=''
    for x in range(0,nr):
        for y in range(0,nr):
            for z in range(0,nr):
                if M!='':
                    M+=';'
                for a in range(0,nr):
                    for b in range(0,nr):
                        for c in range(0,nr):
                            M+=str(np.sqrt(np.power(x-a,2)+np.power(y-b,2)+np.power(z-c,2)))
                            M+=' '
    return M


def main():


    R = np.array([1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    C= np.array([1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    M=crateCostMatrix(2)
    B=np.matrix(M)
    M=np.asarray(B)
    path=r"C:\Users\Andrea\Desktop\TestImage\zebra2.jpg"
    #R=ReadRGB.readImage(path)
    path = r"C:\Users\Andrea\Desktop\TestImage\zebra1.jpg"

    #C=ReadRGB.readImage(path)
    #print (R)
    #print(C)
    print (SinkhornAlgorithm.dLambda(1/10,R,C,M,0))
    print (emd(R,C,M))





main()
