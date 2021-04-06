from threading import *
def job():
    print('Executed by child thread')

t=Thread(target=job)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())