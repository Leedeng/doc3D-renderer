import os
import cv2
import matplotlib.pyplot as pyplot
import numpy as np
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)
os.mkdir("gt1")
os.mkdir("gt2")
for f in os.listdir('img/10'):
    if f.endswith('.png'):
        img = cv2.imread("label/10/"+f,0) 
        window_size = 25
        thresh_sauvola = threshold_sauvola(img, window_size=25)
        result = img>thresh_sauvola
        result = result.astype('uint8')
        result = result*255
        label = cv2.imread("gt/10/"+f,0)
        ret,th = cv2.threshold(label,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        for i in range(th.shape[0]):
            for j in range(th.shape[1]):
                if th[i,j] == 0:
                    result[i,j] = 255
        cv2.imwrite("gt1/"+f,result)        

                    
for f in os.listdir('img/10'):
    if f.endswith('.png'):
        img = cv2.imread("img/10/"+f,0) 
        window_size = 25
        thresh_sauvola = threshold_sauvola(img, window_size=25)
        result = img>thresh_sauvola
        result = result.astype('uint8')
        result = result*255
        label = cv2.imread("gt/10/"+f,0)
        ret,th = cv2.threshold(label,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        for i in range(th.shape[0]):
            for j in range(th.shape[1]):
                if th[i,j] == 0:
                    result[i,j] = 255
        cv2.imwrite("gt2/"+f,result)        

        
        
                
            
            
