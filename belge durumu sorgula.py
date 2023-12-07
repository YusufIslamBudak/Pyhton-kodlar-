#Girilen ortalamaya göre belge durumunu sorgulama
puan = int(input("ORTALAMANIZ\t:   "))

if puan>=85 :
    print("TAKDİR BELGESİ")
elif puan>=70 :
    print("TEŞEKKÜR BELGESİ")
elif puan<70 :
    print(" BELGE YOK!")

