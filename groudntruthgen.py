import os
import cv2
import csv
import matplotlib.pyplot as pyplot
import numpy as np
import glob
import sys
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)

env_list = './envs.csv'
tex_list = './tex.csv'
obj_list = './objs.csv'
id2 = int(sys.argv[-3])
id1 = int(sys.argv[-2])
id3 = int(sys.argv[-1])
rridx = int(sys.argv[-4])
with open(env_list, 'r') as f:
    envlist = list(csv.reader(f))

with open(tex_list, 'r') as t, open(obj_list, 'r') as m:
    texlist = list(csv.reader(t))
    objlist = list(csv.reader(m))
    objpath = objlist[id1][0]
    texpath=texlist[id2][0]
    fn = objpath.split('/')[-1][:-4] + "-" + texpath.split('/')[-1][:-4] + "-" + envlist[id3][0].split('/')[-1][:-4] + "b{}s{}l{}h{}-"

    f = fn.format("0","0","0","0")
    f = f + "0001.png"
    print(f)
    img = cv2.imread("label/10/"+f,0) 
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
       
     

        
        
                
            
            
