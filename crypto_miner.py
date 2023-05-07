import random
import string
import hashlib
from concurrent.futures import ProcessPoolExecutor
question = str(input("Do you want to have the easy copy paste option on? (y/n): "))
repeat = int(input("how many blobcoin do you want to find?: "))
letter = str(string.ascii_lowercase)
dif = int(input("Enter difficulty level: "))
digit = int(input("Enter number of digits does the tested numbers should have: "))
check = ''.join('0' for i in range(dif))
x = 0
while x < repeat:
    a = ''.join(random.choice(letter) for b in range(digit))
    c = hashlib.sha256(a.encode("utf")).hexdigest()
    if c.startswith(check):
        if x != -1:
            x += 1
        if question == 'y':
            print(a)
        else:
            print("you found a difficulty %s" % dif + " blobcoin! it is: %s" % a)