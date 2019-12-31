import os
import cv2
import matplotlib.pyplot as pyplot
import numpy as np
import glob
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)


last = glob.glob("source_img/10/*")
latest_file = max(last,key=os.path.getctime)
f = latest_file.replace("source_img/10/","")
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
cv2.imwrite("target_img/"+f,result)
img1 = cv2.imread("source_img/10/"+f.replace("b0s0l0h0","b0s0l0h1")) 
img1 = np.power(img1/float(np.max(img1)), 1/1.5)
cv2.imwrite("source_img/10/"+f.replace("b0s0l0h0","b0s0l0h1"),img1*255)         
       
     

        
        
                
            
            
