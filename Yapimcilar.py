import Menu


def YapimEkibi():
    print("--------------------------\n"
          "Yapımcılar : Uğur Can Yıldız\n"
          "---------------------------\n")
    print("Menüye Dönmek için 'Q'\n"
          "Oyundan Çıkmak İçin 'E'\n")
    while 1 :
        secim = input("Seçimi Yapınız :")
        secim= secim.upper()
        if secim == 'Q':
            print("\n")
            print("Menüye Dönüyorsunuz ....")
            print("\n")
            Menu.Login()
            break
        elif secim == 'E':
            print("\n")
            print("Oyundan Çıkıyor .....")
            print("\n")
            exit()
        else :
            print("\n")
            print("Yanlış Tuşlama Yaptın Tekrar Dene...")
