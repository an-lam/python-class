# C:\Users\lama2\dd-python\taas\dm_dev\athena\tests\samples\test_sample_pytest.py
from time import sleep

import pytest

def setup_module(module):
    """ run this code at the beginning of the module """
    print("setup_module for module:%s" % module.__name__)


def teardown_module(module):
    """ run this code at the end of the module """
    print("teardown_module for module:%s" % module.__name__)


class TestMyTestcase(object):
    """
    20 or so tests to demonstrate:
        1. the order of the pytest plugin calls
            setup_module
                setup_class
                    setup_method
                    run test_...
                        stepbegin
                        ...
                        stepend
                    teardown_method
                teardown_class
            teardown module
        2. Negative tests demo TestStatus with exceptions and bad test steps
    Usage:
      run all tests, client parameter is optional, ddr is required
      python -m pytest -s test_sample_pytest.py

       pytest -s test_sample_pytest.py

      pytest -k test_numbers test_sample_pytest.py --ddr=dd890-73.chaos.local
    """
    @classmethod
    def setup_class(cls):
        """
        run this code before running any tests in TestMyTestcase
        """
        cls.log.info("calling setup_class for class:%s" % cls.__name__)


    def setup_method(self, test_method):
        """ run this code at the beginning of each test """
        self.log.info("calling setup method for method:%s"
                      % test_method.__name__)
        if test_method.__name__ == "test_setup_error":
            raise ConfigParamException

    def test_numbers(self):
        """ test case to verify 3*3 == 9 """
        self.tcr.stepbegin(1, "test numbers assert three times three equals "
                              "nine")
        sleep(1)
        assert(3*3 == 9)
        self.tcr.stepend(self.STATUS_OK)

    def test_letters_pass(self):
        """ test case to verify 'a'*3 != "abc" """
        self.tcr.stepbegin(1, "test letters, assert 'a' times three does NOT"
                              " equal 'abc'")
        sleep(2)
        assert("a"*3 != "abc")
        self.tcr.stepend(self.STATUS_OK)

    def test_letters_fail(self):
        """test case to demonstrate failed assertion """
        self.tcr.stepbegin(1, "test letters, assert 'a' times three does"
                              " equal 'abc'")
        assert("a"*3 == "abc")
        self.tcr.stepend(self.STATUS_OK)

    def test_runtime_error(self):
        """test case that raises a runtime exception"""
        raise RuntimeError

    def teardown_method(self, test_method):
        """"" run this code at the end of each test """
        self.log.info("calling tear down method for method:%s"
                      % test_method.__name__)
        if test_method.__name__ == "test_teardown_error":
            username = "Teddy"
            raise Exception("Unable to remove user %s" % username)

    def test_raise_script_error(self):
        """ test case to demonstrate raise of script error"""
        try:
            i = 1/0
        except ZeroDivisionError:
            raise

    @classmethod
    def teardown_class(cls):
        """ run this code after running all of the tests in the class """
        cls.log.info("calling tear down class for class:%s" % cls.__name__)
