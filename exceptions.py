# 04/04/2021
#        print(lines)
#
# except FileNotFoundError as err:
#        print('err')
#        print("Enter correct file path, check your file path")
#




# print(5/0)

try:
    num = 5/int(input("enter the number divide by: "))
except ZeroDivisionError as err:
    print('You cannot devide by zero')
else: # this is dependant on the try block, if they block executes else block will be executed
    print('this is else block')
    print(f"Result of this division: {num}")
finally:
    print("I am a Finally block, I am always executed whatever happens with try, except or else block")

print("Program is completed")