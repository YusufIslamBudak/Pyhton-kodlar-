while True:
   giris='''
   1-TOPLA
   2-ÇIKAR
   3-ÇARP
   4-BÖL
   5-KARE
   6-KÖK
   7-MOD
   Çıkış için "exit" yazınız
               '''
   print(giris)
   soru=input("İŞLEM SEÇİNİZ\t:")
   if soru=="1":
      x=int(input("SAYI 1\t:"))
      y=int(input("SAYI 2\t:"))
      print("{} sayısı ile {} sayısının toplamı {} dır.".format(x,y,x+y))

   elif soru=="2":
      x=int(input("SAYI 1\t:"))
      y=int(input("SAYI 2\t:"))
      print("{} sayısı ile {} sayısının farkı {} dır.".format(x,y,x-y))

   elif soru=="3":
      x=int(input("SAYI 1\t:"))
      y=int(input("SAYI 2\t:"))
      print("{} sayısı ile {} sayısının çarpımı {} dır.".format(x,y,x*y))

   elif soru=="4":
      x=int(input("SAYI 1\t:"))
      y=int(input("SAYI 2\t:"))
      print("{} sayısı ile {} sayısının bölümü {} dır.".format(x,y,x/y))

   elif soru=="5":
      x=int(input("SAYI \t:"))
      
      print("{} sayısının karesi {} dır.".format(x,x**2))

   elif soru=="6":
      x=int(input("SAYI \t:"))
      
      print("{} sayısının karekökü {} dır.".format(x,pow(x,0.5)))

   elif soru=="7":
      x=int(input("SAYI 1\t:"))
      y=int(input("SAYI 2\t:"))
      print("{} sayısının {} sayısına modu {} dır.".format(x,y,x%y))
   elif soru=="exit":
      break
   else:
       print("LÜTFEN 1-7 ARASI GEÇERLİ BİR İŞLEM SEÇİNİZ")

