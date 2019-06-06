#C:\Users\Andrea\Desktop
from PIL import Image
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def createHistogram(precision, rgbValues):
    precisionBig=(256//precision)*(256//precision)*(256//precision)
    precisionRGB=256//precision
    histogram=np.arange(precisionBig)
    histogram=histogram.reshape((precisionRGB,precisionRGB,precisionRGB))
    histogram=np.zeros_like(histogram)
    #print(histogram)
    for pixel in rgbValues:
        histogram[pixel[0]//precision,pixel[1]//precision,pixel[2]//precision]+=1
    return histogram.reshape(precisionBig)




def readImage(path,precision):
    im=Image.open(path,"r")
    hist=createHistogram(precision,list(im.getdata()))
    #hist=np.histogram(im,64)
    print("\n",hist)
    #a=plt(hist)
    #plt.show()
    plt.hist(hist,density=False, bins=len(hist))  # density
    plt.ylabel('Probability')
    #plt.xticks(range(0,len(hist)))
    #plt.yticks(hist)
    plt.show()
    return np.divide(hist,hist.sum())