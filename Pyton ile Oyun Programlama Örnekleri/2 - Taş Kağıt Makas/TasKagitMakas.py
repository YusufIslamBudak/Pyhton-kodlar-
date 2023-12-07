import random

print(("-" * 30) + "\nTaş, Kağıt, Makas\n" + ("-" * 30))

user_score, computer_score = 0, 0

while True:
    print("\n1 - Taş\n2 - Kağıt\n3 - Makas")
    user_choice = input("Seçiminiz: ")
    computer_choice = random.choice(["1", "2", "3"])


    if user_choice == "1" or user_choice=="Taş":
        if computer_choice == "1":
            print("Bilgisayarın Seçimi: Taş\nTaş taşa eşit. Skor Yok!")

        elif computer_choice == "2":
            print("Bilgisayarın Seçimi: Kağıt\nKağıt taşı sarar. Kaybettiniz!")
            computer_score += 100

        elif computer_choice == "3":
            print("Bilgisayarın Seçimi: Makas\nTaş Makası kırar. Kazandınız!")
            user_score += 100

    elif user_choice == "2" or user_choice=="Kağıt":
        if computer_choice == "1":
            print("Bilgisayarın Seçimi: Taş\nKağıt taşı sarar. Kazandınız!")
            user_score += 100

        elif computer_choice == "2":
            print("Bilgisayarın Seçimi: Kağıt\nKağıt kağıta eşit. Skor Yok!")

        elif computer_choice == "3":
            print("Bilgisayarın Seçimi: Makas\nMakas kağıdı keser. Kaybettiniz!")
            computer_score += 100

    elif user_choice == "3" or user_choice=="Makas":
        if computer_choice == "1":
            print("Bilgisayarın Seçimi: Taş\nTaş Makası kırar. Kaybettiniz!")
            computer_score += 100

        elif computer_choice == "2":
            print("Bilgisayarın Seçimi: Kağıt\nMakas kağıdı keser. Kazandınız!")
            user_score += 100

        elif computer_choice == "3":
            print("Bilgisayarın Seçimi: Makas\nMakas makasa eşir. Skor Yok!")

    else:
        break

print("\nSenin Puanın: {}\nBilgisayarın Puanı: {}".format(user_score, computer_score))