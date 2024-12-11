# def hide_password():
#     password = input("enter password: ")
#     hid_password = len(password) * " * " 
#     return f"Your password is {password} and it's {len(password)} characters long."
              
# print(hide_password())


#EXTRA CHALLENGE
# Write a function called equal_strings. The function takes 
# two strings as arguments and compares them. If the strings 
# are equal (if they have the same characters and have equal 
# length), it should return True; if they are not, it should 
# return False. For example, "love" and "evol" should 
# return True

# def equal_strings(string1, string2)
#prompt user for string1
# string1 = input("enter word: ").lower()
# #prompt user for string2
# string2 = input("enter another word: ").lower()

# if len(string1) == len(string2):
#     for each in string1:
#         if each in string2:
#             print("true")
# else:
#     print("false")
# #checking the length of two words
# for each in string1:
#     if each in string2 and len(string1) == len(string2):
#         #return just true.
#     else:
#         print("false") 


def equal_strings(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) == len(string2):
        for each in string1:
            if each in string2:
                return "true"
                # print("true")
    else:
        print("false")
equal_strings("love", "evol")






