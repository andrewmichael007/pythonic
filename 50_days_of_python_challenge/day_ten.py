# this tool takes a set of numbers and displays the total

#creates a function called sum numbers
def sum_numbers (numbers):
    #creats a variable total
    total = 0
    #loop through numbers
    for each in numbers:
        #calculates total and stores the new value of total still in total
        total += each 
    #displays total after each iteration
    return total
#displays total after  loop ends
print(sum_numbers([1,2,3,4,5,6,7,8,9,10]))  # expected output 👉 55
    
    
