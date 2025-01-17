import sys
# # A python program to do arithmetical operations addition and division.

# # addition
# # first implementation
# first_number = input("enter first number: ") # 5
# second_number = input("enter second number: ") # 5
 
# result = first_number + second_number
# print(result) # program should return 10

# # pitfall : this program outputed 55 instead of 10 because the program just appended the two numbers
# # suggested solution: convert inputed number to integer


# # # second implementation
# first_number = int(input("enter first number: ") )# 5
# second_number = int(input("enter second number: ") )# 5
 
# result = first_number + second_number
# print(result) # program should return 10

# pitfall : the code breaks down when a decimal was inputed
# suggested solution : using float instead of int 

# first_number = float(input("enter first number: ") )# 5
# second_number = float(input("enter second number: ") )# 5
 
# result = first_number + second_number
# print(result) # program should return 10

# pitfall : code breaks when any character order than a number is inputed
# suggested solution : include try and catch block to make sure code still runs if any character other than a number is inputed.


# Implementation
try:
    first_number  = float(input("enter first number: "))
    second_number = float(input("enter second number: "))
except ValueError:
    print("enter a digit next time.")
    sys.exit()

result = first_number + second_number
print(f"the sum of {first_number} + {second_number}  is  {result}")

