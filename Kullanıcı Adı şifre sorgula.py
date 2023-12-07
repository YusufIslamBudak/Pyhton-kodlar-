kullanıcı=input("Kullanıcı:")
sifre=input("Şifre:")

if kullanıcı and sifre:             #Kulllanıcı adı ve şifre girilmişse
    if kullanıcı=="admin":           #Kullanıcı adı admin ise
        if sifre=="1234":           #Şifre 1234 ise
            print("Merhaba")
        else:                       #Şifre 1234 degilise       
            print("Yanlış Şifre")
    else:                           #Kullanıcı adı admin değilse
        print("Yanlış kullanıcı adı")
else:                                       #Kullanıcı adı veya şifre girilmemişse
    print("Kullanıcı adı veya şifre boş olamaz")

