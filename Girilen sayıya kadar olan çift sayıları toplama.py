#Girilen sayıya kadar olan çift sayıları toplama

ciftToplam = 0
x = int(input("bir sayı gir: "))
for simdikiSayi in range(1,x):
        if simdikiSayi%2 ==0:
                ciftToplam = ciftToplam + simdikiSayi
                print(simdikiSayi)
print("toplam: ",ciftToplam)
    
