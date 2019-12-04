# car1.py

class Car:

    """ A car with properties and methods """
    power_source = "electricity"
    make = ""

    #def __init__(self, make):
    #    self.make = make
     #   self.start = False

    def __init__(self, make, year=0):
        self.make = make
        self.year = year
        self.start = False

    def start_engine(self):
        # Bug ?
        self.start = True

    # This method is called by print(object)
    def __str__(self):
       return "Make: {0.make}, year: {0.year}, start: {0.start}, power: {0.power_source}".format(self)
