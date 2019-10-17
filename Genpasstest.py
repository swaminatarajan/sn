# -*- coding: utf-8 -*-
import string
from random import *

passwordLength = randint(5, 9)
print ("my password length : ", passwordLength)




allowedSpecialChars = ("*","&", "$")

characters = string.ascii_letters + choice(allowedSpecialChars) + string.digits
password =  "".join(choice(characters) for x in range(1,passwordLength+1))
print ("password", password)
