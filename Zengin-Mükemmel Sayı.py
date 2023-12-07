x=int(input("SAYI 1 : "))
bolen=0
for i in range(1,x):
     if x%i==0:
         bolen+=i

if bolen>x:
    print("zengin sayı")
elif bolen==x:
    print("mükemmel sayı")
else:
    print("normal sayı")
         
