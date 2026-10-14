'''
Requirements for insurance company:
Base charge $150
Under age of 25 add $50
6 or less accidents $35 per accident
Over 6 accidents, no insurance

'''

# Variables and input
baseCharge = 150
age = int(input("Enter age: "))
accidents = int(input("Enter number of accidents: "))

# Processing (check age and accidents)
if age < 25:
    baseCharge += 50 # += does take what you have and add this

if accidents >= 0 and accidents <= 6:
    baseCharge += 35 * accidents
else:
    baseCharge = 0
    print()

# Output
print("Insurance Cost:", baseCharge)