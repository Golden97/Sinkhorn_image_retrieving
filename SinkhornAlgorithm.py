import numpy as np
from scipy.linalg import expm


def dmAlfa(alfa, r, c, M):
    mylambda=1/10
    #while True:
    return dLambda(mylambda,r,c,M,alfa,0)
        ##if vectorsDistance(answer[1],entropyV(r)+entropyV(c)-alfa)<=0.01:


def entropyV(vector):
    sum = 0
    for i in vector:
        sum -= i * np.log(i)
    return sum


def entropyM(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            sum -= j * np.log(j)
    return sum


def KL(P, Q):
    sum = 0
    for i in P:
        for j in i:
            sum += j * (np.log(j) / np.log(Q[i][j]))
    return sum

def mapHistogram(histogram):
    vector=[]
    for i in histogram:
        for j in i:
            for k in j:
                vector.append(k)
    return vector


def vectorsDistance(a,b):
    return np.linalg.norm(a - b)

def pos(lst):
    return [x for x in lst if x > 0] or None#i posti dove ce zero ricordarli per toglierli in M? (k forse anche adesso chiedo)

def posMat(lst,M):
    i=0
    delete=[]
    for x in lst:
        if x==0:
            delete.append(i)
        i=i+1
    #print delete
    #print np.delete(M, delete,0)
    return np.delete(M, delete,0)



def dLambda(myLambda, R, C, M,alfa,iteration):
   # print M
    M=posMat(R,M)
   # print M
    K=np.exp(-myLambda*M)
    R=pos(R)
    #print R
    #print K
    #print -myLambda*M
    u = np.ones(len(R))
    ones = np.ones(len(u))
    u=np.divide(u, len(R))
    oldU=u
    tmp=np.divide(ones,R)
    tmp2=np.diag(tmp)
    #print K
    Kdiagonal=np.matmul(tmp2,K)#matmul=multiplication for matrix/////multiply=element-whise multiplication
    iter=0


    #print iteration
    while True:
        #u=np.multiply(ones,np.matmul(Kdiagonal,np.divide(C,np.matmul(K.transpose(),u))))
        u = np.divide(R,(np.matmul(K, np.divide (C,np.matmul(np.transpose(K),u)))))
        if vectorsDistance(u,oldU)<0.01 or iter>10000:#odleglosc vektora a nie array equal
            break;


        iter=iter+1
        oldU=u
    #vpiece=np.matmul(K.transpose(),u)
    #v=np.divide(C,vpiece)


    vpiece = np.matmul( u.transpose(),K)
    v=np.divide(C,vpiece.transpose())

    #v = b. / ((u'*K)');
    u=np.divide(R,np.matmul(K,v))
    #u = a. / (K * v);
    d=np.multiply(u,np.matmul(np.multiply(K,M),v))
    d=d.sum()
    #U = K.*M
    #D = sum(u. * (U * v));
    PLambda=np.matmul(np.matmul(np.diag(u),K),np.diag(v))
    if vectorsDistance(PLambda,entropyV(R)+entropyV(pos(C))-alfa)<=0.01 or iteration>100:
        return d
    else:
        return dLambda(myLambda*1.5,R,C,M,alfa*1.5,iteration+1)

