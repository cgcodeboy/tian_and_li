# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:25:56 2019

@author: cgcodeboy
"""

import os

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

path = '../photo/'
file_path = './photo/yinchuan.html'

name = []
for file in os.listdir(path):
    name.append(file)

use_name = []
count = 0
for file in name:
    if is_number(file[:-5]):
        if int(file[:-5]) >= 1566025257889 and int(file[:-5]) <= 1566025260732:
            use_name.append(file)
            count += 1

print(count)
i = 0
with open(file_path + '_','w',encoding = 'utf-8') as temp_file:
    with open(file_path,'r',encoding = 'utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.find('<img src=') != -1:
                line = line[:34] + use_name[i] + line[34:]
                temp_file.write(line)
                i += 1
            else:
                temp_file.write(line)
        file.close()
    temp_file.close()
            
print(i)
