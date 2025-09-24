numbers = [1, 2, 3, 4, 5]


#in python, the length of an array is equal to the number of elements, 
# return size of list
print("************************")
# print(len(numbers))  # 👉 5
print("************************")


#in python, indexing(accessing items) starts from 0 to the lenght of the array,
# technically, indexing would always be lenght - 1 
# print(len(numbers) - 1)   👉 4

# print(len(numbers) - 2)   👉 3

# print(numbers[0])

#middle of the array
print("************************")
# middle_number =  (len(numbers) / 2)
# print(middle_number) # 👉 2.5
print("************************")

lenght_of_numbers = len(numbers)
for each in numbers:
    # print(each)
    temp = numbers[0]
    numbers[0] = numbers[lenght_of_numbers - 1]
    numbers[lenght_of_numbers-1] = temp

    #for swapping the second index
    temp2 = numbers[1]
    numbers[1] = numbers[lenght_of_numbers - 2]
    numbers[lenght_of_numbers-2] = temp
print(numbers)


