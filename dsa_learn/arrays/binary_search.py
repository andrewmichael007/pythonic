# pseudocode for  binary search
def binary_search(numbers):
  low = numbers[0]
  high = numbers[n - 1 ]
  target = something
  
  while low <= high:
    mid =  (low + high) // 2 
    
    #if the mid is greater than the target, discard from mid to high. How ? by setting a new high
    if mid > target:
      high = mid - 1 

    #if the mid is less than the target, discard from low to mid. How ? by setting a new low
    else if mid < target:
      low = mid + 1

    #else if mid == target, number found
    else:
      target == mid
    
    
