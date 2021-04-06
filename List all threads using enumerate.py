from threading import *
import time
def display():
    print(current_thread().name,'.....started')
    time.sleep(3)
    print(current_thread().name,'.....ended')

print('The number of active threads:',active_count())
t1=Thread(target=display,name='child 1')
t2=Thread(target=display,name='Child 2')
t1.start()
t2.start()
l=enumerate()
for t in l:
    print('Thread name:',t.name)
    print('Thread Identification Number',t.ident)
    print()

time.sleep(10)

