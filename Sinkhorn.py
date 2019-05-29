import numpy as np
import SinkhornAlgorithm
import panda as pd
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
    R = np.array([0, 0.12, 0.12, 0.12, 0.12, 0.12, 0.20, 0.20])
    #C= np.array([0, 0.20, 0.20, 0.12, 0.12, 0.12, 0.12, 0.12])
    C = np.array([0, 0.12, 0.12, 0.12, 0.12, 0.12, 0.20, 0.20])
    M=crateCostMatrix(2)
    #print M
    B=np.matrix(M)
    M=np.asarray(B)
    #print type(M)
    print SinkhornAlgorithm.dmAlfa(1/10,R,C,M)
'''
    # READ COST MATRIX
    f = open("C:\\Users\\Andrea\\Desktop\\TxtForPythonLicencjat\\testout.txt", "r")
    MCostMatrix = f.read()
    f.close()
    MCostMatrix = [item.split() for item in MCostMatrix.split('\n')[:-1]]
    ###############################################################################
    # READ R HISTOGRAM
    r = open("C:\\Users\\Andrea\\Desktop\\TxtForPythonLicencjat\\RHistogram.txt", "r")
    RHistogram = np.loadtxt(r)
    r.close()
    RHistogram = RHistogram.reshape((4, 4, 4))
    #######################################################################
    # READ C HISTOGRAM
    c = open("C:\\Users\\Andrea\\Desktop\\TxtForPythonLicencjat\\CHistogram.txt", "r")
    CHistogram = np.loadtxt(c)
    c.close()
    CHistogram = CHistogram.reshape((4, 4, 4))
    CHistogram = SinkhornAlgorithm.mapHistogram(CHistogram)
    RHistogram = SinkhornAlgorithm.mapHistogram(RHistogram)
    #
    # print MCostMatrix
    # print RHistogram[0][1][2]
    MCostMatrix=np.asarray(MCostMatrix)
    #print np.multiply(-0.01,MCostMatrix.astype(float))
    print SinkhornAlgorithm.dmAlfa(1, RHistogram, CHistogram, MCostMatrix.astype(float))#McostMAtrix default type=numpy.string_
'''





main()
