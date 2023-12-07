bolunen=int(input("Bölünen\t:"))
bolum=int(input("Bölen\t:"))

if bolunen%bolum==0:
    print("{} sayısı, {} sayısını tam bölüyor".format(bolunen,bolum))

if bolunen%bolum!= 0:
    print("{} sayısı, {} sayısını tam bölemez\n".format(bolunen,bolum))
    print("{} sayısının , {} sayısına bölümünden kalan {}'dır.".format(bolunen,bolum,bolunen%bolum))
