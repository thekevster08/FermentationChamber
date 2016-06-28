from ConfigParser import SafeConfigParser
import threading
import Discrete
import time

class Controller(threading.Thread):
    config = SafeConfigParser()
    P = None
    num = 55 #this needs to become reading the temperature

    def __init__(self, threadID, name, counter):
        global P
        P = Discrete.Discrete()
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.mutex = threading.Lock()
        self.paused = False
        self.start()
        self.pause()

    def pause(self):
        if (not self.paused):
            self.mutex.acquire()
            self.paused = True

    def unpause(self):
        self.mutex.release()
        self.paused = False

    def run(self):
        global P
        print "starting" + self.name
        while True:
            self.mutex.acquire()
            # self.config.read('config.ini')
            # print self.config.get('main', 'counterOn')
            print self.num
            P.update(self.num) #this needs to become reading hte tmeperature
            
            time.sleep(1)
            self.mutex.release()
