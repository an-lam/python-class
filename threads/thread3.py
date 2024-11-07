"""
Threads produce output to the log file.
"""
import logging
import threading
import time

def worker():
    logging.debug('+++>Starting')
    time.sleep(1)
    logging.debug('<+++Exiting')

def my_service():
    logging.debug('===>Starting')
    time.sleep(3)   # number of seconds
    logging.debug('<===Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    filename="thread3.log",
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()
print("\n Done")