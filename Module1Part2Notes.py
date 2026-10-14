# Module 1 - Part 2 Notes

# basic for loop
for i in range(10):
    print("Hello")
print()

# Watch the value of j
for j in range(5):
    print(j)
print()

# Adjust start value
for i in range(1, 6):
    print(i)
print()

# Adjust the step value
for i in range(0, 21, 2):
    print(i)
print()

# Counting down
for i in range(5, 0, -1):
    print(i)
print()

# Fun nested loops
for i in range(1, 11):
    for j in range(1,11):
        print(i * j, " ", end="")
    print()

# ****** Functions ******
# to write functions use def - name the function - name parameters
def printWelcome():
    print("Hello and welcome to class")


def printWelcomeName(name):
    print("Hello,", name, "welcome to class")

printWelcome()

printWelcomeName("Lucas")
name = "Michael"

printWelcomeName(name)