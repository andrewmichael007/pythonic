# square and division

import sys

try:
    number = int(input("enter a number: "))
    print("***************************************\n")
except ValueError:
    print("**************************************************")
    print("Please enter a digit next time.")
    sys.exit()
    
while True:
    if number % 5 == 0:
        sq_root = number ** 0.5
        print(f"The square-root of {number} is {sq_root}")
    else:
        remainder = number % 5
        print(f"The remainder of the division is {remainder}")
    print("********************************************")
    break


# def divide_or_square(number):

#     if number % 5 == 0:
#         sq_root = number ** 0.5
#         return f"The square-root of the number is {sq_root}"
#     else:
#         remainder = number % 5
#         return f" The remainder of the division is {remainder}"
# print(divide_or_square(20))
