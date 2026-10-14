# Lists
# containers where each item called an element is as an index location
numbers = [4, 3, 9.6, 8.2, 12, 3, 4]

# print the list for quick checks!
print(numbers)

# access each individual element
print(numbers[2])
print(numbers[4])
print(numbers[-1]) # negatives
print(numbers[1:5]) # slice
#print(numbers[10]) # would show and index error, same for negative

# check the length
print("The length of the list", len(numbers))

# loop through a list
for num in numbers:
    print(num, end=" ")
print()

# if we want to modify or adjust values - range for loop
for i in range(len(numbers)):
    numbers[i] *= 1.05 # increase by 5%
    numbers[i] = round(numbers[i], 2)

print(numbers)

# add to end of list
numbers.append("hello there")
numbers.append(4.56)
numbers.append(3)

print(numbers)

# add items at certain index into the list
numbers.insert(4, "Good Afternoon")
print(numbers)