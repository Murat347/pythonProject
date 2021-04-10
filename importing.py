# 03/27/2021 Importing the modules


import sys
# import time
from time import *


# from functions_pkg.functions_return import *
#sleep(5) # use this when you 'from time import'


print(sys.platform)
print_formatted_name('akmal', 'husanov')
# # time.sleep(5)  use this when 'import time'

def get_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name


def print_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title ()} {lastname.title ()}"
    print(name)

full_name = get_formatted_name('john', 'doe')
print(full_name)
print(get_formatted_name('jane', 'doe'))


print_formatted_name('ali','tehrani')
student = print_formatted_name('baur', 'eskara')
print(f"value of student is: {student}")
print(f"value of student is: {print_formatted_name('baur', 'eskara')}")

# print(get_list_of_even_numbers(20))

def print_usernames(users: list):
    for user in users:
        print(f"current user is: {users}")

print_usernames(['karim', 'dron', 'gor'])