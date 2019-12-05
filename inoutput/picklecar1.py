# picklecar1.py
import pickle

car2 = ('Lexus', 'RX350', 350, 2010)
cars = {('Lexus', 'RX350', 350, 2010), ('BMW', '328i', 280, 2015)}
mydict = {"Honda": ("Accord", 2018)}
# Save (dump) car into 'car.pickle' as binary file
with open("car.pickle", "wb") as carpickle:
    for car in cars:
        pickle.dump(car, carpickle)
        print(car)

with open("car2.pickle", "wb") as car2pickle:
    pickle.dump(mydict, car2pickle)
    print(mydict)


