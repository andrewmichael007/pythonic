# string range

def string_range(num:int): 
    x = [str(i) for i in range(num)]
    x = ".".join(x)
    return x

print(string_range(6))


# dictionary of names

names = ["Christabel", "Desmond", "Bella", "Diana",
         "Courage", "Christabel","Abigail"
            "Elvis", "Chris", "Romeo", 
            ]

d = {}   # creating an empty dictionary
for name in names:
    # using  the  starts with method to find all names that starts with s
    if name.startswith('C'):
        # using the dictionary update method
        d.update({name: names.count(name)}) 
print(d)






# score = 0
# for i in names:
#     if (names[0]) == "S":
#         count += 1
#         dic_of_names = {names} , ":" , {count}
#         return dic_of_names