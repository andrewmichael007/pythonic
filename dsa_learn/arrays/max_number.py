# this program outputs the maximum number  from an array
def min_max(numbers):

#pseudocode for checking the maximum number
#first check if array is empty
    if not numbers:
        return "empty array"

#set is_max  to the first number initially
    is_max = numbers[0] 

    for each in numbers:
        if each > is_max:
            is_max = each
    return is_max
print(min_max([10, 2, 5, 13, 1, 8])) #  👉 13
print(min_max([3, 3, 3, 3]))# 👉 empty array
print(min_max([])) #👉 empty array
print(min_max([])) #👉 empty array
# ✅ Strengths
# Correctness:
# This implementation correctly finds the maximum number in the array.
# It starts with the first element and iterates through the list, updating is_max whenever a larger number is found.

# Simplicity:
# The logic is clear and easy to understand.
# The loop structure ensures that every element is checked exactly once.

# Efficiency (Time Complexity):
# The time complexity is O(n)
# O(n), where 
# 𝑛
# n is the number of elements in numbers.
# This is optimal because we must check all elements at least once to be sure we found the max.

# Space Complexity:
# O(1) → This algorithm uses only a single extra variable (is_max), making it memory-efficient.

# ❌ Weaknesses
# Only Finds Maximum:
# The code only finds the maximum number, but the problem also asks for the minimum.
# You could extend it to track both is_max and is_min in the same loop.

# Edge Cases Not Handled:
# Empty Array: If numbers = [], this code will throw an IndexError because numbers[0] is accessed when the list is empty.
# Single Element Array: If numbers = [5], the algorithm should still return 5 correctly (this works in your case).
# All Elements are the Same: If numbers = [3, 3, 3, 3], the logic should still return 3, which it does correctly.


# 🚀 Optimized Version (Handle Min & Edge Cases)
#  improved solution by:
# Finding both min and max in a single pass (instead of looping twice).
# Handling edge cases like an empty array.
