# this calculates the area and perimeter of a rectangle

def calculateArea(l, w):
    area = l * w
    print("Area:", area)

def calculatePerim(l, w):
    perim = 2 * l + 2 * w
    print("Perimeter:", perim)

# set up variables
length = 6.58
width = 2.65

# output
print("**** Rectangle Calculator****")
print("Length:", length)
print("Width:", width)
print()
calculateArea(length, width)
calculatePerim(length, width)
