# Brute Force solution
def two_sum_problem(arr, target):
    for i in range (len(arr) - 1):
        for j in range (i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
    return None
result = two_sum_problem([1,2,3], 4)
print(result)
arr = [1, 2, 3]
target = 4


# print("hello world")

# message = "give me one magazine".split()
# print(message)

# print("kofi".split())

