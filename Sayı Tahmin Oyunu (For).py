#SAYI TAHMİN OYUNU
import random
sayac=0
sayi=random.randint(0,100)

print("0 ile 100 arasında bir sayı girin.\n\n")
for i in range (10,1,-1):
    tahmin = int(input("{}. Tahmin hakkın kaldı :".format(i)))
    print("----------------------------------------------------------------")
    
    if 0<=tahmin<=100:
        if sayi==tahmin:
            print ("Tebrikler ",10-i+1," denemede sayıyı buldunuz")
            break
        elif sayi>tahmin:
            print ("Yukarı çık :)")
        elif sayi<tahmin:
            print ("Çok çıktın biraz in")
    else:
        print ("Girdiğiniz sayı 0 ile 100 arasında değil.")
