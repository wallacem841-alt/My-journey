from abc import ABC, abstractmethod

# Abstract base class defining the common interface for all vehicles
class Vehicle(ABC):

    # Concrete method shared by all vehicles
    def start_engine(self):
        print("Engine started")
    
    # Abstract method to enforce implementation of a 'go' action in subclasses
    @abstractmethod
    def go(self):
        pass

    # Abstract method to enforce implementation of a 'stop' action in subclasses
    @abstractmethod
    def stop(self):
        pass

# Concrete subclass implementing the Vehicle interface for a Car
class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

# Concrete subclass implementing the Vehicle interface for a Motorcycle
class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

# Concrete subclass implementing the Vehicle interface for a Boat
class Boat(Vehicle):

    def go(self):
        print("You drive the boat")

    def stop(self):
        print("You anchor the boat")

# Instantiate a Car and call its 'go' method
car = Car()
car.go()

# Instantiate a Boat and call its 'start_engine' method
boat = Boat()
boat.start_engine()