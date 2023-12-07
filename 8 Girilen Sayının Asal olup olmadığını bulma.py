sayi=int(input("SAYI GİR : "))

bolen=0
for i in range(1,sayi+1):
    if sayi%i==0:
            bolen+=1

if bolen==2:
    print("Girilen sayı ASALDIR")
else:
    print("Sayı Asal DEĞİLDİR")
