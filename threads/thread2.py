import threading
import time
import random

""" GIL: global interpreter lock """

def worker():
    print(threading.current_thread().getName(), '+++>Starting-worker')
    time.sleep(random.randint(1, 5))
    print(threading.current_thread().getName(), '<+++Exiting-worker')

def my_service():
    print(threading.current_thread().getName(), '===>Starting-my_service')
    time.sleep(random.randint(5, 10))
    print(threading.current_thread().getName(), '<===Exiting-my_service')

# Create threads
# target=function name to run in thread
sthread = threading.Thread(name='my_service', target=my_service)
wthread = threading.Thread(name='worker1', target=worker)
wthread2 = threading.Thread(target=worker)  # use default name

# Start to run threads
sthread.start()
wthread.start()
wthread2.start()

print("\n All threads done.")
