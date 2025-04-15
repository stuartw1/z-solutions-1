#!/usr/bin/python3

list_plaintext = ["The quick brown fox jumps over the lazy dog.", "This is another secret sentence!","We think of some demo data to put in the list", "We then encrypt it and print to the screen"]
list_ciphertext = []

key = input("input key (0 to 5): ")
shift = int(key)


for line in list_plaintext:
    ciphertext_line = ""
    for character in line:
        ciphertext_line += chr(ord(character)+shift)
    list_ciphertext.append(ciphertext_line)

print("Ciphertext:")
for line in list_ciphertext:
    print(line)