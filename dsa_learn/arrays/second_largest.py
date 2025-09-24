def second_largest(numbers):
    temp = numbers[0]
    for each in numbers:
        if each > temp:
            temp = each
        if each < temp and each > each:
            temp = each
        return temp
# print(second_largest([10, 2, 5, 13, 1])) #👉 10
print(second_largest([1, 2, 5, 13, 20])) #👉 13


