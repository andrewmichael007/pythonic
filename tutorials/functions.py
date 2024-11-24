# a function called test, takes no arguments and prints out a name.
def test():
    print('andy')
# test()

# a function sayMyName, takes one argument and prints it out
def sayMyName(name):
    print(name)
# sayMyName('mitch')

# a function which takes one argument and prints out a greeting.
def greeting(name):
    # print('Hey, ' + name + ' you are welcome!')
    greet = (f"Hey {name}, you're welcome.")
    print(greet)
# greeting('Yo')


def sum(a,b):
    # print(a + b)
    return a + b
# sum(2, 3)

def foodandtipcalculator(food, tip):
    tipPercentage = tip / 100
    tipAmount = food * tipPercentage
    total  =  sum(food, tipAmount) #using the sum function created above
    return total

print(foodandtipcalculator(200, 30))