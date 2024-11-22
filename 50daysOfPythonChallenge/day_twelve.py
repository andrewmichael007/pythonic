import sys
def equal_strings():
    try:
        string1 = input("enter anything: ")
        print("*******************************************")
        string2 = input("enter something different: ")
        print("*********************************************")   
    except ValueError: 
        print("no figures next time please.")
        sys.exit()
        
    if len(string1) == len(string2):
        return 'True'
    else:
        return 'False' 

print(equal_strings())

