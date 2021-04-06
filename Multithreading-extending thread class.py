from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print('Child thread')


t=MyThread()
t.start()
for i in range(5):
    print('Main thread')