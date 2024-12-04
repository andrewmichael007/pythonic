# this tool takes a set of numbers, and separates them into even and odd numbers

#imports system
import sys

#creates a function called odd_even which takes array of numbers as an argument.
def odd_even(numbers):
    # create an empty array to hold even numbers
    even_numbers = []
    # creates an empty array to hold odd numbers
    odd_numbers = []
    # loop through numbers
    for each in numbers:
        #check if each is even thus divisible by 2
        if each % 2 == 0:
            #add that number to the empty even_numbers array created above
            even_numbers.append(each)
        else:
            # check if each is odd thus leaves a remainder if divided by 2
            odd_numbers.append(each)
    return f"even numbers are {even_numbers} and the odd numbers are {odd_numbers}"
    # return max(even) - min(odd)

print(odd_even([1,2,3,4,5,6]))
# print(odd_even([1,2,3,4,5,6,7,8]))
# print(odd_even([1,2,3,4,5,6,7,8,9,10]))


# EXTRA CHALLENGE

# def prime_numbers():
#     prime_num = []
#     try:
#         n = int(input('enter a number: '))
#     except ValueError:
#         print('please enter an integer next time.')
#         sys.exit()
#     for i in range(0, n + 1):
#         if i > 1:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 prime_num.append(i)
    
#     return prime_num

# print(prime_numbers())

