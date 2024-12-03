#this tool takes a email address, and displays only the username to the user

def user_name():
    #prompts user for email
    email = input("enter your email: ")
    #splits from 0 to the @ symbol
    user_name = email.split('@')[0] 
    return f'Your username is {user_name}'

print (user_name())