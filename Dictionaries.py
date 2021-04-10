# 03/18/2021 Dictionaries

# key/value pair data structure, since each element comes as (key: value)
# Create, access, modify (add/remove/update elements)
# looping this data structure
# some mostly used builtin functions


my_friend = {}
my_house = dict()
my_car = {"brand": "Ford", "model": "Mustang", "year": 1964, 1: "value of 1"}

print(my_car)
print(my_car['brand'])
print(f"the value of key 'brand' is: {my_car['brand']}")
print(my_car[1])  # this is not an index, my_car has key=1

my_car['price'] = 125000.00
print("price is added ---------")
print(my_car)

# udpating the value in dictionary
del my_car[1]
print(my_car)

# Exercise 6-1

amigo = {'first_name': 'Vitaly', 'last_name': 'Didkivsky', 'age': 19, 'city': 'Florence'}

print(f"my friend's first name is : {amigo['first_name']}")
print(f"my friend's first name is : {amigo['last_name']}")
print(f"my friend's first name is : {amigo['age']} years old")
print(f"my friend's first name is : {amigo['city']}")



