#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

import re
def intro():
    print ("Please input yout username and password that is with")
    print ("with a Character more than 15 ")
    print ("at least one capital letter")
    print ("at least one number")
    print ("at least one special char (!@#$%^&*()_+ etc)")

def user ():
    input ("username: ")
    pas= input("password: ")
    pw= True
    while pw:
        if  16 >= len(pas):
            break
        elif not re.search("[a-z]",pas):
            break 
        elif not re.search("[0-9]",pas):
            break
        elif not re.search("[A-Z]",pas):
            break
        elif not re.search("[$#@]",pas):
            break
        elif re.search("\s",pas):
            break
        else:
            print("valid")
            pw= False
            break
    if pw:   
        print("Not a Valid Password")
        return user()

def goodbye ():
    print ("your username and password is valid you may now continue")


intro ()
user ()
goodbye ()