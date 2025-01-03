import math
#the len function returns the total number of elements.
#with indexing, it begins with 0, and the last element is the length of the elements - 1
numbers = [1, 2, 3, 4, 5, 6]
low = numbers[0]
high = len(numbers) -1 
mid = len(numbers) / 2
search = (low + high) / 2

print(low)
print(high)
print(mid)
print (math.floor(search))