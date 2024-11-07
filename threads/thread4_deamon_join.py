import threading
import time
import logging

"""
https://pymotw.com/3/threading/

Up to this point, the example programs have implicitly waited to exit until all 
threads have completed their work. Sometimes programs spawn a thread as a daemon
 that runs without blocking the main program from exiting. Using daemon threads
  is useful for services where there may not be an easy way to interrupt the 
  thread, or where letting the thread die in the middle of its work does not 
  lose or corrupt data (for example, a thread that generates “heart beats” for
   a service monitoring tool). To mark a thread as a daemon, pass daemon=True 
   when constructing it or call its set_daemon() method with True. The default 
   is for threads to not be daemons.
"""
def daemon():
    """ Question: we're using logging.  Why does the output goes to
    screen?  """
    logging.debug('Daemon thread: Starting')
    time.sleep(2)
    logging.debug('Daemon thread: Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

""""
daemon=True: run thread as daemon so that it continues to run 
after main thread exits
"""
d = threading.Thread(name='daemon thread', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon thread', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
print("Main thread exits.")