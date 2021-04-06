from threading import *
import time
def display():
    print(current_thread().name,'.....started')
    time.sleep(6)
    print(current_thread().name,'.....ended')

t=Thread(target=display,name='Child 1')
t2=Thread(target=display,name='Child 2')
t.start()
t2.start()
print(t.name,'isAlive:',t.isAlive())
print(t2.name,'isALive:',t2.isAlive())
time.sleep(10)
print(t.name,'isAlive',t.isAlive())
print(t2.name,'isAlive',t2.isAlive())

