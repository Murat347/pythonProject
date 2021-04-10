# 1. A list of lists
#2. A list of Disctionaries
# 3. A list in a Dictionary
# 4. A Dictionary in a Dictionary

countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = [companies, cities, countries]
print(customers)
print(customers[0])
print(customers[0][0])
print(f"printing barcelona: {customers[1][2]}")

multi_dim_nums = [
    [3, 9, 0],
    [2, 7, 1],
    [0, 1, 0]
    ]


print(f"printing the middle value {multi_dim_nums[1][1]}.")

print(f" Looping through nultidimensional list(array).")
for column in customers:
    print(column)
    # ['level up', 'abc company', 'ola company']
    for value in column:
        print(value.upper())

for city in customers[1]:
    print(city, end='\t')

# h/w print multiplication table
print('**** list of dictionaries ****')
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 30, 'city': 'tokyo'}

users = [user_1, user_0, user_2]

print(users[0])
print(users[2]['name'])
print(users[2]['age'])
print(users[2]['city'])

print("----- looping -----")
for user in users:
    print(user['name'], end= ' || ')
    print(user['age'], end= ' || ')
    print(user['city'])

print('******* list of dictionaries **********')
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = {
    'countries':  ['usa', 'russia', 'spain'],
    'cities':  ['new york', 'moscow', 'barcelona'],
    'companies':  ['level up', 'abc company', 'ola company']
}

print(customers['cities'])
print(customers['cities'][1]) # prints 2nd element from cities

print('**** Dictionary in a Dictionary *****')
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 30, 'city': 'tokyo'}

users = {
    'user_0': {'name': 'john', 'age': 25, 'city': 'brooklyn'},
    'user_1': {'name': 'jane', 'age': 20, 'city': 'paris'},
    'user_2': {'name': 'mark', 'age': 30, 'city': 'tokyo'}
}

print(users)
print(users['user_0'])
print(users['user_0']['name'])
print(users['user_2']['city'])

# for user in users.keys():
#     print(user)
#     print(users[user])
for username, details in users.items():
    print(username)
    #print(details['name'])
    for key, value in details.items():
        print(f"details key is : {key}")
        print(f"details value is : {value}")

 # Sunday class 03/22/2021

print('*** incrementing the variable to reach the upper boundary ***')
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print('*** decrementing the variable to reach lower boundary ***')
current_number = 10
while current_number >= 5:
    print(current_number)
    current_number -= 1
    print(current_number)

print('**** Game Started ****')
# enter colors, green - 15, yellow - 10, red - 5
# other colors ro something you lose
# q or quit is to end the game

color = None
while color != 'quit' or color != 'q':
    color = input("Enter your color (green/yellow/red):")
    color = color.lower().strip()
    points = 0
    if color == 'quit' or color == 'q':
        break
    elif color == 'green':
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 5
    else:
        print("Sorry, that's not the right color. You lost.")
    print(f"You have {points} points.")
print("closing the game...")

#'Hello guys'

count = 0