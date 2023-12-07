a=int(input("ilk sayı\t:"))
b=int(input("son sayı\t:"))

while a<=b:
    if a*a<=b:
        print("{} sayısının karekökü {} dır.".format(a*a,a))
        a+=1
    else:
        a+=1
