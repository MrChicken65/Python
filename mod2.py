# INFO 1020 - Module 2 Notes
# Print stuff (more review)
# Getting user input
# Casting data types
# If statements

num1 = 5
num2 = 12
add = num1 + num2
print(add)
print(num1 + num2)

# variables and text
print("The sum of our number is", add, ".") # comma adds space
print()
print("The sum of our number is " + str(add) + ".") # cast to a string
print()
print("The sum of our number is", add, ".", sep="") # adjust 'sep'
print()
print(f"The sum of our number is {add}.")

# adjust the ending - default \n
print("Hello ", end="")
print("There")

# User Input
name = "John"
name = input("Enter your name: ")
print(f"Hello {name}, hope you have a great day!")

# Input with math
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
#num1 = float(num1)
#num2 = float(num2)

add = num1 + num2
sub = num1 - num2

print(f"The sum of your numbers: {add}")
print(f"The difference of your numbers: {sub}")

# see rectangle calculator and build calculator

# selection statements or decision structures
# boolean expressioins - boolean is True/False
# equality operators == equal to != not equal to
# relational operators > greater than  >= greater than equal to
#                      < less than     <= less than or equal to

# 'if' check this boolean expression

'''
temp = int(input("Enter temperature: "))
if temp <= 50: 
    print("Wear a coat!")
else:
    print("Wear some shorts!")

# check a bunch of stuff with 'else if' - elif
grade = float(input("Enter grade: "))

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
elif grade >= 60:
    print("Grade D")
elif grade >= 0:
    print("Grade F")
else:
    print("Error, incorrect input for grade.")
'''
    
# logical operators - and, or, not
# combine multiple boolean expressions
# and - all have to be true
# or - one has to be true
# not - negates value

temp = int(input("Enter temperature: "))
condition = input("Enter condition(rain, snow, clear): ")

if temp <= 30 or condition == "rain" or condition == "snow":
    print("Wear a coat!")
else:
    print("Wear some shorts")

# See insurance calculator problem
