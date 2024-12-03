# only floats

#creating a function that takes two arguments.
def only_floats(a, b): 
    #return 2 if first argument is a float and second argument is also a float
    if type(a) == float and type(b) == float: 
        return 2
    #return 1 if one of the argument is a float
    elif type(a) == float or type(b) == float:
        return 1
    #return 0 if none of the argument is  a float
    else:
        return 0

print(only_floats(5, 6))  # 👉 0
print(only_floats(5.0, 6))  # 👉 1
print(only_floats(5.0, 6.0)) # 👉 2


# def only_floats(a, b):
#     if a and b == float:
#         return '2'
#     elif a or b == float:
#         return '1'
#     else:
#         return '0'

# print(only_floats(5, 6))