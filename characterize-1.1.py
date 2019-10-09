# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:10:17 2019

@author: Shyam Mittal
"""
# these variables can be changed
height = 65
width = 100
character = 'X'

# Importing libraries
import cv2
import numpy as np
from hex_color_codes1 import codes_dict,codes
from sklearn.neighbors import NearestNeighbors
from colored import fg,attr

# Reset
rst = attr("reset")

# Coulor list
all_colors_list = []

# Starting for loops for colours
for i in codes:
    temp = []
    for j in range(1,7,2):
        temp.append(int(i[j]+i[j+1],16))
    all_colors_list.append(tuple(temp))
all_colors = np.array(all_colors_list)
    
x = cv2.imread('characterize_github.jpg') #change the file location to your required image

#array_x = np.array(x)
#print(np.shape(array_x))

new_x = cv2.resize(x,(width,height))

color_dict = {}
color_check_arr = []

for i in range(height):
    temp_to_cca = []
    for j in range(width):
        hex_value = "#%02x%02x%02x"%tuple(new_x[i][j])
        if hex_value in codes:
            temp_to_cca.append(hex_value)
        else:
            if not tuple(new_x[i][j]) in list(color_dict.keys()):    
                all_colors_list.append(tuple(new_x[i][j]))
                all_colors = np.array(all_colors_list)
                nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(all_colors)
                distances,indices = nbrs.kneighbors(all_colors)
                temp_calac_val = all_colors_list[indices[16][1]]
                hex_value = "#%02x%02x%02x"%temp_calac_val
                color_dict[tuple(new_x[i][j])] = hex_value
                all_colors_list = all_colors_list[:-1]
            temp_to_cca.append(color_dict[tuple(new_x[i][j])])
    color_check_arr.append(temp_to_cca)

# Showing the Image
for i in range(height):
    for j in range(width):
        color = fg(abs(codes_dict[color_check_arr[i][j]]))
        print(color+character+rst,end="")
    print("",end="\n")

print(np.shape(new_x))
cv2.imshow("Github_logo",new_x)
cv2.waitKey(100)
cv2.destroyAllWindows()
