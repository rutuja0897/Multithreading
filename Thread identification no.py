from threading import *
def test():
    print('child thread')

t=Thread(target=test)
t.start()
print('Main Thread Identification Number:',current_thread().ident)
print('child thread identification number:',t.ident)