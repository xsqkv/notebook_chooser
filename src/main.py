'''
Program wich helps you choose notebook for work with mathemathic packets

Author: Artem Vanty GitHub:vantyartem
'''
import os,sys
import http.client
import re
from term import *
if os.name == 'nt':
    from msvcrt import getch
else:
    import termios, fcntl
    import select


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

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines

money=0 #budget
prior=0 #gc or processor
storage=0 #ssd
#https://www.citilink.ru/catalog/noutbuki/?sorting=price_asc&f=277_3pentium,1046_3integrirovannyy,11496_3,11699_3ddr3
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

if os.name != 'nt':
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd) # get current flags
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL) # still get current flags
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK) # set flags with nonblock flag

    newattr = termios.tcgetattr(fd) # get current flags again
    newattr[3] = newattr[3] & ~termios.ICANON # idk exclude icanon flag
    newattr[3] = newattr[3] & ~termios.ECHO # exclude echo flag
    termios.tcsetattr(fd, termios.TCSANOW, newattr) # set flags

def setnewflags():
    termios.tcsetattr(fd, termios.TCSANOW, newattr) # set flags

def setoldflags():
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def getchar():
    if os.name == 'nt':
        c = getch()
    else:
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
    return c

#Clear function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#Set text by x and y
def settext(text,x,y,color=colors.white,style=styles.none,lst='\n'):
    out("\x1b[%d;%dH" % (y,x) + text,color,style,lst)

def setsign(color=colors.white,style=styles.none,lst='\n'):
    i = 0
    for x in sign:
        settext(x,width/2 - len(x)/2,height/3 - len(sign)/2 + i,color,style,lst)
        i+=1

def constructor():
    cls()
    settext('Какой у вас бюджет?',width/2-10,height/3)
    settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
    settext('До 25.000',width/2-5,height/2)
    settext('25.000 - 40.000',width/2-8,height/2+2)
    settext('40.000 - 90.000',width/2-8,height/2+4)
    settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
    
    idx = 10004

    while True:
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
        if c == '\x1b[A'|b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B'|b'P': #DOWN ARROW
            idx+=1
        elif c == '\n': # ENTER KEY
            money=idx%4
            break
        if idx%4==0:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
        elif idx%4==3:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Универсальный ноутбук',width/2-11,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4,style=styles.inverse)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==2:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Бюджетный ноутбук',width/2-9,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2,style=styles.inverse)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==1:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Дешёвый ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2,style=styles.inverse)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
    
    idx = 10001

    cls()
    settext('Какого вида вычисления в приоритете?',width/2-18,height/3)
    settext('Графическая карта даёт ощутимый прирост производительности и позволяет производить графические вычисления',width/2-53,height/3+(height/2-height/3)-3)
    settext('Процессор',width/2-5,height/2)
    settext('Графическая карта',width/2-9,height/2+2,style=styles.inverse)

    while True:
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
        if c == '\x1b[A'|b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B'|b'P': #DOWN ARROW
            idx+=1
        elif c == '\n': # ENTER KEY
            prior=idx%2
            break
        if idx%2==1:
            cls()
            settext('Какого вида вычисления в приоритете?',width/2-18,height/3)
            settext('Графическая карта даёт ощутимый прирост производительности и позволяет производить графические вычисления',width/2-53,height/3+(height/2-height/3)-3)
            settext('Процессор',width/2-5,height/2)
            settext('Графическая карта',width/2-9,height/2+2,style=styles.inverse)
        else:
            cls()
            settext('Какого вида вычисления в приоритете?',width/2-18,height/3)
            settext('Процессор позволяет производить базовые операции и является сердцем компьютера',width/2-39,height/3+(height/2-height/3)-3)
            settext('Процессор',width/2-5,height/2,style=styles.inverse)
            settext('Графическая карта',width/2-9,height/2+2)
    
    idx = 10001

    cls()
    settext('Требуется ли быстрая работа с файлами?',width/2-18,height/3)
    settext('Нет',width/2-1,height/2)
    settext('Да',width/2-1,height/2+2,style=styles.inverse)

    while True:
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
        if c == '\x1b[A'|b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B'|b'P': #DOWN ARROW
            idx+=1
        elif c == '\n': # ENTER KEY
            storage=idx%2
            break
        if idx%2==1:
            cls()
            settext('Требуется ли быстрая работа с файлами?',width/2-18,height/3)
            settext('Нет',width/2-1,height/2)
            settext('Да',width/2-1,height/2+2,style=styles.inverse)
        else:
            cls()
            settext('Требуется ли быстрая работа с файлами?',width/2-18,height/3)
            settext('Нет',width/2-1,height/2,style=styles.inverse)
            settext('Да',width/2-1,height/2+2)
    money -= 1
    if money < 0 : money = 3
    cls()
    settext('Вам подойдёт:',width/2-6,height/2-3,style=styles.bold)
    st = f'\x1b[1m{notebook_type[money]}\x1b[0m Процессор: {processor[money]} Видеокарта: {graphic_card[prior][money]} Тип ОЗУ: {ram_type[money]} Тип хранилища: {storage_type[storage][money]}'
    settext(st,width/2-len(st)/2,height/2)
    setoldflags()

def choose():
    cls()
    settext('Какой у вас бюджет?',width/2-10,height/3)
    settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
    settext('До 25.000',width/2-5,height/2)
    settext('25.000 - 40.000',width/2-8,height/2+2)
    settext('40.000 - 90.000',width/2-8,height/2+4)
    settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
    
    idx = 10004

    while True:
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
        if c == '\x1b[A'|b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B'|b'P': #DOWN ARROW
            idx+=1
        elif c == '\n': # ENTER KEY
            money=idx%4
            break
        if idx%4==0:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
        elif idx%4==3:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Универсальный ноутбук',width/2-11,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4,style=styles.inverse)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==2:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Бюджетный ноутбук',width/2-9,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2,style=styles.inverse)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==1:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Дешёвый ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2,style=styles.inverse)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
    
    indent = 0
    money -= 1
    if money < 0 : money = 3
    cls()
    settext('Вам подойдёт:',width/2-6,height/2-3,style=styles.bold)
    c = http.client.HTTPSConnection('www.citilink.ru')
    c.request('GET',f'/catalog/noutbuki/?sorting=price_asc&f={choose_processor[0][money]},{choose_graphic_card[0][money]},{choose_storage_type[0][money]},{choose_ram_type[0][money]}')
    r = c.getresponse()
    html = r.read().decode('UTF-8')
    result = re.findall(r'alt=".+',html)
    for x in result[:-1]:
        st = f'\x1b[1m{x[5:-1]}\x1b[0m Процессор: {choose_processor[1][money]} Видеокарта: {choose_graphic_card[1][money]} Тип ОЗУ: {choose_ram_type[1][money]} Тип хранилища: {choose_storage_type[1][money]}'
        settext(st,width/2-len(st)/2,height/2+indent)
        indent += 1
    setoldflags()

#### MAIN ####
cls()
setsign(style=styles.bold)
settext('Выход',width/3-5,height - height/4)
settext('Далее',(width-width/3)-5,height-height/4,style=styles.inverse)

idx = 10001

while True:
    c = getchar()
    if c == b'\x1b[D'|b'K': #LEFT ARROW
        idx-=1
    elif c == '\x1b[C'|b'M': #RIGHT ARROW
        idx+=1
    elif c == '\n'|b'\r': # ENTER KEY
        if idx%2==1:#Continue
            break
        else:#Exit
            cls()
            setoldflags()
            exit(0)
    if idx%2==1:
        settext('Выход',width/3-5,height - height/4)
        settext('Далее',(width-width/3)-5,height-height/4,style=styles.inverse)
    else:
        settext('Выход',width/3-5,height - height/4,style=styles.inverse)
        settext('Далее',(width-width/3)-5,height-height/4)

cls()
settext('Выберите режим',width/2-7,height/2,style=styles.bold)
settext('Подборка',width/3-5,height - height/4)
settext('Конструктор',(width-width/3)-5,height-height/4,style=styles.inverse)
settext('\x1b[1mКонструктор\x1b[0m - этот режим предназначен для создания своих параметров для ноутбука',width/2-40,height-height/5+2,style=styles.bold)

idx = 10001

while True:
    c = getchar()
    if c == b'\x1b[D'|b'K': #LEFT ARROW
        idx-=1
    elif c == '\x1b[C'|b'M': #RIGHT ARROW
        idx+=1
    elif c == '\n'|b'\r': # ENTER KEY
        if idx%2==1:#Constructor
            constructor()
            setoldflags()
        else:#Choose
            choose()
            setoldflags()
        break
    if idx%2==1:
        cls()
        settext('Выберите режим',width/2-7,height/2,style=styles.bold)
        settext('Подборка',width/3-5,height - height/4)
        settext('Конструктор',(width-width/3)-5,height-height/4,style=styles.inverse)
        settext('\x1b[1mКонструктор\x1b[0m - этот режим предназначен для создания своих параметров для ноутбука',width/2-40,height-height/5+2,style=styles.bold)
    else:
        cls()
        settext('Выберите режим',width/2-7,height/2,style=styles.bold)
        settext('Подборка',width/3-5,height - height/4,style=styles.inverse)
        settext('Конструктор',(width-width/3)-5,height-height/4)
        settext('\x1b[1mПодборка\x1b[0m - этот режим предназначен для выбора ноутбука из уже существующих моделей',width/2-42,height-height/5+2,style=styles.bold)