# find the first vowel
word = input("Enter word: ")

# find the first vowel
vowels = "aeiouAEIOU"
firstIndex = 0
for i in range(len(word)):
    if word[i] in vowels:
        firstIndex = i 
        break

if firstIndex == 0:
    encryptedText = word + "yay"