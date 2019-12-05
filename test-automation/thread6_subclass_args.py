"""
Thread subclass with arguments
"""
import threading
import logging
import random
import time

class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 myargs=(), mykwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = myargs
        self.kwargs = mykwargs

    def run(self):
        time.sleep(random.randint(1, 50) / 10)
        logging.debug('running with %s and %s',
                      self.args, self.kwargs)

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(1, 5):
    t = MyThreadWithArgs(myargs=(i), mykwargs={'a': 'A', 'b': 'B'})
    t.start()