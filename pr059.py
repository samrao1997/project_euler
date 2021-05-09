"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

import time

f = open("p059_cipher.txt", "r")

if f.mode == "r":
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(x.split(","))
else:
    raise ValueError("Cannot read from file")

finalContents = []
for x in realContents[0]:
    finalContents.append(int(x))


def isAcceptable(myChar):
    return (
        "a" <= myChar <= "z"
        or "A" <= myChar <= "Z"
        or myChar == " "
        or myChar == "'"
        or myChar == ","
        or myChar == '"'
        or myChar == "["
        or myChar == "]"
        or myChar == ":"
        or "0" <= myChar <= "9"
        or myChar == "/"
        or myChar == "."
        or myChar == "("
        or myChar == ")"
        or myChar == ";"
        or myChar == "+"
    )


def projectEulerProblemFiftyNine(cipherText):
    tl = len(cipherText)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    possible = []
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                myGuess = a + b + c
                asciiIndices = [ord(a), ord(b), ord(c)]
                s = ""
                bad = False
                for x in range(tl):
                    myChar = chr(cipherText[x] ^ asciiIndices[x % 3])
                    if not isAcceptable(myChar):
                        bad = True
                        break
                    s += myChar
                if not bad:
                    possible.append(s)
    total = -1
    for x in possible:
        subTotal = 0
        for y in x:
            subTotal += ord(y)
        if total == -1:
            total = subTotal
    return total


start = time.time()
print(projectEulerProblemFiftyNine(finalContents))
print("--- %s seconds ---" % (time.time() - start))
