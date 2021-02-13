#3 classes
#A Train class -  speed up and slow down. Load and unload. A train has a list of cars
#A passenger car class
#Cargo car class

class Train:
    def __init__(self):
        self.cars = []

    def get_cars(self):
        return self.cars.copy()

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, index):
        self.cars.pop(index)


class Car:
    def __init__(self):
        pass
    def load(self):
        pass
    def unload(self):
        pass

