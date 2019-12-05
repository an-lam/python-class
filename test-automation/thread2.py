import threading
import time
import random

def worker():
    print(threading.current_thread().getName(), '+++Starting')
    time.sleep(random.randint(1, 5))
    print(threading.current_thread().getName(), '+++Exiting')

def my_service():
    print(threading.current_thread().getName(), '===Starting')
    time.sleep(random.randint(1, 10))
    print(threading.current_thread().getName(), '===Exiting')

# Create threads
sthread = threading.Thread(name='my_service', target=my_service)
wthread = threading.Thread(name='worker1', target=worker)
wthread2 = threading.Thread(target=worker)  # use default name

# Start to run threads
sthread.start()
wthread.start()
wthread2.start()