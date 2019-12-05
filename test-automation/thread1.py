"""
Thread tutorial:
https://pymotw.com/3/threading/
"""
import threading
import time

def worker(num):
    """thread worker function"""
    print("Worker thread: {}".format(num))

threads = []
for i in range(1, 5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    time.sleep(2)
    t.start()
    print("Main: i = {}".format(i))