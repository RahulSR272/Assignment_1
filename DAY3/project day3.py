#Project
#Generate every time a 6 character OTP and print it
import random
import string
id =''
list1=list(string.ascii_letters+string.digits)
for i in range(6):
    id+=random.choice(list1)

print(id)
