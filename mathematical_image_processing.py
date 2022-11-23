#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:59:45 2022

@author: dldou
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from math import sqrt

def histogram_normalization(image):
    
    res = np.zeros_like(image)
    
    for k in range(3):
        res[:,:,k] = cv.equalizeHist(image[:,:,k])
        
    return res


def add_white_noise(image, nof_white_noise_points):
    
    res = np.copy(image)
    
    #Replace random pixels by white pixels 
    for i in range(nof_white_noise_points):
        
        i = randint(0, image.shape[0]-1)
        j = randint(0, image.shape[1]-1)
        res[i,j] = 255
    
    return res


def low_pass_filter_constructor(image, 
                                distance_threshold):
    
    res          = np.zeros_like(image)
    image_center = (image.shape[0]//2, image.shape[1]//2)
    
    res[(image_center[0]-distance_threshold):(image_center[1]+distance_threshold), (image_center[0]-distance_threshold):(image_center[1]+distance_threshold)] = 1
    
    #    for x in range(image.shape[1]):
    #        for y in range(image.shape[0]):
    #            
    #            # Met à 1 tout ce qui est compris dans le cercle de centre (0,0) et de rayon 'distance'
    #            if distance_criterion((y,x),centre) < distance_threshold:
    #                transfert[y,x] = 1
                
    return res



def periodic_noise_reduction(image, filter):
    
    #FFT of the image
    fft_image = np.fft.fft2(image)
    
    #Centering the FFT
    centered_fft_image = np.fft.fftshift(fft_image)
    
    #Filtering the TFD
    filtered_fft = centered_fft_image*filter
    
    #Decentering
    decent_filtered_fft = np.fft.ifftshift(filtered_fft)
    
    #Image reconstruction
    filtered_image = np.fft.ifft2(decent_filtered_fft)
 
    
    #Plot
    plt.figure(figsize=(20,20))
    
    #Image
    plt.subplot(2,2,1)
    plt.title("Noisy image")
    plt.imshow(np.abs(image), cmap='gray')
    plt.axis('off')
    
    #FFT of the image
    plt.subplot(2,2,2)
    plt.title("Frequency spectrum of the noisy image")
    plt.imshow(np.log(1 + np.abs(centered_fft_image)), cmap='gray')
    plt.axis('off')
    
    #Filtered FFT of the image
    plt.subplot(2,2,3)
    plt.title("Filtered frequency spectrum")
    plt.imshow(np.log(1 + np.abs(filtered_fft)), cmap='gray')
    plt.axis('off')
    
    #Denoised image
    plt.subplot(2,2,4)
    plt.title("Denoised image")
    plt.imshow(np.abs(filtered_image), cmap='gray')
    plt.axis('off')
    
    #Save figure
    plt.savefig("Denoised_image_processing" + ".pdf")
    
    #Show figure
    plt.show()
    
    return filtered_image



