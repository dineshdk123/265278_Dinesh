import string
from collections import Counter
import itertools


# #1.getspan(s,ss)-returns the start and end index(span) of substring ss in string s
def getspan(s, sub):
    span = []
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            #print("substring not found")
            break
        end = start + len(sub)
        span.append((start, end))
        start += 1
    return len(span), span

#2.reversewords(s)-Reverse the order of words in s
def reverseword(s):
    print(s[::-1])
# value=input("Enter a reverseword:")
# reverseword("dineshkumar")

#3.removepunctuation(s)-Remove the order of words in s
def removepunctuation(s):
    for i in s:
        if i not in string.punctuation:
            print(i,end="")
# value=input("Enter a punctuation sentence:")
# removepunctuation("value@is a^&python*&sentence&")

#4.countwords(s)- count the number of words in s
def countwords(s):
    splits=s.split()
    length=len(splits)
    print(length)
# value=input("Enter a words:")
# countwords("python training is good")

#5.characterMap(s)-Returns a dictionary with characters of s askeys and frequencies as a value
def characterMap(s):
    return dict(Counter(s))
# value= input("Enter charactermap sentence:")
# result=characterMap("Dineshkumar")
# print(f"mapped characters: {result}")

#6.maketitle(s)-convert s to title case
def makeTitle(s):
    return s.title()
# value= input("Enter maketitle sentence:")
# makeTitle("din kum hjaj")

#7.normalizeSpace(s)-Remove extra spaces ,leaving only single spaces between words
def normalizeSpace(s):
    print(" ".join(s.split()))  
# value=input("Enter a line:")
# normalizeSpace("tha language   is   a to speak")

#8.transform(s)-Reverse the string and swapscase 
def transform(s):
    reverse=s[::-1]
    swapping=reverse.swapcase()
    print(swapping)
# value=input("Enter a transform words:")
# transform("Dinesh")

#9.getpermutation(s)-Return the permutation os s
def getPermutation(s):
    permutations = itertools.permutations(s)
    return sorted(''.join(p) for p in permutations)
# value=input("Enter a permutation words:")
# # result = getPermutation(value)
# print("abc")