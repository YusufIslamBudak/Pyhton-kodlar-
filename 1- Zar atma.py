
import random

while True :
    #input()
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    
    print(" {} - {} attınız".format(zar1,zar2))
    if zar1 == 6 and zar2 == 6:
        print("Kazandınız")
        break
