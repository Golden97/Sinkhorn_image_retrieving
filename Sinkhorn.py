import numpy as np
import SinkhornAlgorithm
import ReadRGB



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

    #R = np.array([0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.30, 0.20])
    R = np.array([0.020336 ,  0.022928 ,  0.00488  , 0.02884267 ,0.45736533 ,0.10637867,
 0.34859733, 0.010672  ])
    #C= np.array([0, 0.20, 0.20, 0.12, 0.12, 0.12, 0.12, 0.12])
    C = np.array([0.020336 ,  0.022928 ,  0.00488  , 0.02884267 ,0.45736533 ,0.10637867,
 0.34859733, 0.010672  ])
    M=crateCostMatrix(2)
    #print M
    B=np.matrix(M)
    M=np.asarray(B)
    #print type(M)
    #R=R.reshape((2,2,2))
    #C=C.reshape((2,2,2))
    #print (SinkhornAlgorithm.dmAlfa(1/10,R,C,M))
    path=r"C:\Users\Andrea\Desktop\TestImage\zebra1.jpg"
    R=ReadRGB.readImage(path)
    path = r"C:\Users\Andrea\Desktop\TestImage\zebra2.jpg"

    C=ReadRGB.readImage(path)
    print (R)
    print(C)
    print (SinkhornAlgorithm.dmAlfa(1/10,R,C,M))



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
