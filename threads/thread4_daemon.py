"""
Daemon vs. non-daemon threads
"""
import threading
import time
import logging

def daemon():
    logging.debug('+++> Daemon: Starting')
    print("+++ Daemon: Starting")
    #time.sleep(20)
    while True:
        time.sleep(10)
        logging.debug("in while loop")

    logging.debug('+++ Daemon: Exiting')
    print("+++ Daemon: Exiting")

def non_daemon():
    logging.debug('=== Non-daemon: Starting')
    print("=== Non-daemon\n")

logging.basicConfig(
    level=logging.DEBUG,
    filename="thread4.log",
    format='(%(threadName)-10s) %(message)s',
)

d_thread = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

"""  Note: In the output, the daemon thread has not printed "Exiting"
  because it's still running while the main thread already exits.  Then
  the daemon thread is killed.
"""
d_thread.start()
t.start()

print("Main thread exits.")
