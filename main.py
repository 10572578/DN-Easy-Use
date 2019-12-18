# -*- coding: UTF-8 -*-

import os


def main():
    i = raw_input("The input picture is \n>>> ")
    point = i.rfind('.')
    o = i[:point] + '_Denoised' + i[point:]
    command = 'D:\\NvidiaAIDenoiser-master\\bin\\Denoiser.exe -i ' + i + ' -o ' + o
    os.system(command)


main()
