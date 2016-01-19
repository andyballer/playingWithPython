'''
Created on Nov 26, 2012

@author: Andy
'''

#returns true if words are isomorphic (i.e. letters can be mapped onto other letters)
def iso(a,b):
    if len(a) != len(b):
        return False
    d = {}
    d1={}
    for index in range(len(a)):
        if a[index] not in d:
            d[a[index]] = b[index]
        if b[index] not in d1:
            d1[b[index]] = a[index]
        if a[index] in d:
            if a[index] != d1[b[index]]:
                return False

    print d.keys(), d.values(), d1.keys(), d1.values()
    for item in d.values():
        if d.values().count(item) != d1.keys().count(item):
            return False
    for item in d.keys():
        if d.keys().count(item) != d1.values().count(item):
            return False
    
    else:
        return True


#prints to show how it works when program is run
print iso("abb", "aab")
print iso('abca', 'zbxz')
print iso('aba', 'caa')

#uses the method above to count the number of words in a list that are isomorphic with each other
def countPairs(words):
    counter = 0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if iso(words[i],words[j]) == True:
                counter +=1
    return counter
    
print countPairs(['aab', 'abb', 'cdd', 'ccd'])
print countPairs(["aa", "ab", "bb", "cc", "cd"])