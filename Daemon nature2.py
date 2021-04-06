from threading import *
import time
def job1():
    print('executed by t1')
    t2=Thread(target=job2)
    print('t2 is Daemon:',t2.isDaemon())
    t2.start()

def job2():
    print('executed by t2')

t1=Thread(target=job1)
t1.setDaemon(True)
print('t1 is Daemon:',t1.isDaemon())
t1.start()
time.sleep(10)
