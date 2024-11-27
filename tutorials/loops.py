# Program : Sum numbers

# Author : Andy

# Description: this tool takes a list of numbers, loop through
#print out total

#initialize a counter
counter = 0
#array of numbers
numbers = [1,2,3,4,5,6] #👉 21
#for loop to loop through numbers
for each in numbers:
    #update counter by adding counter to each
    counter = counter + each
    #repeat till last number
#exit out of the for loop and print out the total
print(f"the total number is {counter}")
    
# Program : Maximum number

# Description: this tool takes an array of numbers, loop through
#print out the largest number

#initialize an array of numbers should return 30
digits = [20,15,25,10,30,5] #👉 30
#initialize maximum number as the first number of the array at position 0
max_numb = digits[0]
#loop through the numbers starting from the first
for each in digits:
    #if the first looped (20) number is greater the number at the first position (20)
    if each > max_numb:
        #set the maximum number to each (the looped number)
        max_numb = each
        #repeat till the last number
#exit out of loop, print out the maximum number
print(f"the maximum number is {max_numb}")

# Program : Minimum number

# Description: this tool takes an array of numbers, loop through
#print out the minimum number

#initialize an array of numbers should return 5
figures = (20,15,25,10,30,5,35) #👉 5 
#initialize minimum number as the first number of the array at position 0
min_numb = figures[0]
#loop through the numbers starting from the first
for each in figures:
    #set the minimum number to each (the looped number)
    if each < min_numb:
        #set the minimum number to each (the looped number)
        min_numb = each
        #repeat till the last number
print(f"the minimum number is {min_numb}")
#exit out of loop, print out the minimum number


