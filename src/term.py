'''
Header file for work with terminal
'''

from enum import IntEnum

#enumeration of colors
class colors(IntEnum):
    white = 37,
    yellow = 33,
    green = 32,
    blue = 34,
    cyan = 36,
    red = 31,
    magenta = 35,
    black = 30

#enumeration of styles
class styles(IntEnum):
    none = 0,
    bold = 1,
    underline = 4,
    inverse = 7

#output function with styles
def out(text,color,style,lst='\n'):
    print('\033[%d;%dm' % (style,color) + text + '\033[0m',end=lst)