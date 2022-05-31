import os,sys,string

import termios, fcntl
import select
from time import sleep

import types
import vars
from term import *
import tui



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

money=0
prior=0
storage=0

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def settext(text,x,y,color=colors.white,style=styles.none,lst='\n'):
    out("\033[%d;%dH" % (y,x) + text,color,style,lst)

def setsign(color=colors.white,style=styles.none,lst='\n'):
    i = 0
    for x in sign:
        settext(x,width/2 - len(x)/2,height/3 - len(sign)/2 + i,color,style,lst)
        i+=1

def constructor():
    cls()
    settext('Какой у вас бюджет?',width/2-10,height/3)
    settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
    settext('До 15.000',width/2-5,height/2)
    settext('15.000 - 30.000',width/2-8,height/2+2)
    settext('30.000 - 70.000',width/2-8,height/2+4)
    settext('70.000+',width/2-4,height/2+6,style=styles.inverse)
    
    idx = 10004

    while True:
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
        if c == '\033[A': #UP ARROW
            idx-=1
        elif c == '\033[B': #DOWN ARROW
            idx+=1
        elif c == '\n': # ENTER KEY
            money=idx%4
            break
        if idx%4==0:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Мощный ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 15.000',width/2-5,height/2)
            settext('15.000 - 30.000',width/2-8,height/2+2)
            settext('30.000 - 70.000',width/2-8,height/2+4)
            settext('70.000+',width/2-4,height/2+6,style=styles.inverse)
        elif idx%4==3:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Универсальный ноутбук',width/2-11,height/3+(height/2-height/3)-3)
            settext('До 15.000',width/2-5,height/2)
            settext('15.000 - 30.000',width/2-8,height/2+2)
            settext('30.000 - 70.000',width/2-8,height/2+4,style=styles.inverse)
            settext('70.000+',width/2-4,height/2+6)
        elif idx%4==2:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Бюджетный ноутбук',width/2-9,height/3+(height/2-height/3)-3)
            settext('До 15.000',width/2-5,height/2)
            settext('15.000 - 30.000',width/2-8,height/2+2,style=styles.inverse)
            settext('30.000 - 70.000',width/2-8,height/2+4)
            settext('70.000+',width/2-4,height/2+6)
        elif idx%4==1:
            cls()
            settext('Какой у вас бюджет?',width/2-10,height/3)
            settext('Дешёвый ноутбук',width/2-8,height/3+(height/2-height/3)-3)
            settext('До 15.000',width/2-5,height/2,style=styles.inverse)
            settext('15.000 - 30.000',width/2-8,height/2+2)
            settext('30.000 - 70.000',width/2-8,height/2+4)
            settext('70.000+',width/2-4,height/2+6)
    
    idx = 10001

    cls()
    settext('Какого вида вычисления в приоритете?',width/2-18,height/3)
    settext('Графическая карта даёт ощутимый прирост производительности и позволяет производить графические вычисления',width/2-53,height/3+(height/2-height/3)-3)
    settext('Процессор',width/2-5,height/2)
    settext('Графическая карта',width/2-9,height/2+2,style=styles.inverse)

    while True:
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
        if c == '\033[A': #UP ARROW
            idx-=1
        elif c == '\033[B': #DOWN ARROW
            idx+=1
        elif c == '\n': # ENTER KEY
            money=idx%2
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
        if c == '\033[A': #UP ARROW
            idx-=1
        elif c == '\033[B': #DOWN ARROW
            idx+=1
        elif c == '\n': # ENTER KEY
            io=idx%2
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

#### MAIN ####
cls()
setsign(style=styles.bold)
settext('Выход',width/3-5,height - height/4)
settext('Далее',(width-width/3)-5,height-height/4,style=styles.inverse)

idx = 10001

while True:
    inp, outp, err = select.select([sys.stdin], [], [])
    c = sys.stdin.read()
    if c == '\033[D': #LEFT ARROW
        idx-=1
    elif c == '\033[C': #RIGHT ARROW
        idx+=1
    elif c == '\n': # ENTER KEY
        if idx%2==1:#Continue
            break
        else:#Exit
            setoldflags()
            exit(0)
    if idx%2==1:
        settext('Выход',width/3-5,height - height/4)
        settext('Далее',(width-width/3)-5,height-height/4,style=styles.inverse)
    else:
        settext('Выход',width/3-5,height - height/4,style=styles.inverse)
        settext('Далее',(width-width/3)-5,height-height/4)

cls()
settext('Выберите язык / Choose language',width/2-16,height/2,style=styles.bold)
settext('English',width/3-5,height - height/4)
settext('Русский',(width-width/3)-5,height-height/4,style=styles.inverse)

idx = 10001

while True:
    inp, outp, err = select.select([sys.stdin], [], [])
    c = sys.stdin.read()
    if c == '\033[D': #LEFT ARROW
        idx-=1
    elif c == '\033[C': #RIGHT ARROW
        idx+=1
    elif c == '\n': # ENTER KEY
        if idx%2==1:#Russian
            #setoldflags()
            break
        else:#English
            #setoldflags()
            break
    if idx%2==1:
        settext('English',width/3-5,height - height/4)
        settext('Русский',(width-width/3)-5,height-height/4,style=styles.inverse)
    else:
        settext('English',width/3-5,height - height/4,style=styles.inverse)
        settext('Русский',(width-width/3)-5,height-height/4)

cls()
settext('Выберите режим',width/2-7,height/2,style=styles.bold)
settext('Подборка',width/3-5,height - height/4)
settext('Конструктор',(width-width/3)-5,height-height/4,style=styles.inverse)
settext('\033[1mКонструктор\033[0m - этот режим предназначен для создания своих параметров для ноутбука',width/2-40,height-height/5+2,style=styles.bold)

idx = 10001

while True:
    inp, outp, err = select.select([sys.stdin], [], [])
    c = sys.stdin.read()
    if c == '\033[D': #LEFT ARROW
        idx-=1
    elif c == '\033[C': #RIGHT ARROW
        idx+=1
    elif c == '\n': # ENTER KEY
        if idx%2==1:#Constructor
            constructor()
            setoldflags()
            break
        else:#Choose
            setoldflags()
    if idx%2==1:
        cls()
        settext('Выберите режим',width/2-7,height/2,style=styles.bold)
        settext('Подборка',width/3-5,height - height/4)
        settext('Конструктор',(width-width/3)-5,height-height/4,style=styles.inverse)
        settext('\033[1mКонструктор\033[0m - этот режим предназначен для создания своих параметров для ноутбука',width/2-40,height-height/5+2,style=styles.bold)
    else:
        cls()
        settext('Выберите режим',width/2-7,height/2,style=styles.bold)
        settext('Подборка',width/3-5,height - height/4,style=styles.inverse)
        settext('Конструктор',(width-width/3)-5,height-height/4)
        settext('\033[1mПодборка\033[0m - этот режим предназначен для выбора ноутбука из уже существующих моделей',width/2-42,height-height/5+2,style=styles.bold)