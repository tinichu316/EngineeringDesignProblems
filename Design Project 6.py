#Week 8: Caeser Cipher

#Read in a message and a key and write the encrypted message to a file (.txt)

#Read the encryped file, decrypt it, and print out the secret message.

filepath = "../MiscResources/cipher.txt"

def code(txt, k, type):
    """Shifts each letter of the text k times to the right(or left) and returns it."""
    txt = txt.upper()
    if type == 'e':
        #encode
        type = 1
    elif type == 'd':
        type = -1
    else:
        raise Exception('invalid keyword. use (e)ncrypt or (d)ecrypt')
    #note that ord('A') = 65, ord('Z') = 90. We use chr to get it back.
    coded = ''
    for char in txt:
        ind = ord(char) + type*k
        if 64 < ord(char) < 91: #if the char is in the alphabet
            if ind > 90:
                newind = ind - 26
            elif ind < 65:
                newind = ind + 26
            else:
                newind = ind
        else:
            newind = ord(char) #punctuation, spaces, etc
        coded += chr(newind)
    return coded

def saveText(txt, filepath):
    """Saves the txt to the file"""
    file = open(filepath, 'w')
    file.write(txt)
    
def readText(filepath):
    """Returns each line of the file as a list"""
    file = open(filepath, 'r')
    return file.readlines()

def encodeSave(txt, k, filepath):
    saveText(code(txt, k, 'e'), filepath)
    
def decodeOpen(k, filepath):
    lines = readText(filepath)
    for line in lines:
        print(code(line, k, 'd'))

