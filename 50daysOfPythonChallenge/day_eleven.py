def hide_password():
    password = input("enter password: ")
    hid_password = len(password) * " * " 
    return f"Your password is {password} and it's {len(password)} characters long."
              
print(hide_password())

  