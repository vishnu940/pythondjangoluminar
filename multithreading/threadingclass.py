from threading import *

class Mythread(Thread):
    def run(self):
        for i in range(10):
            print("child thread executing")


obj=Mythread()
obj.start()
for i in range(10):
    print("Main thread executing")
