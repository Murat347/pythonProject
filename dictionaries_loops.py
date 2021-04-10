# 03/20/2021 Looping through Dictionary

my_car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in my_car:
    print("----------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is: {my_car[key]}")

print("----2.using keys----")
for key in my_car.keys():
    print("----2----")
print(f"key in this iteration is: {key}")
print(f"value of this key is: {my_car[key]}")

# If 'model' in my_car.keys():
if 'model' in my_car:
    print(f"Yes, my car description contains model information")

print("----3. using values----")
for value in my_car.values():
    print("--------")
print(f"value in this iteration is: {value}")
# print(f"value of this key is: {my_car[value]}")

print("----4. using dictionary items()----")
for key, value in my_car.items():
    print("--------")
print(f"val1 in this iteration is: {key}")
print(f"val2 of this key is: {value}")

if 1964 in my_car.values():
    print(f"Yes ")

print("******** exercise 6-5 ****************")
""" 6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary."""

rivers = {'nile': 'egypt', 'tigers': 'iraq', 'amazon': 'brazil', 'mississippi': 'usa'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")