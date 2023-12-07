#PUANA GÖRE NOT
#Klavyeden girilen notun hangi puana denk geldiğini bulma

puan = int(input("ORTALAMANIZI YAZINIZ\t: "))

if puan>=85 :       # Hatalı sonuçlar verir
    print("BEŞ")    # Örneğin 88 girildiğinde ; BEŞ DÖRT ÜÇ İKİ yazar
if puan>=70 :
    print("DÖRT")
if puan>=60 :
    print("ÜÇ")
if puan>=50 :
    print("İKİ")
if puan<50 :
    print("BİR")

----------------------------------------------------------
#ÇÖZÜM 1
puan = int(input("ORTALAMANIZI YAZINIZ\t: "))

if puan>=85 and puan<=100 :
    print("BEŞ")
elif puan>=70 and puan<=84 :
    print("DÖRT")
elif puan>=60 and puan<=69:
    print("ÜÇ")
elif puan>=50 and puan<=59 :
    print("İKİ")
elif puan<50 and puan>=0 :
    print("BİR")

else:
    print("GEÇERLİ BİR NOT GİRİNİZ")
----------------------------------------------------------
#ÇÖZÜM 2:
puan = int(input("ORTALAMANIZI YAZINIZ\t: "))

if 85<=puan<=100 :
    print("BEŞ")
elif 70<=puan<=84 :
    print("DÖRT")
elif 60<=puan<=69 :
    print("ÜÇ")
elif 50<=puan<=59 :
    print("İKİ")
elif 0<=puan<=50 :
    print("BİR")

elif puan<0 or puan>100:
    print("GEÇERLİ BİR NOT GİRİNİZ")
