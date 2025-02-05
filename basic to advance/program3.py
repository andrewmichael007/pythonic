# A program to find the area of a triangle

# input lenght of triangle
base_of_triangle = float(input("enter the base of the triangle: "))


# input height of triangle
height_of_triangle = float(input("enter the height of the triangle: "))


# formulae for triangle
# half * base * height
formulae = 0.5 * base_of_triangle * height_of_triangle

print(f"the area of a triangle with base {base_of_triangle} and height {height_of_triangle} is {formulae} cm square")
