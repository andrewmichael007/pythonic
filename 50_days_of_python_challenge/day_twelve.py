#import system
import sys
#create a function called equal_strings
def equal_strings():
    #a try block that catch all valueerrors 
    try:
        string1 = input("enter anything: ")
        print("*******************************************")
        string2 = input("enter something different: ")
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

