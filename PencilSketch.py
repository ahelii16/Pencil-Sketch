# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:04:47 2018

@author: debja
"""

import imageio

img = r"C:\Users\debja\Desktop\test_pic.jpg"
start_img = imageio.imread(img)

#interpret image shape
start_img.shape

#applying greyscale
import numpy as np
def grayscale(rgb):
 return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
gray_img = grayscale(start_img)

#inverted image
inverted_img = 255-gray_img

#blur the inverted image
import scipy.ndimage
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=20)
#play with sigma for clearer results!

#dodge and merge
#divides the bottom layer by the inverted top layer
def dodge(front,back):
 result=front*255/(255-back) 
 result[result>255]=255
 result[back==255]=255
 return result.astype('uint8')
final_img= dodge(blur_img,gray_img)

#result plot
import matplotlib.pyplot as plt
plt.imshow(final_img, cmap="gray")

#save
plt.imsave('img3.png', final_img, cmap='gray', vmin=0, vmax=255)