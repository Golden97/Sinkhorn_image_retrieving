#C:\Users\Andrea\Desktop
from PIL import Image
import numpy as np

def readImage(path):
    im=Image.open(path,"r")
    hist=np.histogram(im,8)
    return np.divide(hist[0],hist[0].sum())