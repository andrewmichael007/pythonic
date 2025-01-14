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

# print(foodandtipcalculator(200, 30))

#  Numbers Manipulation

# this tool takes an array of numbers and logs each of them out
def numbersManipulate(numbers):
    for each in numbers:
        print(each)
# numbersManipulate([2,4,6,8,10])

print("********************************")
# this tool takes an array of numbers  multiplies each by 2 and logs out the new result
def numbersManipulate2(numbers):
    for each in numbers:
        manipulated = each * 2
        print(manipulated)
numbersManipulate2([2,4,6,8,10])



