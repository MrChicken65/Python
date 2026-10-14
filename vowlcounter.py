# INFO 1020 - Vowel Counter

# get input for a word
text = input("Enter text to count vowels: ")

lowerText = text.lower() # make all letters lowercase

# process- loop through and count vowels
vowelCount = 0 # track vowels
for ch in lowerText:
    if ch == "a" or ch == "e" or ch =="i" or ch == "o" or ch == "u":
        vowelCount += 1
        # You could also do if ch.lower() == ...

# print out the number of vowels
print(f"Vowel Count: {vowelCount}")

vowelCount2 = 0
vowels = "aeiouAEIOU"
for ch in text:
    if ch in vowels:
        vowelCount2 += 1

print(f"Vowel count 2: {vowelCount2}")
