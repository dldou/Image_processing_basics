#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:37:22 2020

@author: dldou
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#Function to import image
def image_importation(file_path):
    """
        Based on OpenCV
    """
    image = cv.imread(file_path)
    #Arrenging the order
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    
    return image


def image_show(image, title):
    
    plt.figure()
    plt.title(title + " $({}x{})$".format(image.shape[0], image.shape[1]))
    plt.axis("off")
    plt.imshow(image)
    plt.show()
    
    return None

def red_extract(image):
    
    #Copying the image to avoid direct modification
    res = np.copy(image)
    
    #Set other params to zero
    res[:,:,1] = 0
    res[:,:,2] = 0
    
    return res

def neg(image):
    
    res = np.copy(image)
    
    #negatif: pix_value_res = 255 - pix_value
    res[:,:,:] = 255 - res[:,:,:]
    
    return res

def to_grey(image):
    
    res = np.copy(image)
    
    #pix_value_res = 0.299*pix_value_red + 0.587∗pix_value_green + 0.114∗pix_value_blue
    res[:,:,:] = 0.229*res[:,:,0] + 0.587*res[:,:,1] + 0.114*res[:,:,2] 
    
    return res

def sepia(image, image_red_coeff, image_green_coeff, image_blue_coeff):
    
    res = np.copy(image)
    
    #Sepia 
    #pix_value_res_red   = 0.393*pix_value_red + 0.769∗pix_value_green + 0.189∗pix_value_blue
    #pix_value_res_green = 0.349*pix_value_red + 0.686∗pix_value_green + 0.168∗pix_value_blue
    #pix_value_res_blue  = 0.272*pix_value_red + 0.534∗pix_value_green + 0.131∗pix_value_blue
    
    for k in range(3):
        
        res[:,:,k] = image_red_coeff[k]*image[:,:,0] + image_green_coeff[k]*image[:,:,1] + image_blue_coeff[k]*image[:,:,2]
    
    return res

def contrast(image):
    
    res = np.copy(image)
    
    res[res<30] = 0
    res[res>=225] = 255
    res[res>=30 and res<225] = (255.0/195.0)*(res[res>=30 and res<225]-30)+0.5
    
    return res
    
def grey_threshold(grey_image, threshold):
    
    res = np.copy(grey_image)
    
    res[res<=threshold] = 0
    res[res>threshold]  = 255
    
    return res

def color_threshold(image, threshold):
    
    res = np.copy(image)
    
    res[res<=threshold] = 0
    res[res>threshold]  = 255
    
    return res


def flip(image):
    
    res = np.copy(image)
    
    return res[::-1]



    