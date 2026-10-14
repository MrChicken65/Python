# Template

def substitutionEncrypt(plainText, key):
    import string # import string function to get lowercase alphabet
    alphabet = string.ascii_lowercase + key # Adds the alphabet
    plainText = plainText.lower() # Lowers it
    
    cipherText = ""   # Set up blank string
    for ch in plainText: # loops through character by character
        idx = alphabet.find(ch) # Finds the position in the key
        cipherText = cipherText + key[idx] # adds the encrypted letter 
    
    return cipherText # sends it back to get printed

# Decryption function: 
def substitutionDecrypt(encryptedText, key):
    import string # Imports string function to get a lowercase alphabet
    alphabet = string.ascii_lowercase # Adds the alphabet
    encryptedText = encryptedText.lower() # Converts to lowercase
    
    plainText = ""   # Makes a blank string for it
    for ch in encryptedText: # Loops through it letter by letter
        idx = key.find(ch) # Finds the position of the scrambled letter
        if idx != -1: # checks to make sure the character is within the key
            plainText = plainText + alphabet[idx] #Adds the letter
        else:
            plainText = plainText + ch #If it's a space or symbol, it just gets added as is
    
    return plainText # sends the plaintext back as the output to be printed

#'''
print("Welcome to the text decrypter!")
userChoice = float(input("Enter 1 for encrypt or 2 for decrypt: "))

if userChoice == 1:
    plainText = input("Enter text to encrypt: ")
    key = input("Enter the key: ")
    print(substitutionEncrypt(plainText, key))
elif userChoice == 2: 
    encryptedText = input("Enter encrypted text: ")
    key = input("Enter the key: ")
    print(substitutionDecrypt(encryptedText, key))
#'''