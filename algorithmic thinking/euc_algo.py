def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 12
num2 = 6
gcd = euclidean_algorithm(num1, num2)
print("The GCD of", num1, "and", num2, "is:", gcd)



# def euclidean_algorithm(a, b):
    # This function takes two integers, a and b, and calculates their greatest common divisor (GCD)
    # while b != 0: 
        # Continue looping until b becomes 0
        # a, b = b, a % b
        # Update the values of a and b:
        # a is set to the current value of b
        # b is set to the remainder of dividing the previous value of a by the previous value of b
    # return a
    # Once b becomes 0, return the current value of a, which is the GCD

# Example usage:
# num1 = 48
# num2 = -18
# Define two numbers for which we want to find the GCD

# gcd = euclidean_algorithm(num1, num2)
# Call the euclidean_algorithm function with num1 and num2 as arguments and store the result in gcd

# print("The GCD of", num1, "and", num2, "is:", gcd)
# Print the result, indicating the GCD of num1 and num2




