# my discount

def my_discount():
    try:
        # p is the actual price
        p = int(input("enter price: "))
        print("*************************************\n")
    
        # d is the discount
        d = int(input("enter discount:  "))
        print("****************************************\n")
    except ValueError:
        print("Please enter a digit :)")
        quit()
        
    # price is the discounted price
    # calculating the discounted price
    price = (p - ((d / 100) * p))
    return price

print(my_discount())
print("***********************************************")















