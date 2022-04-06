import Game


def HeroSecme():

    print("-------------------------\n"
          "****Hero Seçme Alanı****\n"
          "------------------------\n")
    print("--> Savaşçı --  Can : 30 , Hasarı : 6 , Savunması : 4\n"
          "--> Okçu --  Can : 20 , Hasarı : 8 , Savunması : 3\n"
          "--> Büyücü --  Can : 25 , Hasarı : 7 , Savunması : 2\n")
    while 1 :
        secim = input("Seçeceğin Heronun Baş Harfini Yaz : ")
        secim = secim.upper()
        if secim == 'S':
            print("Bundan Sonra Yola Savaşçı İle Devam Ediceksin..")
            can = 30
            Hasar = 6
            Savunma = 4
            Hero = "Savascı"
            break

        elif secim == 'O':
            print("Bundan Sonra Yola Okçu İle Devam Ediceksin..")
            can = 20
            Hasar = 8
            Savunma = 3
            Hero = "Okcu"
            break

        elif secim == 'B':
            print("Bundan Sonra Yola Büyücü İle Devam Ediceksin..")
            can = 25
            Hasar = 7
            Savunma = 2
            Hero = "Buyucu"
            break

        else :
            print("Yanlış Tuşlama Yaptın...")
            print("Tekrar Dene \n")

    return can,Hasar,Savunma,Hero