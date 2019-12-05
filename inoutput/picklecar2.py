# picklecar2.py
import pickle

# Read (load) car data back from binary file "rb"
with open("car.pickle", "rb") as carpickle:
    while True:
        try:
            car = pickle.load(carpickle)
            make, model, engine, year = car
            print("make: {}, model: {}, engine: {}, year: {}".format(make, model, engine, year))
            #print(car)
        except EOFError:
            break

with open("car2.pickle", "rb") as car2pickle:
    while True:
        try:
            car2 = pickle.load(car2pickle)
            print(car2["Honda"])
        except EOFError:
            break

