#Klavyeden girilen not ortalamasına göre belge sorgulama

# ÇÖZÜM 1
puan = int(input("ORTALAMANIZI YAZINIZ\t: "))

if puan>=85 :
    print("TAKDİR BELGESİ")
elif puan>=70 :
    print("TEŞEKKÜR BELGESİ")
elif puan<70 :
    print(" BELGE YOK!")

----------------------------------------------------------

# ÇÖZÜM 2
puan = int(input("ORTALAMANIZI YAZINIZ\t: "))

if puan>=85 and puan<=100 :
    print("TAKDİR BELGESİ")
elif puan>=70 and puan <=84 :
    print("TEŞEKKÜR BELGESİ")
elif puan<70 and puan>=0 :
    print(" BELGE YOK!")
else:
    print("GEÇERLİ BİR NOR GİRİNİZ")

    
----------------------------------------------------------

# ÇÖZÜM 3
puan = int(input("ORTALAMANIZI YAZINIZ\t: "))

if puan<0 or puan>100:
    print("GEÇERLİ BİR NOR GİRİNİZ")
elif 100>=puan>=85 :
    print("TAKDİR BELGESİ")
elif 84>=puan>=70 :
    print("TEŞEKKÜR BELGESİ")
elif puan<70 :
    print(" BELGE YOK!")

