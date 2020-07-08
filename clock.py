import threading
import os
import datetime


def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def time():
    os.system('clear')
    t = datetime.datetime.now()
    s = t.strftime('%S')
    m = t.strftime('%M')
    h = t.strftime('%I')
    print(f'{h}:{m}:{s}')


setInterval(time,1)

