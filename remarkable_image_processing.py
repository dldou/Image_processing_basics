#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:58:51 2022

@author: dldou
"""

import numpy as np


def photomaton(image):
        
    res = np.copy(image)
    
    #We divided image in 2 therefore we need the center of the image
    mid_column = int(image.shape[0]/2) 
    mid_row    = int(image.shape[1]/2)
    
    # On procède pixel par pixel
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[0]):
            
            #If row and column index are even --> keep the pixel at its place (left superior square)
            if i%2 == 0 and j%2 == 0:
                k_i = int(i/2)
                k_j = int(j/2)
                res[k_i,k_j,:] = image[i, j, :]
        
            #If row index even and left index odd --> pixel go to left inferior square
            if i%2 == 0 and j%2 == 1:
                k_i = int(i/2)
                k_j = int((j-1)/2)
                res[k_i, (mid_row+k_j),:] = image[i, j, :]
            
            #If row index odd and left index even --> pixel go to right superior square
            if i%2 == 1 and j%2 == 0:
                k_i = int((i-1)/2)
                k_j = int(j/2)
                res[(mid_column+k_i), k_j,:] = image[i, j, :]
            
            #If row index odd and left index odd --> pixel go to right inferior square
            if i%2 == 1 and j%2 == 1:
                k_i = int((i-1)/2)
                k_j = int((j-1)/2)
                res[(mid_column+k_i), (mid_row+k_j),:] = image[i, j, :]
                
    return res.astype(int)