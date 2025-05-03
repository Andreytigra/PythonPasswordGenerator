import string
import random
import time

chars1=string.ascii_lowercase + string.ascii_uppercase + string.digits
chars2=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
chars3=string.digits + string.punctuation

size = input('Input lenght: ')
size = int(size)
print('Choose variant | 1 = letters + numbers | 2 = all | 3 = Numbers')
charsint = input('')
charsint = int(charsint)

time.sleep(1)
#Generate password
if charsint == 1:
    password = (''.join(random.choice(chars1) for _ in range(size)))
elif charsint == 2:
    password = (''.join(random.choice(chars2) for _ in range(size)))
elif charsint == 3:
    password = (''.join(random.choice(chars3) for _ in range(size))) 

print('This console will be closed in 15 second')
print(password)    
time.sleep(15) 
