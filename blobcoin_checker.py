import os
import hashlib
os.system("cls")
mode = str(input("Blobcoin viewer or blobcoin tester (v/t): "))
if mode == 't':
    blobcoin = str(input("Enter blobcoin: "))
    blobcoin = hashlib.sha256(blobcoin.encode("utf")).hexdigest()
    for x in range(0,11):
        test = ''.join('0' for i in range(x))
        if blobcoin.startswith(test):
            continue
        else:
            os.system("cls")
            if x == 0:
                print("This is not a blobcoin")
                break
            else:
                x -= 1
                print("This is a level %s blobcoin!" % x)
                break
elif mode == 'v':
    blobcoin = str(input("Enter blobcoin: "))
    blobcoin = hashlib.sha256(blobcoin.encode("utf")).hexdigest()
    os.system('cls')
    print("the blobcoin is %s" % blobcoin)