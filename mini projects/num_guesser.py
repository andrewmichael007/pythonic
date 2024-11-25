import random

top_of_range = input("Enter any number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else: 
    print("Please enter number next time.")
    quit()
    
    
rand_num = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue
    
    if user_guess == rand_num:
        print("You got it! :)")
        break
    else:
        print("You got it wrong! :(")
        
print("You got it in" , guesses, "guesses.")


    

