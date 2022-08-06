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
from lang import *
lang = 0
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
    out("\x1b[%d;%dH" % (y,x-len(text)/2) + text,color,style,lst)
#set sign on the screen
def setsign(color=colors.white,style=styles.none,lst='\n'):
    i = 0
    for x in sign[lang]:
        settext(x,width/2,height/3 - len(sign[lang])/2 + i,color,style,lst)
        i+=1
#Constructor page
def constructor():
    cls()#clear screen
    settext(budget[lang],width/2,height/3)
    settext(powerful_notebook[lang],width/2,height/3+(height/2-height/3)-3)
    settext(twenty_five[lang],width/2,height/2)
    settext('25.000 - 40.000',width/2,height/2+2)
    settext('40.000 - 90.000',width/2,height/2+4)
    settext('90.000+',width/2,height/2+6,style=styles.inverse)
    
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
            settext(budget[lang],width/2,height/3)
            settext(powerful_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2)
            settext('25.000 - 40.000',width/2,height/2+2)
            settext('40.000 - 90.000',width/2,height/2+4)
            settext('90.000+',width/2,height/2+6,style=styles.inverse)
        elif idx%4==3:
            cls()#clear screen
            settext(budget[lang],width/2,height/3)
            settext(universal_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2)
            settext('25.000 - 40.000',width/2,height/2+2)
            settext('40.000 - 90.000',width/2,height/2+4,style=styles.inverse)
            settext('90.000+',width/2,height/2+6)
        elif idx%4==2:
            cls()#clear screen
            settext(budget[lang],width/2,height/3)
            settext(budget_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2)
            settext('25.000 - 40.000',width/2,height/2+2,style=styles.inverse)
            settext('40.000 - 90.000',width/2,height/2+4)
            settext('90.000+',width/2,height/2+6)
        elif idx%4==1:
            cls()#clear screen
            settext(budget[lang],width/2,height/3)
            settext(cheap_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2,style=styles.inverse)
            settext('25.000 - 40.000',width/2,height/2+2)
            settext('40.000 - 90.000',width/2,height/2+4)
            settext('90.000+',width/2,height/2+6)
    
    idx = 10001 #index of cursor

    cls()#clear screen
    settext(ops_prior[lang],width/2,height/3)
    settext(gc[lang],width/2,height/3+(height/2-height/3)-3)
    settext(proc[lang],width/2,height/2)
    settext(gh[lang],width/2,height/2+2,style=styles.inverse)

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
            settext(ops_prior[lang],width/2,height/3)
            settext(gc[lang],width/2,height/3+(height/2-height/3)-3)
            settext(proc[lang],width/2,height/2)
            settext(gh[lang],width/2,height/2+2,style=styles.inverse)
        else:
            cls()#clear screen
            settext(ops_prior[lang],width/2,height/3)
            settext(procc[lang],width/2,height/3+(height/2-height/3)-3)
            settext(proc[lang],width/2,height/2,style=styles.inverse)
            settext(gh[lang],width/2,height/2+2)
    
    idx = 10001 #index of cursor

    cls()#clear screen
    settext(fast_files[lang],width/2,height/3)
    settext(yes[lang],width/2,height/2)
    settext(no[lang],width/2,height/2+2,style=styles.inverse)

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
            settext(fast_files[lang],width/2,height/3)
            settext(yes[lang],width/2,height/2)
            settext(no[lang],width/2,height/2+2,style=styles.inverse)
        else:
            cls()#clear screen
            settext(fast_files[lang],width/2,height/3)
            settext(yes[lang],width/2,height/2,style=styles.inverse)
            settext(no[lang],width/2,height/2+2)
    money -= 1
    if money < 0 : money = 3
    cls()#clear screen
    settext(suit[lang],width/2,height/2-3,style=styles.bold)
    st = f'\x1b[1m{notebook_type[lang][money]}\x1b[0m {prc[lang]}: {processor[money]} {graphic_c[lang]}: {graphic_card[prior][money]} {ram_t[lang]}: {ram_type[money]} {storage_t[lang]}: {storage_type[storage][money]}'
    settext(st,width/2,height/2)
    setoldflags()#set old flags
#Choose page
def choose():
    cls()#clear screen
    settext(budget[lang],width/2,height/3)
    settext(powerful_notebook[lang],width/2,height/3+(height/2-height/3)-3)
    settext(twenty_five[lang],width/2,height/2)
    settext('25.000 - 40.000',width/2,height/2+2)
    settext('40.000 - 90.000',width/2,height/2+4)
    settext('90.000+',width/2,height/2+6,style=styles.inverse)
    
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
            settext(budget[lang],width/2,height/3)
            settext(powerful_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2)
            settext('25.000 - 40.000',width/2,height/2+2)
            settext('40.000 - 90.000',width/2,height/2+4)
            settext('90.000+',width/2,height/2+6,style=styles.inverse)
        elif idx%4==3:
            cls()#clear screen
            settext(budget[lang],width/2,height/3)
            settext(universal_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2)
            settext('25.000 - 40.000',width/2,height/2+2)
            settext('40.000 - 90.000',width/2,height/2+4,style=styles.inverse)
            settext('90.000+',width/2,height/2+6)
        elif idx%4==2:
            cls()#clear screen
            settext(budget[lang],width/2,height/3)
            settext(budget_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2)
            settext('25.000 - 40.000',width/2,height/2+2,style=styles.inverse)
            settext('40.000 - 90.000',width/2,height/2+4)
            settext('90.000+',width/2,height/2+6)
        elif idx%4==1:
            cls()#clear screen
            settext(budget[lang],width/2,height/3)
            settext(cheap_notebook[lang],width/2,height/3+(height/2-height/3)-3)
            settext(twenty_five[lang],width/2,height/2,style=styles.inverse)
            settext('25.000 - 40.000',width/2,height/2+2)
            settext('40.000 - 90.000',width/2,height/2+4)
            settext('90.000+',width/2,height/2+6)
    
    indent = 0
    money -= 1
    if money < 0 : money = 3
    cls()#clear screen
    settext(suit[lang],width/2,height/2-3,style=styles.bold)
    c = http.client.HTTPSConnection('www.citilink.ru')
    c.request('GET',f'/catalog/noutbuki/?sorting=price_asc&f={choose_processor[0][money]},{choose_graphic_card[0][money]},{choose_storage_type[0][money]},{choose_ram_type[0][money]}')
    r = c.getresponse()
    html = r.read().decode('UTF-8')
    result = re.findall(r'alt=".+',html)
    for x in result[:-1]:
        st = f'\x1b[1m{x[5:-1]}\x1b[0m Процессор: {choose_processor[1][money]} Видеокарта: {choose_graphic_card[1][money]} Тип ОЗУ: {choose_ram_type[1][money]} Тип хранилища: {choose_storage_type[1][money]}'
        settext(st,width/2,height/2+indent)
        indent += 1
    setoldflags()#set old flags

#### MAIN ####
cls()
settext('Select language/Выберите язык',width/2,height/2,style=styles.bold)
settext('English',width/3,height - height/4)#set exit text
settext('Русский',width-width/3,height-height/4,style=styles.inverse)#set next text

idx = 10001 #index of cursor

while True:
    c = getchar()
    if c == '\x1b[D' or c == b'K': #LEFT ARROW
        idx-=1
    elif c == '\x1b[C' or c == b'M': #RIGHT ARROW
        idx+=1
    elif c == '\n' or c == b'\r': # ENTER KEY
        if idx%2==1:#Continue
            lang = 0
            break
        else:#Exit
            lang = 1
            break
    if idx%2==1:
        settext('English',width/3,height - height/4)
        settext('Русский',(width-width/3),height-height/4,style=styles.inverse)
    else:
        settext('English',width/3,height - height/4,style=styles.inverse)
        settext('Русский',(width-width/3),height-height/4)

cls()#clear screen
setsign(style=styles.bold)#set sign on screen
settext(exitt[lang],width/3,height - height/4)#set exit text
settext(nextt[lang],width-width/3,height-height/4,style=styles.inverse)#set next text

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
        settext(exitt[lang],width/3,height - height/4)#set exit text
        settext(nextt[lang],width-width/3,height-height/4,style=styles.inverse)#set next text
    else:
        settext(exitt[lang],width/3,height - height/4,style=styles.inverse)#set exit text
        settext(nextt[lang],width-width/3,height-height/4)#set next text

cls()#clear screen
settext(select_mode[lang],width/2,height/2,style=styles.bold)
settext(chose[lang],width/3,height - height/4)
settext(construct[lang],(width-width/3),height-height/4,style=styles.inverse)
settext(construct_desc[lang],width/2,height-height/5+2)

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
        settext(select_mode[lang],width/2,height/2,style=styles.bold)
        settext(chose[lang],width/3,height - height/4)
        settext(construct[lang],(width-width/3),height-height/4,style=styles.inverse)
        settext(construct_desc[lang],width/2,height-height/5+2)
    else:
        cls()#clear screen
        settext(select_mode[lang],width/2,height/2,style=styles.bold)
        settext(chose[lang],width/3,height - height/4,style=styles.inverse)
        settext(construct[lang],(width-width/3),height-height/4)
        settext(chose_desc[lang],width/2,height-height/5+2)