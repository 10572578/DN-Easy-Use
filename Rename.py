# -*- coding: UTF-8 -*-
import os

def rename():
    path = 'D:\\Py Projects\\pic\\'
    for pic in os.listdir(path):
        if os.path.isfile(os.path.join(path, pic)) == True:
            new_name = pic.replace('\xb3\xcb\xb7\xa8\xc6\xf7', "Multiplier")
            os.rename(os.path.join(path, pic), os.path.join(path, new_name))

rename()