from threading import *
import time
def job():
    for i in range(10):
        print('Lazy Thread')
        time.sleep(3)
t=Thread(target=job)
t.setDaemon(True)
t.start()
time.sleep(10)
print('End of main Thread')
