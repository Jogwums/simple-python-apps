import string
import random

def gen():
    str1 = string.ascii_uppercase
    str2 = string.ascii_lowercase
    str3 = string.digits
    str4 = string.punctuation
    
    passlen = int(input("Enter the password length:\n"))

    s = []
    s.extend(str1)
    s.extend(str2)
    s.extend(str3)
    s.extend(str4)

    random.shuffle(s)
    
    passwrd = ("".join(s[0:passlen])) 

    print(passwrd)
gen()