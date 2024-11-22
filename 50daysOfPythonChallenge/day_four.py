# only floats

def only_floats(a, b): #creating a function that takes two arguments.
    if type(a) == float and type(b) == float: #checking the type of a and b.
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0

print(only_floats(5, 6))
print(only_floats(5.0, 6))
print(only_floats(5.0, 6.0))


# def only_floats(a, b):
#     if a and b == float:
#         return '2'
#     elif a or b == float:
#         return '1'
#     else:
#         return '0'

# print(only_floats(5, 6))