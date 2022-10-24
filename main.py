#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:45:10 2020

@author: delphinedoutsas
"""

from basic_treat import * 

if __name__=="__main__":
    
    
    #Example 1
    title = 'Lena, size:'
    
    image_path = "images/Lena.jpg"
    image = image_importation(image_path)
    image_show(image, title)
    
    res = red_extract(image)
    title = "Extraction of the red component"
    image_show(res, title)
    
    res = neg(image)
    title = "Negatif version"
    image_show(res, title)
    
    #res = to_grey(image)
    #title = "Grey version"
    #image_show(res, title)
    
    image_red_coeff   = (0.393, 0.349, 0.272)
    image_green_coeff = (0.769, 0.686, 0.534)
    image_blue_coeff  = (0.189, 0.168, 0.131)
    #res = sepia(image, image_red_coeff, image_green_coeff, image_blue_coeff)
    #title = "Sepia version"
    #image_show(res, title)
    
    #res = contrast(image)
    #title = "Contrasted version"
    #image_show(res, title)
    
    res = color_threshold(image, 30)
    title = "Thresholded version"
    image_show(res, title)
    
    res = flip(image)
    title = "Flipped version"
    image_show(res, title)
    
    #res = (image)
    #title = ""
    #image_show(res, title)
    
    