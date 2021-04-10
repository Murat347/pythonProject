# 03/13/2021
# Working with part of the list
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']

# slice of the list list_name [start:stop] - start is inclusive, stop is exclusive values
#values: list_name[start]
for car in cars[1:3]:
    print(f"the car is : {car}")

print("-------second----------")
for car in cars[:3]: #the same thing as cars[0:3]
    print(f"the car is : {car}")

print("-------third----------")
for car in cars[2:]: #the same thing as cars[2: end of the list]
    print(f"the car is : {car}")


print("-------fourth----------")
for car in cars[2:10]: # no Index out of range
    print(f"the car is : {car}")

print("-------copying and linking----------")
print("-------linking the 2 variable to the same value----------")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw')

