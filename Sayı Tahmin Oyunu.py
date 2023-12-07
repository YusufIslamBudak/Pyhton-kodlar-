
import random
sayac1=0
sayac2=0
o1=input("oyuncu1 adı:")
o2=input("oyuncu2 adı:")
sayi=random.randint(0,100)
print(sayi)

print("0 ile 100 arasında bir sayı girin.")
while True:
    sayac1=sayac1+1
    sayac2=sayac2+1
    tahmin = int(input("{}'in {}. Tahmini :".format(o1,sayac1)))
    if 0<=tahmin<=100:
        if sayi==tahmin:
            print ("Tebrikler ",sayac1," denemede sayıyı buldun",o1)
            break
        elif sayi>tahmin:
            print ("Yukarı çık :)")
        elif sayi<tahmin:
            print ("çok çıktın biraz in")
    else:
        print ("Girdiğiniz sayı 0 ile 100 arasında değil.")


    tahmin2=int(input("{}'in {}. Tahmini :".format(o2,sayac2)))
    print("----------------------------------------------------------------")
    
    if 0<=tahmin<=100:
        if sayi==tahmin:
            print ("Tebrikler ",sayac2," denemede sayıyı buldun",o2)
            break
        elif sayi>tahmin:
            print ("Yukarı çık :)")
        elif sayi<tahmin:
            print ("çok çıktın biraz in")
    else:
        print ("Girdiğiniz sayı 0 ile 100 arasında değil.")


