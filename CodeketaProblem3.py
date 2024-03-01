#Prbloem 3 
#You are given the coefficients of a quadratic equation in order A, B & C.

# Where A is the coefficient of X2,  B is the coefficient of X and C is the constant term in the most simplified form.

# Example: For  X2 + 5X + 6 = 0, you are given the input as: 1 5 6.

# Write a program to find all of the roots of the quadratic.

# Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.

# Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a

# Input Description:
# Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order

# Output Description:
# Print the two values of X after rounding off to 2 decimal places if required.

# Sample Input :
# 1 5 6
# Sample Output :
# -2.00
# -3.00

#Solution

import math

# Taking input from the user
A, B, C = map(int, input().split())

# Calculating the discriminant
D = B**2 - 4*A*C

# Checking if the discriminant is negative (complex roots)
if D < 0:
    # Converting to imaginary part
    D = abs(D)
    real_part = round(-B / (2*A), 2)
    imaginary_part = round(math.sqrt(D) / (2*A), 2)
    # Printing roots in complex form
    print(f"{real_part:.2f}+{imaginary_part:.2f}i")
    print(f"{real_part:.2f}-{imaginary_part:.2f}i")
else:
    # Calculating the roots
    root1 = round((-B + math.sqrt(D)) / (2*A), 2)
    root2 = round((-B - math.sqrt(D)) / (2*A), 2)
    # Printing the roots
    print(f"{root1:.2f}")
    print(f"{root2:.2f}")
