import os

class TestSamples():

    @classmethod
    def setup_class(cls):
        cls.log.info("calling setup_class method")

    def test_check_time(self):
        print(os.times())

    def test_check_os_name(self):
        print(os.name)


    def teardown_method(self, test_method):
        self.log("calling tear down method")

    @classmethod
    def teardown_class(cls):
        print(cls)
        #super().teardown_class()

    @classmethod
    def log(cls, message):
        print("Write to log file: {}".format(message))