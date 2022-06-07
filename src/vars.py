'''
Header file for variables
'''

import os


#sign array
sign =[r"Добро пожаловать в программу",
       r"по выбору оптимальной конфигурации для ноутбука",
       r"::::::::::::::::::::::::::::::",
       r"::        _______________   ::",
       r"::       /\______________\  ::",
       r"::      / /    Notebook  /  ::",
       r"::     / /    for       /   ::",
       r"::    / /    Math      /    ::",
       r"::   / /    Packets   /     ::",
       r"::  /_/______________/      ::",
       r"::  \ \\\\\\\\\\\\\\\\      ::",
       r"::   \ \\\\\\\\\\\\\\\\     ::",
       r"::    \ \\\\\\\\\\\\\\\\    ::",
       r"::     \ \\\\\\\\\\\\\\\\   ::",
       r"::      \/______________/   ::",
       r"::                          ::",
       r"::::::::::::::::::::::::::::::"]

width = os.get_terminal_size().columns #get width of terminal
height = os.get_terminal_size().lines #get height of terminal

money=0 #budget
prior=0 #gc or processor
storage=0 #ssd

#                        cheap          medium            uni          powerfull
choose_processor = [['277_3pentium','277_3ryzend15','277_3cored1i5','277_3cored1i7'],
['Pentium','ryzen 5','i5','i7']]
choose_ram_type = [['11699_3ddr3','11699_3ddr4','11699_3ddr4','11699_3ddr4'],
['DDR3','DDR4','DDR4','DDR4']]
choose_graphic_card = [['1046_3integrirovannyy','1046_3integrirovannyy','12461_3nvidiad1geforced1d1rtxd13060d1dlyad1noutbukovd1a5d16144d1mb','12461_3nvidiad1geforced1d1rtxd13070d1dlyad1noutbukovd1a5d18192d1mb'],
['Integrated','Integrated','RTX 3060','RTX 3070']]
choose_storage_type = [['11496_3','2588_3','2589_3','2589_3'],
['emmc','hdd','ssd','ssd']]

#             cheap     medium     uni     powerfull
processor = ['ryzen 3','ryzen 5','ryzen 7','ryzen 9']
graphic_card = [
['Integrated/Office GC','GTX 1050','GTX 1080','RTX 3090 TI'],
['Integrated/Office GC','GTX 1050','GTX 1080','NVIDIA Quadro']]
ram_type = ['ddr2','ddr3','ddr4','ddr5']
storage_type = [['emmc','hdd','ssd','ssd'],
['emmc','hdd','ssd','nvme']]
notebook_type = ['Дешёвый ноутбук','Бюджетный ноутбук','Универсальный ноутбук','Мощный ноутбук']