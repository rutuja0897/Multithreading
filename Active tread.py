from threading import *
import time
def display():
    print(current_thread().name,'......started')
    print()
    time.sleep(3)
    print(current_thread().name,'.......ended')

print('The number of active threads:',active_count())
t1=Thread(target=display,name='Child1')
t2=Thread(target=display,name='child2')
t3=Thread(target=display,name='child3')
t1.start()
t2.start()
t3.start()
print()
print('The number of active threads:',active_count())
time.sleep(10)
print('The number of active threads:',active_count())