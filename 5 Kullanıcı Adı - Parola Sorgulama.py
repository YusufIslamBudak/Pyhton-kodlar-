#Klavyeden girilen kullanıcı adı ve parolanın önceden belirlenen
#kullanıcı adı ve parola ile eşleşmesini bulma

    
kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız: ")

if kullanıcı_adı == "aliveli" and parola == "1234":
    print("Programa hoşgeldiniz")
else:
    print("Yanlış kullanıcı adı veya parola! hatalı")
    
----------------------------------------------------------
#ÇÖZÜM 1
    
kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız: ")

if kullanıcı_adı == "aliveli" and parola == "1234":
    print("Programa hoşgeldiniz.Kullanıcı adı ve Parola DOĞRU")
elif kullanıcı_adı == "aliveli" and parola != "1234":
    print("Kullanıcı adı doğru , Parola! hatalı")
elif kullanıcı_adı != "aliveli" and parola == "1234":
    print("Parola doğru, Kullanıcı Adı! hatalı")
elif kullanıcı_adı != "aliveli" and parola != "1234":
    print("Kullanıcı Adı hatalı ve Parola hatalı")
