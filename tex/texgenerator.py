import os
import cv2
import matplotlib.pyplot as pyplot
import numpy as np
import random

os.mkdir("../tex_b")
os.mkdir("../tex_s")

for f in os.listdir('./'):
    if f.endswith('.png'):
        stain_num = random.randint(1, 8)
        stamp_num = random.randint(1, 8)
        blur_num = random.randint(1, 2)
        
        img = cv2.imread(f)   
        stain = cv2.imread("./Stamp&Stain/stain"+str(stain_num)+".jpg")
        stain = cv2.resize(stain,(300,300))
        mask = 255 * np.ones(stain.shape, stain.dtype)
        width, height, channels = img.shape
        center = (int(300), int(300))
        mixed_clone = cv2.seamlessClone(stain, img, mask, center, cv2.MIXED_CLONE)
        stamp = cv2.imread("./Stamp&Stain/stamp"+str(stamp_num)+".jpg")
        stamp = cv2.resize(stamp,(300,300))
        mask = 255 * np.ones(stamp.shape, stamp.dtype)
        width, height, channels = img.shape
        center = (int(height-300), int(width-300))
        mixed_clone2 = cv2.seamlessClone(stamp, mixed_clone, mask, center, cv2.MIXED_CLONE)
        cv2.imwrite("../tex_s/"+f,mixed_clone2)
  

        if blur_num == 1:
            blur = cv2.blur(img,(5,5))
        if blur_num == 2:

            kernel_size = 8
            kernel_h = np.zeros((kernel_size, kernel_size)) 
            kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size) 
            kernel_h /= kernel_size 
            blur = cv2.filter2D(img, -1, kernel_h) 



        cv2.imwrite("../tex_b/"+f,blur)
                    


        
        
                
            
            
