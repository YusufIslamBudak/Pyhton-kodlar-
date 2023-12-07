#Klavyeden girilen sıcaklık değerine göre; Suyun katı-sıvı-gaz hali

t = int(input("sıcaklık giriniz: "))

if t<0:
    hal = "Su katıdır (BUZ) "
elif t>=0 and t<100:
    hal = "Su sıvıdır"
else:
    hal = "Su gazdır (BUHAR) "
print(hal)
