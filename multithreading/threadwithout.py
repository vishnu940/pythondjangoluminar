from threading import *

import time

class Myclass:
    def job(self):
        for i in range(10):
            time.sleep(2)
            print("child thread executing")

obj=Myclass()
t=Thread(target=obj.job)
t.start()
for i in range(10):
    time.sleep(2)
    print("main thread executing")