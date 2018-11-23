#--*-- coding:utf-8 --*--
import time
import threading

class Server(object):

    def __init__(self):
        pass

    def start(self,intervals):
        while True:
            time.sleep(intervals)
            print('server normal start')

    def init(self):
        print('server start')
        t=threading.Thread(target=self.start,args=(10,))
        t.start()

def main():
    s=Server()
    s.init()

if __name__ == '__main__':
    main()





