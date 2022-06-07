'''
Program wich helps you choose notebook for work with mathemathic packets

Author: Artem Vanty GitHub:vantyartem
'''

import os,sys
import http.client
import re
if os.name == 'nt':
    from msvcrt import getch
else:
    import termios, fcntl
    import select

from term import *
from vars import *


#if unix system then include this code
if os.name != 'nt':
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd) # get current flags
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL) # still get current flags
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK) # set flags with nonblock flag

    newattr = termios.tcgetattr(fd) # get current flags again
    newattr[3] = newattr[3] & ~termios.ICANON # idk exclude icanon flag
    newattr[3] = newattr[3] & ~termios.ECHO # exclude echo flag
    termios.tcsetattr(fd, termios.TCSANOW, newattr) # set flags
#set new flags 
def setnewflags():
    if os.name != 'nt':
        termios.tcsetattr(fd, termios.TCSANOW, newattr) # set flags
#set old flags
def setoldflags():
    if os.name != 'nt':
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
#get char by keyboard
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
#set sign on the screen
def setsign(color=colors.white,style=styles.none,lst='\n'):
    i = 0
    for x in sign:
        settext(x,width/2 - len(x)/2,height/3 - len(sign)/2 + i,color,style,lst)
        i+=1
#Constructor page
def constructor():
    cls()#clear screen
    settext('Какой у вас бюджет?',width/2-10,height/3)
    settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
    settext('До 25.000',width/2-5,height/2)
    settext('25.000 - 40.000',width/2-8,height/2+2)
    settext('40.000 - 90.000',width/2-8,height/2+4)
    settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
    
    idx = 10004 #index of cursor

    while True:
        
        c = getchar()
        if c == '\x1b[A' or c == b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B' or c == b'P': #DOWN ARROW
            idx+=1
        elif c == '\n' or c == b'\r': # ENTER KEY
            money=idx%4
            break
        if idx%4==0:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
        elif idx%4==3:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Универсальный ноутбук',width/2-11,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4,style=styles.inverse)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==2:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Бюджетный ноутбук',width/2-9,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2,style=styles.inverse)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==1:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Дешёвый ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2,style=styles.inverse)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
    
    idx = 10001 #index of cursor

    cls()#clear screen
    settext('Какого вида вычисления в приоритете?',width/2-18,height/3)
    settext('Графическая карта даёт ощутимый прирост производительности и позволяет производить графические вычисления',width/2-53,height/3+(height/2-height/3)-3)
    settext('Процессор',width/2-5,height/2)
    settext('Графическая карта',width/2-9,height/2+2,style=styles.inverse)

    while True:
        
        c = getchar()
        if c == '\x1b[A' or c == b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B' or c == b'P': #DOWN ARROW
            idx+=1
        elif c == '\n' or c == b'\r': # ENTER KEY
            prior=idx%2
            break
        if idx%2==1:
            cls()#clear screen
            settext('Какого вида вычисления в приоритете?',width/2-18,height/3)
            settext('Графическая карта даёт ощутимый прирост производительности и позволяет производить графические вычисления',width/2-53,height/3+(height/2-height/3)-3)
            settext('Процессор',width/2-5,height/2)
            settext('Графическая карта',width/2-9,height/2+2,style=styles.inverse)
        else:
            cls()#clear screen
            settext('Какого вида вычисления в приоритете?',width/2-18,height/3)
            settext('Процессор позволяет производить базовые операции и является сердцем компьютера',width/2-39,height/3+(height/2-height/3)-3)
            settext('Процессор',width/2-5,height/2,style=styles.inverse)
            settext('Графическая карта',width/2-9,height/2+2)
    
    idx = 10001 #index of cursor

    cls()#clear screen
    settext('Требуется ли быстрая работа с файлами?',width/2-18,height/3)
    settext('Нет',width/2-1,height/2)
    settext('Да',width/2-1,height/2+2,style=styles.inverse)

    while True:
        
        c = getchar()
        if c == '\x1b[A' or c == b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B' or c == b'P': #DOWN ARROW
            idx+=1
        elif c == '\n' or c == b'\r': # ENTER KEY
            storage=idx%2
            break
        if idx%2==1:
            cls()#clear screen
            settext('Требуется ли быстрая работа с файлами?',width/2-18,height/3)
            settext('Нет',width/2-1,height/2)
            settext('Да',width/2-1,height/2+2,style=styles.inverse)
        else:
            cls()#clear screen
            settext('Требуется ли быстрая работа с файлами?',width/2-18,height/3)
            settext('Нет',width/2-1,height/2,style=styles.inverse)
            settext('Да',width/2-1,height/2+2)
    money -= 1
    if money < 0 : money = 3
    cls()#clear screen
    settext('Вам подойдёт:',width/2-6,height/2-3,style=styles.bold)
    st = f'\x1b[1m{notebook_type[money]}\x1b[0m Процессор: {processor[money]} Видеокарта: {graphic_card[prior][money]} Тип ОЗУ: {ram_type[money]} Тип хранилища: {storage_type[storage][money]}'
    settext(st,width/2-len(st)/2,height/2)
    setoldflags()#set old flags
#Choose page
def choose():
    cls()#clear screen
    settext('Какой у вас бюджет?',width/2-10,height/3)
    settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
    settext('До 25.000',width/2-5,height/2)
    settext('25.000 - 40.000',width/2-8,height/2+2)
    settext('40.000 - 90.000',width/2-8,height/2+4)
    settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
    
    idx = 10004 #index of cursor

    while True:
        
        c = getchar()
        if c == '\x1b[A' or c == b'H': #UP ARROW
            idx-=1
        elif c == '\x1b[B' or c == b'P': #DOWN ARROW
            idx+=1
        elif c == '\n' or c == b'\r': # ENTER KEY
            money=idx%4
            break
        if idx%4==0:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6,style=styles.inverse)
        elif idx%4==3:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Универсальный ноутбук',width/2-11,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4,style=styles.inverse)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==2:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Бюджетный ноутбук',width/2-9,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2)
            settext('25.000 - 40.000',width/2-8,height/2+2,style=styles.inverse)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
        elif idx%4==1:
            cls()#clear screen
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Дешёвый ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 25.000',width/2-5,height/2,style=styles.inverse)
            settext('25.000 - 40.000',width/2-8,height/2+2)
            settext('40.000 - 90.000',width/2-8,height/2+4)
            settext('90.000+',width/2-4,height/2+6)
    
    indent = 0
    money -= 1
    if money < 0 : money = 3
    cls()#clear screen
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
    setoldflags()#set old flags

#### MAIN ####
cls()#clear screen
setsign(style=styles.bold)#set sign on screen
settext('Выход',width/3-5,height - height/4)#set exit text
settext('Далее',(width-width/3)-5,height-height/4,style=styles.inverse)#set next text

idx = 10001 #index of cursor

while True:
    c = getchar()
    if c == '\x1b[D' or c == b'K': #LEFT ARROW
        idx-=1
    elif c == '\x1b[C' or c == b'M': #RIGHT ARROW
        idx+=1
    elif c == '\n' or c == b'\r': # ENTER KEY
        if idx%2==1:#Continue
            break
        else:#Exit
            cls()#clear screen
            setoldflags()#set old flags
            exit(0)#exit from program
    if idx%2==1:
        settext('Выход',width/3-5,height - height/4)
        settext('Далее',(width-width/3)-5,height-height/4,style=styles.inverse)
    else:
        settext('Выход',width/3-5,height - height/4,style=styles.inverse)
        settext('Далее',(width-width/3)-5,height-height/4)

cls()#clear screen
settext('Выберите режим',width/2-7,height/2,style=styles.bold)
settext('Подборка',width/3-5,height - height/4)
settext('Конструктор',(width-width/3)-5,height-height/4,style=styles.inverse)
settext('\x1b[1mКонструктор\x1b[0m - этот режим предназначен для создания своих параметров для ноутбука',width/2-40,height-height/5+2,style=styles.bold)

idx = 10001 #index of cursor

while True:
    c = getchar()
    if c == '\x1b[D' or c == b'K': #LEFT ARROW
        idx-=1
    elif c == '\x1b[C' or c == b'M': #RIGHT ARROW
        idx+=1
    elif c == '\n' or c == b'\r': # ENTER KEY
        if idx%2==1:#Constructor
            constructor()#constructor page
            setoldflags()#set old flags
        else:#Choose
            choose()#choose page
            setoldflags()#set old flags
        break
    if idx%2==1:
        cls()#clear screen
        settext('Выберите режим',width/2-7,height/2,style=styles.bold)
        settext('Подборка',width/3-5,height - height/4)
        settext('Конструктор',(width-width/3)-5,height-height/4,style=styles.inverse)
        settext('\x1b[1mКонструктор\x1b[0m - этот режим предназначен для создания своих параметров для ноутбука',width/2-40,height-height/5+2,style=styles.bold)
    else:
        cls()#clear screen
        settext('Выберите режим',width/2-7,height/2,style=styles.bold)
        settext('Подборка',width/3-5,height - height/4,style=styles.inverse)
        settext('Конструктор',(width-width/3)-5,height-height/4)
        settext('\x1b[1mПодборка\x1b[0m - этот режим предназначен для выбора ноутбука из уже существующих моделей',width/2-42,height-height/5+2,style=styles.bold)