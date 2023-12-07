#Klavyeden girilen sayının tek yada çift olduğunu bulma

# ÇÖZÜM 1
sayı = int(input("Bir sayı girin: "))

if sayı % 2 == 0:
    print("Girdiğiniz sayı bir çift sayıdır.")
else:
    print("Girdiğiniz sayı bir tek sayıdır.")


# ÇÖZÜM 2
sayı = int(input("Bir sayı girin: "))

if sayı % 2 == 0:
    print("Girdiğiniz sayı bir çift sayıdır.")
elif sayı % 2 == 1:
    print("Girdiğiniz sayı bir tek sayıdır.")


# ÇÖZÜM 3
sayı = int(input("Bir sayı girin: "))

if sayı % 2 == 0:
    print("Girdiğiniz sayı bir çift sayıdır.")
if sayı % 2 == 1:
    print("Girdiğiniz sayı bir tek sayıdır.")
