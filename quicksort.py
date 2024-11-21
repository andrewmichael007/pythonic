def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [ x for x in arr if x < pivot]
    middle = [ x for x in arr if x ==  pivot]
    right = [ x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

data = [ 3, 1, 4, 2]
print(quicksort(data)) 




# name = input("Enter your name: ")
# address = input("enter your house number: ")
# try:
#     firstvalue = int(input("Enter first number : "))
#     secondvalue = int(input("Enter second number : "))
# except ValueError:
#     print("Enter a digit next time.")
# finalvalue = print("The result is: ", int(firstvalue + secondvalue)
                   
    


