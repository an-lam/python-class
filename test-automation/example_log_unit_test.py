"""
   Unit test example with logging rotation file
"""
import unittest
import sys
import os

import glob
import logging
import logging.handlers

from ssh_connection import SSHconnection

"""
Setting message level:
   Level      Value
   CRITICAL   50
   ERROR      40
   WARNING    30
   INFO       20
   DEBUG      10
   UNSET      0
The log message is only emitted if the handler and logger are configured to 
emit messages of that level or higher. For example, if a message is CRITICAL,
and the logger is set to ERROR, the message is emitted (50 > 40).
If a message is a WARNING, and the logger is set to produce only messages set to 
ERROR, the message is not emitted (30 < 40).
"""
LOG_FILENAME = 'logging_example6.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    #level=logging.INFO,
    #level=logging.DEBUG,
    level=logging.ERROR,
)

#hostname = '10.203.35.153'
hostname = '10.0.0.21'
port = 22
username = 'pi'
password = 'anlam2018'
# password = 'lam2018'
#username = 'pi'
#password = 'raspberry'

class Mytest(unittest.TestCase):
    @classmethod
    def setup_class(cls):   # cls is similar to self
        """
        This code will be run before any test case
        """
        print("setup_class is called for class: {}".format(cls.__name__))

        # Getting a logger instance
        cls.log = logging.getLogger(__name__)
        #cls.log = logging.getLogger()  # get default logger "ROOT"
        cls.log.info("Calling Mytest:setup_class")

        # Add the log message handler to the logger
        handler = logging.handlers.RotatingFileHandler(
                                LOG_FILENAME,
                                maxBytes = 5000,    # max size of log file
                                backupCount = 3,   # how many log files to keep
                                )
        cls.log.addHandler(handler)
        # Create SSH Client connection to test device
        cls.ssh_con = SSHconnection(hostname, username, password, port)

    @classmethod
    def teardown_class(cls):
        """
        This code will be run after completing all test cases
        """
        print("teardown_class is called for class: {}".format(cls.__name__))

        # Close SSH Client connection to test device
        cls.ssh_con.close()

    def setup_method(self, test_method):
        """ run this code at the beginning of each test: test_xxx """
        print("setup_method is called. test_method: {}".format(test_method))
        self.log.debug("This goes to log file: 'setup_method'")

    def teardown_method(self, test_method):
        """ run this code at the end of each test: test_xxx """
        # Should check for coredumps and panic
        print("teardown_method is called. test_method: {}".format(test_method))
        self.log.debug("This goes to log file: 'teardown_method'")

    def test_ls(self):
        print("test_ls is called.")
        # NOTE: ssh_con was created in setup_class by
        #   cls.ssh_con
        # but referred here as self.ssh_con
        out, err = self.ssh_con.execute_command("ls /home/pi")
        print("output from NFS: " + out)
        self.log.info("This goes to log file: 'test_ls'")

    def test_get_file(self):
        print("test_get_file is called.")
        self.log.info("This goes to log file: 'test_get_file'")

if __name__ == '__main__':
    unittest.main()


# C:\Users\lama2\AppData\Local\Programs\Python\Python36-32\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.4\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/lama2/PycharmProjects/test-automation/example_log_unit_test.py
# Testing started at 4:47 PM ...
# Launching py.test with arguments C:/Users/lama2/PycharmProjects/test-automation/example_log_unit_test.py in C:\Users\lama2\PycharmProjects\test-automation
# ============================= test session starts =============================
# platform win32 -- Python 3.6.1, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
# rootdir: C:\Users\lama2\PycharmProjects\test-automation, inifile:
# collected 2 items
# example_log_unit_test.py setup_class is called for class:Mytest
# setup_method is called. test_method: <bound method Mytest.test_get_file of <example_log_unit_test.Mytest testMethod=test_get_file>>
# .test_get_file is called.
# teardown_method is called. test_method: <bound method Mytest.test_get_file of <example_log_unit_test.Mytest testMethod=test_get_file>>
# setup_method is called. test_method: <bound method Mytest.test_ls of <example_log_unit_test.Mytest testMethod=test_ls>>
# .test_ls is called.
# ssh_connection::execute_command ls /home/pi
#  Output from Rasberry Pi: Desktop
# Documents
# Downloads
# Music
# Pictures
# Public
# python_games
# PythonGPIO
# Templates
# Videos
#
#  errString :
# output from NFS: Desktop
# Documents
# Downloads
# Music
# Pictures
# Public
# python_games
# PythonGPIO
# Templates
# Videos
#
# teardown_method is called. test_method: <bound method Mytest.test_ls of <example_log_unit_test.Mytest testMethod=test_ls>>
# teardown_class is called for class: Mytest
#
#
# ========================== 2 passed in 2.13 seconds ===========================
# Process finished with exit code 0
#

# C:\Users\lama2\PycharmProjects\test-automation>pytest -s example_unit_test.py
# ============================= test session starts =============================
# platform win32 -- Python 3.6.1, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
# rootdir: C:\Users\lama2\PycharmProjects\test-automation, inifile:
# collecting 0 items
# collecting 2 items
# collecting 2 items
# collected 2 items
#
#
#  example_unit_test.py setup_class is called for class:Mytest
#
#     setup_method is called. test_method: <bound method Mytest.test_get_file of <exam
#          ple_unit_test.Mytest testMethod=test_get_file>>
#     test_get_file is called.
#     teardown_method is called. test_method: <bound method Mytest.test_get_file of <
#          example_unit_test.Mytest testMethod=test_get_file>>

#     setup_method is called. test_method: <bound method Mytest.test_ls of <example_un
#          it_test.Mytest testMethod=test_ls>>
#     test_ls is called.
#     teardown_method is called. test_method: <bound method Mytest.test_ls of <exampl
#          e_unit_test.Mytest testMethod=test_ls>>

#  teardown_class is called for class: Mytest
#
# ========================== 2 passed in 0.05 seconds ===========================