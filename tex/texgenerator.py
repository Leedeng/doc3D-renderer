import os
import cv2
import matplotlib.pyplot as pyplot
import numpy as np
import random


for f in os.listdir('../source/'):
    if f.endswith('.png'):
        img = cv2.imread('../source/'+f) # Read in the image and convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white
        coords = cv2.findNonZero(gray) # Find all non-zero points (text)
        x, y, w, h = cv2.boundingRect(coords) # Find minimum spanning bounding box
        rect = img[y:y+h, x:x+w]
        cv2.imwrite(f,rect)

        
os.mkdir("../tex_b")
os.mkdir("../tex_s")        
for f in os.listdir('./'):
    if f.endswith('.png'):
 
        stain_num = random.randint(1, 8)
        stamp_num = random.randint(1, 8)
        blur_num = random.randint(1, 2)
        
        img = cv2.imread(f) 
        width, height, channels = img.shape  

        stain = cv2.imread("./Stamp&Stain/stain"+str(stain_num)+".jpg")
        stain = cv2.resize(stain,(int(height/3),int(width/3)))
        mask = 255 * np.ones(stain.shape, stain.dtype)

        center = (int(height/3), int(width/3))
        mixed_clone = cv2.seamlessClone(stain, img, mask, center, cv2.MIXED_CLONE)
        stamp = cv2.imread("./Stamp&Stain/stamp"+str(stamp_num)+".jpg")
        stamp = cv2.resize(stamp,(int(height/3),int(width/3)))
        mask = 255 * np.ones(stamp.shape, stamp.dtype)
        width, height, channels = img.shape
        center = (int(height-int(height/3)), int(width-int(width/3)))
        mixed_clone2 = cv2.seamlessClone(stamp, mixed_clone, mask, center, cv2.MIXED_CLONE)
        cv2.imwrite("../tex_s/"+f,mixed_clone2)
  

        if blur_num == 1:
            blur = cv2.blur(img,(int(height/100),int(height/100)))
        if blur_num == 2:

            kernel_size = 8
            kernel_h = np.zeros((kernel_size, kernel_size)) 
            kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size) 
            kernel_h /= kernel_size 
            blur = cv2.filter2D(img, -1, kernel_h) 



        cv2.imwrite("../tex_b/"+f,blur)
                    


        
        
                
            
            
