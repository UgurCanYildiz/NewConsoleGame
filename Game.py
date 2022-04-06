import Hero
import Menu
import Savas
import random


def SecimKismi():
    #Hero secimi can,hasar,savunmayı döndürdü bunları diziye aldım
    """
    Hero Seçimini 1 kere yapmam lazım !!!!
    """
    dizi =Hero.HeroSecme()
    print(dizi)
    can = dizi[0]
    hasar = dizi[1]
    savunma = dizi[2]
    hero = dizi[3]

    print("Hero : {}\nSağlık : {}\nHasar : {}\nSavunma : {}\n".format(hero,can,hasar,savunma))

    """
    Rastgele Dusman secmek icin random ile sayı üretıp bu sayıya gore savas kısmından secım yaparak 
    ılerlemesini sağlıcak.Bu arada savastan kazanarak donmesı halındeki dondurdugum canı ve altını 
    menu kısmında tutuyorum....
    """
    rastgele = random.randint(1,3)
    if rastgele == 1 :
        print("\n")
        Savas.Kurt(can, hasar, savunma)
        degerler = Savas.Kurt(can,hasar,savunma)

    elif rastgele == 2 :
        print("\n")
        Savas.Ayi(can, hasar, savunma)
        degerler = Savas.Ayi(can,hasar,savunma)

    else :
        print("\n")
        Savas.Aslan(can, hasar, savunma)
        degerler = Savas.Aslan(can,hasar,savunma)

    print(degerler)
    """
    Değerleri görmek için ....
    """
    can = degerler[0]
    altın = degerler[1]
    print(can)
    print(altın)
    print("\n")
    print("Menüye Gitmek için 'Q'"
          "Tekrar Savaşmak İçin 'R'")
    while 1 :
        secim = input("Seçim : ")
        secim = secim.upper()
        if secim == 'Q' :
            print("{} canın var .".format(can))
            print("{} altının var.".format(altın))
            print("Menüye gidiyorsunuz....")
            break
        elif secim == 'R':
            print("Canın : {}".format(can))
            print("Savaşa gidiyorsun..")
            rastgele = random.randint(1, 3)
            if rastgele == 1:
                print("\n")
                Savas.Kurt(can, hasar, savunma)
                newdegerler = Savas.Kurt(can, hasar, savunma)

            elif rastgele == 2:
                print("\n")
                Savas.Ayi(can, hasar, savunma)
                newdegerler = Savas.Ayi(can, hasar, savunma)

            else:
                print("\n")
                Savas.Aslan(can, hasar, savunma)
                newdegerler = Savas.Aslan(can, hasar, savunma)
    Menu.Login()
    return altın , can
