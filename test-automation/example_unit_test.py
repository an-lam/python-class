import unittest
import sys
import os

import logging

from contextlib import contextmanager

"""
Setting debug level:
   Level      Value
   CRITICAL   50
   ERROR      40
   WARNING    30
   INFO       20
   DEBUG      10
   UNSET      0
The log message is only emitted if the handler and logger are configured to 
emit messages of that level or higher. For example, if a message is CRITICAL,
and the logger is set to ERROR, the message is emitted (50 > 40). If a 
message is a WARNING, and the logger is set to produce only messages set to 
ERROR, the message is not emitted (30 < 40).
"""
LOG_FILENAME = 'example_unit_test.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    #level=logging.INFO,
    level=logging.DEBUG,
    #level=logging.ERROR,
)

class Mytest(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        """
        This code will be run before any test case
        :param cls - this class reference (similar to self)
        """
        print("setup_class is called for class: {}".format(cls.__name__))

        # Getting a logger instance
        #cls.log = logging.getLogger(__name__)
        cls.log = logging.getLogger()   # set up log for other methods
        cls.log.info("Calling Mytest:setup_class")

    @classmethod
    def teardown_class(cls):
        """
        This code will be run after completing all test cases
        :param cls - this class reference (similar to self)
        """
        print("teardown_class is called for class: {}".format(cls.__name__))

    def setup_method(self, test_method):
        """ run this code at the beginning of each test: test_xxx """
        print("setup_method is called. test_method: {}".format(test_method))

    def teardown_method(self, test_method):
        """"" run this code at the end of each test: test_xxx """
        print("teardown_method is called. test_method: {}".format(test_method))

    def test_ls(self):
        print("test_ls is called. ")
        x = 5
        assert x == 5, "Failed x != 6"
        # log was initialized in setup_class (cls.log)
        # self is an instance of cls.  It has access to cls's data
        self.log.info("This goes to log file: 'test_ls'")

    def test_get_file(self):
        print("test_get_file is called.")
        self.log.debug("This goes to log file: 'test_get_file'")

if __name__ == '__main__':
    unittest.main()

# Click "Run" "Pytest in example_unit_test.py"
# or run on command line
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