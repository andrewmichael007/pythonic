# Author : Andy

# Program : control flow deals with if and else statements, for and while loops

# Program Description:

#this program is a simple if or else statement.
# a user is asked for a temperature.
# if temperature is less than 20, program should display it's cold.
# if temperature is greater than 20 and  less than or equal to 50, program should display it's hot.
# if tmepearture is greater than 50, program should display, it's super hot!.

#ask user for temperature
temperature = float(input(("what is the temperature? ")))

#check if temperature is less than or equal to 20 degrees
if temperature <= 20  : 
    #if true, display message
    print("it's cold")

#check if temperature is greater than 20 and less than 5
elif temperature > 20 and temperature < 50 :
    print("it's hot")

#display a message if none of the condtions hold.
else :
    print("it's super hot!")


