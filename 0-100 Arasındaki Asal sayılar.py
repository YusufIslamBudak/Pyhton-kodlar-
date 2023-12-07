for i in range(1,100):
    for j in range(2,i):
        if i%j==0:
            k=i/j
            print("{} esittir {} * {}".format(i,j,int(k)))
            break
    else:
        print(i,"bir asal sayidir")
