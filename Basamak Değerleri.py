basamakDegeri=1
sayi=int(input("SAYI GİRİNİZ :"))
while sayi>0:
    birler=sayi%10
    sayi=sayi//10
    print("{}'ler basamağı= {}".format(basamakDegeri,birler))
    basamakDegeri*=10
