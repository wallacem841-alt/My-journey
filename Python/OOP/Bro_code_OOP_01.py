class Car:

    salesmen = "vedita" #Class variable (Global to the class)
    cars_qtd = 0

    def __init__(self, model, year, color, for_sale): #Constructor
        self.model = model
        self.year = year #instance variable
        self.color = color
        self.for_sale = for_sale
        Car.cars_qtd +=1



    def drive(self):
        print(f"you drive a {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.for_sale}")

car1 = Car("Logan", 2008, "Green", False)
car2 = Car("Civic", 2015, "Blue", True)
car3 = Car("Mustang", 2020, "Red", True)
car4 = Car("Corolla", 2012, "White", False)
car5 = Car("Tesla Model S", 2023, "Black", True)

all_cars = [car1, car2, car3, car4, car5]

print(car1.model)

car1.drive()

car1.stop()

car1.describe()

print(Car.salesmen)

print(Car.cars_qtd)

print('Vedita has these cars:')

for car in all_cars:
    print(car.model)