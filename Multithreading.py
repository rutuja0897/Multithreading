from threading import *
def display():
    print('This code executed by Thread:',current_thread().getName())

t=Thread(target=display)
t.start()
print('This code executed by Thread:',current_thread().getName())