"""import time
from threading import Thread
def sleepFun(x):
    print("Thread",x,"is going to sleep for 5 seconds.")
    time.sleep(5)
    print("Thread",x,"is active now")

th=Thread(target=sleepFun, args=(1, ))
th.start
sleepFun(1)
time.sleep(1)
#sleepFun(1)
print("Hello i am exectuing parallel to thread")
"""
"""
import time
from threading import Thread
def calculation():
    a=10
    b=20
    res=a+b
    return res
def sleepFun(x):
    print("Thread",x,"is going to sleep for 20 seconds.")
    time.sleep(20)
    print("Thread",x,"is active now")
for i in range(1,11):
    th=Thread(target=sleepFun,args=(i, ))
    th.start()
    time.sleep(1)
res=calculation()
print("Res=",res)
"""

import time
from threading import Thread
def eventhrd(x,y):
    print("Even thread executing")
    time.sleep(5)
    print("ex is:",x)
def oddthrd(y):
    print("Odd thread executing")
    time.sleep(10)
    print("ox:",y)
th= Thread(target=eventhrd, args=(1,4))
th.start()
time.sleep(1)
th1=Thread (target=oddthrd, args=(1,))
th1.start()
time.sleep(1)







