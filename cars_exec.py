# 04/03/2021
# This file is for executing the cars.py classes
from classes.cars import Car, ElectricCar

# greet_user()
# drive()
# Execution
# drive() will not have an access to this function yet

# mycar = Car() # Car is the class, mycar is an object, in this line we are creating instance of the (instantiation)

mycar = Car("BMW", "530xi", "black")
yourcar = Car("Lexus", "lexus RX", "silver")

print("------------------")
mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.odo_reader = 45 # this is the direct access to the instance variables
mycar.set_odometer_reader(65)
mycar.set_odometer_reader(34)
mycar.set_odometer_reader(545)
mycar.set_odometer_reader(9504)
mycar.colorofthecar = 'RED'
mycar.get_description()

# yourcar.do_something()
print("------------------")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()

print("--- Increment ---")


print("--- Electric Car instances ---")
my_ev = ElectricCar("tesla", "model x", "blue")
my_ev.drive()
my_ev.get_description()


