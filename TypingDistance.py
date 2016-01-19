'''
Created on Nov 26, 2012

@author: Andy
'''

#returns the number of keys one has to traverse in order to type a message. 
#uses a linear "keyboard" input to check how far apart the letters are

def minDistance(keyboard,word):
    counter = []
    library = []
    for index, letter in enumerate(keyboard):
        library += [(letter, index)]
    print library
    for char in word:
        for letter in library:
            if char in letter:
                print letter[1]
                counter.append(letter[1])
    print counter
    final = 0
    x = 0
    y = 0
    for num in range(len(counter)):
        if num+1 < len(counter):
            final += abs((int(counter[num]) - int(counter[num+1])))
        
    
    return final
        
        
#below a typical qwerty keyboard is represented by the first string. q is the first letter and m
#is the last, so there are 25 keys between them. The word below will have a total distance of 
#1225, or 25 x 49.    
print minDistance("qwertyuiopasdfghjklzxcvbnm","qmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqm")