#Klavyeden girilen metni karakter numarasına göre tek ve çift diye iki karakter dizisine aktararak şifreler

#metin="Gün olur alır başımı giderim"
metin=input("Şifrelenecek metni giriniz\t:")

tek=metin[0::2]
print("TEK\t:",tek)
çift=metin[1::2]
print("ÇİFT\t:",çift)

print("ŞİFRELİ METİN :",tek,çift)
sifreli=""
for i in range(len(tek)):
    sifreli+=tek[i]+çift[i]
print("ŞİFRESİ ÇÖZÜLMÜŞ METİN : ",sifreli)
