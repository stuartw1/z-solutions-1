#!/usr/bin/python3

list_ciphertext= ['Wkh#txlfn#eurzq#ir{#mxpsv#ryhu#wkh#od}|#grj1', 'Wklv#lv#dqrwkhu#vhfuhw#vhqwhqfh$', 'Zh#wklqn#ri#vrph#ghpr#gdwd#wr#sxw#lq#wkh#olvw', 'Zh#wkhq#hqfu|sw#lw#dqg#sulqw#wr#wkh#vfuhhq']
list_plaintext=[]

key = input("input key (0 to 5): ")
shift = int(key)

#decrypt
for line in list_ciphertext:
    plaintext_line = ""
    for character in line:
        plaintext_line += chr(ord(character)-shift)
    list_plaintext.append(plaintext_line)

print("Plaintext:")
for line in list_plaintext:
    print(line)