# girilen sayılar içinde yer alan negatif ve pozitif sayıların adedi hesaplar
negatifSay = 0
pozitifSay = 0
print("ÇIKIŞ için 0 giriniz")
while True:
    x = int(input("bir sayı gir: "))
    if x ==0:
        break  
    if x<0:
       negatifSay = negatifSay + 1
    else:
        pozitifSay = pozitifSay + 1
print("Toplam negatif sayı:",negatifSay)
print("Toplam pozitif sayı:",pozitifSay)
    
