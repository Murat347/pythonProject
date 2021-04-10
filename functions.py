# 03/21/2021

def greet_user():
    """ this is a dockstring, something that describe the function."""
    print("Hello!!!")


def great_user_by_name(name):
    """It will say hello and use the name entered.
    Name is required, user has to pass a function
    """
    print(f"Hello, {name.title()}!")


def sum_numbers(num1, num2):
    print(f"sum of {num1} and {num2} is {num2 + num1}")
    print(f"square of {num2} is: {num2 ** 2}")


def describe_pet(pet_name, pet):
    print(f"I have a {pet}, and we call it {pet_name.title()}")


# *********
# All executions of the funtions (Calling the functions)
# greet_user() #this is how you CALL function
# # greet_user_by_name() #expected TypeError
# #greet_user_by_name('ali')
# sum_numbers(45, 789)
# sum_numbers(-456, 3444)
# sum_numbers(num2=-46,num1=34)
# #we can specifically mention parameters this way as well

describe_pet('Balu', 'dog')
