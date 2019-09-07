#!/usr/bin/python3

"""
This program implements the Caesar Cipher where the 
data is encrypted by shifting the letters to a specific 
number. That number is the key. If key = 1 
'abc' will be 'bcd' a shifted by one letter b by one and 
c by one
"""

import string

#Varisbles declared

dictionary = {}
out        = open("Cipher.txt","w")                                  # opening file to write o/p
plain      = input("Enter file to encrypt along with path  : ")
key        = int(input("Enter the key to use for Encryption : "))

while ( key > 52 or key < 0 ):
    key = int(input("Enter a Valid Key (0-52) : "))

print("\nEncrypting using the key "+str(key))

for i in range(len(string.ascii_letters)):
    dictionary[string.ascii_letters[i]] = string.ascii_letters[i-key] # initializing the dictionary

with open(plain) as file:   # opening the Plaintext file
    
    while True:
        c = file.read(1)    # Reading a single character
        
        if ( not c ):       # if EOF is reached
            print("Reached EOF stopping")
            break
        if c in dictionary:             # Assigning CipherText
            data = dictionary[c]
        else:
            data = c                    # when spaces and special symbols not in dictionary
        out.write(data)                 # Wriutng output to file
out.close()                             # Closing a file
