# If statement
# if expression:
#      code here when expression is true
# else expression:
#      code here when expression is false
#

#num1_str = input("enter the num1: ")

num1 = int(input("enter the num1:"))
num2 = 3

#if num1 < num2:
if num1 == num2: #comparing 2 values using ==
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print("if statement completed here")



print("--if statement with lists ---")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
if 'tesla' in cars:
    print("yes we have tesla in stock")
else:
    print("sorry we don't have this car.")