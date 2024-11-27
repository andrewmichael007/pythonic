# Description:
#  this tool takes a number...
# returns the square of the number if it's divisible by 5..
# or returns the remainder if it's not divisible by 5. 


#import system to control the work flow of the program
import sys

#the try block ensures the the program run even when there's an error..... it takes care of value error
#when anything apart from a number is inputed by the user, the user is prompted to enter a digit next time and the program ends.
try:
    #prompt a user for a number
    number = int(input("enter a number: "))
    print("***************************************\n")
#catches value error
except ValueError:
    print("**************************************************")
    #prompts the user for a digit next time
    print("Please enter a digit next time.")
    #end the program
    sys.exit()
    
while True:
    #check if number is divisible by 5
    if number % 5 == 0:
        #create a variable to store the square root of the number
        sq_root = number ** 0.5
        #display the square root of the number to the user 
        print(f"The square-root of {number} is {sq_root}")
    else:
        #create a variable to store the remainder
        remainder = number % 5
        #display the remainder to the user
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
