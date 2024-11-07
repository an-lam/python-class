"""
Thread using subclass
"""
import threading
import logging
import time
import random

class MyThread(threading.Thread):
    """
    You must implement run() method
    """
    def run(self):
        # pass  # no op
        time.sleep(random.randint(1, 4))
        logging.debug('running')

# NOTE: no log filename.  The output goes to console
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThread()
    #t.run()    # blocking call
    t.start()

print("Done")
