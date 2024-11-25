# register check
            
register = {
    'Solomon': 'no',
    'Patience': 'yes',
    'Esther': 'yes',
    'Daniel': 'no',
    'Michael': 'yes',
    'John': 'no',
    'Peter': 'yes',
    'Mary': 'yes'
}


def register_check(reg: dict):
    count = 0
    for value in reg.values():
        if value == 'yes':
            count += 1
    return 'Number of students in school is', count

print(register_check(register))



# def register_check():
#     register = {
#         'Michael':'yes',
#         'John': 'no',
#         'Peter':'yes',
#         'Mary': 'yes',
#     }
#         numb = 0
#         for i in register:
#             if present == 'yes':
#             numb += 1
#             numbs.append(numb)
#             print(numb)