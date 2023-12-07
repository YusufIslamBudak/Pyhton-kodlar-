#SAYI TAHMİN OYUNU
import random
sayi=random.randint(0,100)
oyuncu1=input("OYUNCU 1 İÇİN İSİM GİRİNİZ : ")
oyuncu2=input("OYUNCU 2 İÇİN İSİM GİRİNİZ : ")

oyuncu = [ ]
oyuncu.append(oyuncu1)
oyuncu.append(oyuncu2)

print ("\nBaşarılar {} ve {} ".format(oyuncu[0], oyuncu[1]))

print("\n 0 ile 100 arasında bir sayı tuttum. Haydi bulmaya çalışın .\n\n")
for i in range (10,1,-1):
    sira = i %2
    tahmin = int(input("Söyle {} :".format(oyuncu[sira])))
    print("..................................................................")
    
    if 0<=tahmin<=100:
        if sayi==tahmin:
            print ("Tebrikler {} \n Oyunu  Kazandın :) ".format(oyuncu[sira]))
            break
        elif sayi>tahmin:
            print ("Yukarı çık :)")
        elif sayi<tahmin:
            print ("Çok çıktın biraz in")
    else:
        print ("Girdiğiniz sayı 0 ile 100 arasında değil.")
