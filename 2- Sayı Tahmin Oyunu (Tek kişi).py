#SAYI TAHMİN OYUNU
import random
sayac=0
sayi=random.randint(0,100)

print("0 ile 100 arasında bir sayı girin.")
while True:
    sayac=sayac+1
    tahmin = int(input("{}. Tahminin :".format(sayac)))
    print("----------------------------------------------------------------")
    
    if 0<=tahmin<=100:
        if sayi==tahmin:
            print ("Tebrikler ",sayac," denemede sayıyı buldunuz")
            break
        elif sayi>tahmin:
            print ("Yukarı çık :)")
        elif sayi<tahmin:
            print ("Çok çıktın biraz in")
    else:
        print ("Girdiğiniz sayı 0 ile 100 arasında değil.")
