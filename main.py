#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:45:10 2020

@author: dldou
"""

from basic_treat import * 
from mathematical_image_processing import *
from remarkable_image_processing import *

if __name__=="__main__":
    
    basics_proc = False
    math_proc   = True
    
    if basics_proc:
        #Basics of image processing on an example (Lena.jpg)
        
        image_path = "images/Lena.jpg"
        image = image_importation(image_path)
        
        res = red_extract(image)
        title = "Extraction of the red component"
        image_show(image, res, title)
        
        res = neg(image)
        title = "Negatif"
        image_show(image, res, title)
        
        res = to_grey(image)
        title = "Grey"
        image_show(image, res, title, gray=True)
        
        image_red_coeff   = (0.393, 0.349, 0.272)
        image_green_coeff = (0.769, 0.686, 0.534)
        image_blue_coeff  = (0.189, 0.168, 0.131)
        res = sepia(image, image_red_coeff, image_green_coeff, image_blue_coeff)
        title = "Sepia"
        image_show(image, res, title)
        
        res = contrast(image)
        title = "Contrasted"
        image_show(image, res, title)
        
        res = color_threshold(image, int(255/2))
        title = "Threshold=255/2"
        image_show(image, res, title)
        
        res = flip(image)
        title = "Flipped"
        image_show(image, res, title)
    
    elif math_proc:
    
        image_path = "images/aquitain.tif"
        image = image_importation(image_path)
        
        processed_image = histogram_normalization(image)
        title = "Histogram normalization"
        image_show(image, processed_image, title)
        
        image_path = "images/Lena.jpg"
        image = image_importation(image_path)
        
        nof_white_noise_points = 4000
        processed_image = add_white_noise(image, nof_white_noise_points)
        title="White noise"
        image_show(image, processed_image, title)
        
        image_path = "Images/clown.tif"
        image = image_importation(image_path)
        image = image[:,:,0]
        
        filter = low_pass_filter_constructor(image, distance_threshold=20)
        processed_image = periodic_noise_reduction(image, filter)
        
        
        image_path      = "images/MonaLisa_square.jpg"
        image           = image_importation(image_path)
        processed_image = image
        
        for n in range(12):    
            image = processed_image
            processed_image = photomaton(processed_image)
            title="Photomaton n°" + str(n+1)
            image_show(image, processed_image, title)
        
        
        #res = (image)
        #title = ""
        #image_show(image, res, title)
    
    