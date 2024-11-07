"""
Wait for all threads to finish
"""
import random
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def worker():
    """thread worker function"""
    pause = random.randint(1, 50) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)     # unit in seconds
    logging.debug('ending')

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    # main_thread is also in the list, skip it to avoid deadlock. Why?
    if t is main_thread:
        continue
    #    break

    logging.debug('joining %s', t.getName())
    if t.isAlive():
        t.join()
