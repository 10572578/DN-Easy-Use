# -*- coding: UTF-8 -*-
import os


def multiprocess():
    #path = raw_input("The input dir is \n>>> ")
    path = 'D:\\pic'
    for pic in os.listdir(path):
        point = pic.rfind('.')
        d = pic.find('Denoised_')
        if d >= 0:
            continue
        con = 0
        for pict in os.listdir(path):
            d = pict.find('Denoised_')
            if d >= 0:
                if pict[9:] == pic:
                    con = 1
        if con == 1:
            continue
        i = os.path.join(path, pic)
        new_name = 'Denoised_' + pic
        o = os.path.join(path, new_name)
        command = 'D:\\NvidiaAIDenoiser-master\\bin\\Denoiser.exe -i ' + i + ' -o ' + o
        os.system(command)


multiprocess()