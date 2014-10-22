from random import choice
import string 
def genpassword(length,chars = string.letters + string.digits):
    return "".join([choice(chars) for _ in range(length)])
    
for i in range(10):
    print genpassword(12)