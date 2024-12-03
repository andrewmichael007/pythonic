# this program takes a price and dicount and calculates the discounted price.
# the price and discount takes in numbers only. the program halts if otherwise - the try and catch block takes care of this


def my_discount():
    try:
        # dynamically takes price from the user
        price  = int(input("enter price: "))
        print("*************************************\n")
    
        # dynamically takes discount from the user
        discount = int(input("enter discount:  "))
        print("****************************************\n")
    except ValueError:
        #displays an error message if anything other than a number was entered
        print("Please enter a digit :)")
        quit()
        
    # price is the discounted price
    # calculating the discounted price
    discounted_price = (price - ((discount / 100) * price))
    return discounted_price

print(my_discount())
print("***********************************************")















