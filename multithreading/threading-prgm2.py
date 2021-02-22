import threading
import time

def display():
    for i in range(1,10):
        time.sleep(2)
        print("child thread executing")
    print(threading.currentThread().getName())


t=threading.Thread(target=display)
t.start()
begintime=time.time()
print("begin time:",begintime)
t.join()
for i in range(1,10):
    time.sleep(2)
    print("main threading executing")
print(threading.currentThread().getName())

endtime=time.time()
totaltime=endtime-begintime
print("total time taken:",totaltime)