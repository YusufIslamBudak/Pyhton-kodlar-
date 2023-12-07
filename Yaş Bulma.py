import datetime
y = int(input("Lütfen doğum yılınızı giriniz : "))
a = int(input("Lütfen doğum ayınızı giriniz: "))
g = int(input("Lütfen doğum gününüzü giriniz : "))

bugun = datetime.datetime.today()
dogumGunu = datetime.datetime(y,a,g)
yas = bugun - dogumGunu 

print("\n\n YAŞAMA SÜRENİZ")
print("GÜN\t :",yas.days )
print("HAFTA\t :",int(yas.days/365*52) )
print("AY\t :",int(yas.days/365*12) )
print("YIL\t :",int(yas.days/365) )




