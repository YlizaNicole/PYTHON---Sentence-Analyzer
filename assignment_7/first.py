#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

import re

def intro ():
    name = input("what is your name?: ")
    name = name.title()
    print ("""Hello {}, this a program that will help you identify the number of words, vowels, and consonants ^___^ """. format(name))

def Info ():
    vowels = 0
    consonant = 0
    str = input ("Input: ")

    for i in range(0, len(str)):
        word =len(re.findall(r'\w+', str))
        
        ch = str[i]

        if ( (ch >= 'a' and ch <= 'z') or
             (ch >= 'A' and ch <= 'Z') ):
             
             ch = ch.lower()
             
             if (ch == 'a' or ch == 'e' or ch == 'i'
                        or ch == 'o' or ch == 'u'):
                vowels += 1
             else:
                consonant += 1

    print ("Word:", word)
    print("Vowels:", vowels)
    print("Consonant:", consonant)

def goodbye ():
    print ("thank you for using this program! ^___^")
    
intro ()
Info ()
goodbye ()