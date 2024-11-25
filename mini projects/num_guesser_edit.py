import random


# generating random numbers using randrange (upper bound  exclusive)
r = random.randrange(-1, 11)
# print(r)


# generating random numbers using randint (upper bound inclusive)
r = random.randint(-1, 11)
# print(r)




# beginning of program
top_of_range = input("Enter any number: ")
print("************************************************\n")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()


# generating a random number
random_number = random.randint(0, top_of_range)

# number of guesses
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    print("**********************************************\n")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)    
    else:
        print("Please enter a number next time.")
        continue
        
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You are above the number!")
        print("******************************************\n")
    else:
        print("You are below the number!")
        print("*******************************************\n")
        
print("**************************************************\n")                   
print("You got it in" , guesses, "guesses.")
print("***************************************************")


    























