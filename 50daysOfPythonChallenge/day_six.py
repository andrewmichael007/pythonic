def user_name():
    email = input("enter your email: ")
    user_name = email.split('@')[0] 
    return f'Your username is {user_name}'

print (user_name())