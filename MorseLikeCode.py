'''
Created on Dec 3, 2012

@author: Andy
'''

#uses a dictionary to translate a secret language library (using a letter and its translation, separated by
#a space)

def decrypt(library,message):
    d = {}
    word = ""
    for letter in library:
        x = letter.split(" ")
        if x[1] not in d:
            d[x[1]] = x[0]
    for secret in message.split(" "):
        if secret in d:
            word += d[secret]
        else:
            word += "?"
    return word
    
print decrypt(["O ---","S ..."], "... --- ...")