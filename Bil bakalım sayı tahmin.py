import random
sayi=random.randint(1,100)
sayac=0
anahtar=1
while anahtar==1:
    tahmin=int(input("TAHMİN ET BAKALIM : "))
    sayac+=1
    if tahmin<sayi:
        print("Tahmin ettiğim sayı daha daha büyük...")
    elif tahmin>sayi:
        print("Tahmin ettiğim sayı daha daha küçük...")
    elif tahmin== sayi:
        print("Tebrikler {} adımda bildiniz".format(sayac))
        anahtar=0
        

# AŞAĞIDAKİ KODLAR DA AYNI GÖREVİ GÖRMEKTEDİR

#sayi=45
#sayac=0
#while True:
#    tahmin=int(input("TAHMİN ET BAKALIM : "))
#    sayac+=1
#    if tahmin<sayi:
#        print("Tahmin ettiğim sayı daha daha büyük...")
#    elif tahmin>sayi:
#        print("Tahmin ettiğim sayı daha daha küçük...")
#    elif tahmin== sayi:
#        print("Tebrikler {} adımda bildiniz".format(sayac))
#        break
