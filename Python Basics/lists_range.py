# 03/11/2021 - Lists (continue)

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
# Making Numerical List
# Range([start], stop, [step]) - return an object that produces a sequence of integers from start (insclusive) to stop (exclusive)
for num in range(4):
    print(f"number: {num}")

# shift + fn + f6 - shortcut for Refactor>rename
# ctrl + Y - deletes the line without selecting

nums = range(4) # this does not mean nums = [0, 1, 2, 3]
nums2 = list(range(4)) # this creates list data structure from sequence of numbers
print(nums)
print(nums2)

for num in nums2:
    print(num)
print("range with start and stop ---")
for num in range(1, 4):
    print(num)

print("range with start, stop and step ---")
for num in range(1, 10, 2):
    print(num)

print("print all even numbers from 1 to 16 (16 should be included)")

evens = []
for num in range(2, 17, 2):
    print(num)
    evens.append(num)
    print(evens)

print(f"This is the final list: {evens}")

print(" print the squares of numbers from 10 to 20 ")
squares = list()
for num in range(10, 21):
    squares.append(num**2)
    # print(num*num)
print(f"final list: {squares}")
print(f"min(squares): {min(squares)}")
print(f"max(squares): {max(squares)}")
print(f"sum(squares): {sum(squares)}")

cars = ['bugatti', 'ferrari', 'tesla', 'lexus', 'bmw']
cars_len = len(cars)
for car in cars:
    print(car)
    print(f"index of the {car} is {cars.index(car)}")

print("looping the list using index*********")
for ind in range(len(cars)):
    print(ind)
    print(f"index of the {car} is {cars.index(car)}")

#--------------
print("# List comprehension : ")
squares = list()
for num in range(10,21):
    squares.append(num**2)
squares = [num**2 for num in range(10,21)] # for read only, use later
print(squares)





