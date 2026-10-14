# INFO 1020 - String Data Type Concepts

# String literals - we can use "" or '' quotes
name = "Lucas"
name1 = 'Tom'

# set of 3 creates text block
someText = """This is a text block. You can type all kinds of text
This is another line of our text
One more line"""

''' # This is a multiline comment
print(name)
print(name1)
print(someText)
'''

# Access individual characters via their index
fruit = "banana"
#        012345

# use square brackets - []
print(fruit[2])
print(fruit[4])

# work from the back with negative indexes
print(fruit[-1])
print(fruit[-2])

# length function - len()
print(len(fruit))
print(len(someText))

middleIndex = len(fruit) // 2
print(fruit[middleIndex])

if len(fruit) % 2 == 0: # if even length word- two middle letters
    print(fruit[middleIndex-1]+fruit[middleIndex])
else: # Otherwise get one
    print(fruit[middleIndex])

# Grab multiple characters - use slices - substrings
print(fruit[2:4]) # First number includes, the last excludes
print(fruit[2:5])
print(fruit[:3])
print(fruit[4:])

# looping through a word - 2 ways

# counter control loop - good for getting index locations
for i in range(len(fruit)): # 0, 1, 2, 3, 4, 5
    print(fruit[i], end=" - ")
print()
# for each loops - great for access only
for ch in fruit:
    print(ch, end=" - ")