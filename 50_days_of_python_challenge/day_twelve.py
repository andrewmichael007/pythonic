#There's a bug: The program is supposed to display an error message when a user inputs a number

#import system
import sys
#create a function called equal_strings
def equal_strings():
    #a try block that catch all value errors 
    try:
        string1 = input("enter anything: ")
        print("*******************************************")

        string2 =  input("enter something different: ")
        print("*********************************************")   
    #output a message to tell user to input a string instead.  

    except ValueError: 
        print("no figures next time please.")
        #exit the program
        sys.exit()
    #check if length of first string is equal to length of string2
    if len(string1) == len(string2):
        return 'True'
    else:
        return 'False' 

print(equal_strings())

#Extra challenge
# This is a program that takes a string 
# separated by dots as a parameter and counts how many dots are in 
# the string. For example, "h.e.l.p." should return 4 dots, and 
# "he.lp." should return 2 dots

#needs to be debugged
def count_dots(name):
    count = []
    for each in name:
        if each == "e":
            total = count.append(each)
    print(count)
# print(count_dots("michael"))




