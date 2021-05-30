class Vehicle:
    def __init__(self, brand, make):
        self.brand = brand
        self.make = make

    # Common method for all subclasses.If needed it can be modified in child classes.
    def get_vehicle_details(self):
        print(f"Vehicle brand is - {self.brand} and it was manufactured in {self.make}")

    # Abstract method - Child class must implement this method
    def start(self):
        raise NotImplementedError("Subclass must implement start method")

# To inherit Vehicle class pass it as argument in parenthesis
class Car(Vehicle):
    # Initializer
    def __init__(self, brand, model, make):
        Vehicle.__init__(self, brand, make)
        self.model = model

    # Implementing abstract method of parent class
    def start(self):
        print(f"{self.brand} {self.model} car started.")

    # Subclass 'Car' specific method
    def get_model(self):
        return self.model

class Truck(Vehicle):
    # Initializer
    def __init__(self, brand, category, make):
        Vehicle.__init__(self, brand, make)
        self.category = category

    # Implementing abstract method of parent class
    def start(self):
        print(f"{self.category} {self.brand} Truck started.")

    # Subclass 'Truck' specific method
    def get_category(self):
        return self.category

    # Overriding parent class methods
    def get_vehicle_details(self):
        print(f"Vehicle is {self.brand}'s {self.category} truck and it was manufactured in {self.make}")

# Creating Car class object
my_car = Car(brand="Tata", model="Safari", make=2021)
my_truck = Truck(brand="Tata", category="18 Wheeler", make=2020)

# Accessing vehicle properties
print(f"I had purchased my car in year : {my_car.make}")
print(f"I had purchased my car in year : {my_truck.make}")

# Calling parent class implemented method
my_car.get_vehicle_details()
my_truck.get_vehicle_details()

# Calling parent class abstract method
my_car.start()
my_truck.start()

# Calling subclass specific methods
print("My car model : ", my_car.get_model())
print("My truck category : ", my_truck.get_category())

"""
In this example "start()" method was declared in Parent class(i.e Vehicle class) but was defined in child class 
(i.e Car class and Truck class).So basically parent class as well as both child classes have same method 'start'.
This is called 'Polymorphism' and more particularly 'Polymorphism with inheritance'.
And the process of re-implementing a method in the child class is known as "method overriding". 
"""