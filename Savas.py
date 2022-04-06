import random
import Menu

"""
Rastgele 1 ile 3 arasında sayı uretıp ona göre kaç tane olacagını yazdım 
İlk 4 aşama Kurt Olucak + Sonraki  3 Ayı Olucak+ Sonraki 3 Aslan Olucak 
Kurtların Vereceği Hasar Ve Vereceği Altını Hesaplıcak....
"""
def Kurt(can,hasar,savunma):
    rastegele = random.randint(1, 3)
    Hero_Cani = can
    Hero_Hasari = hasar
    Hero_Savunması = savunma
    Kurt_Sayisi =rastegele
    Kurt_Hasari = 8
    Kurt_Cani = 7*Kurt_Sayisi
    Altın = 0

    print("Her Bir Kurt 5 Altın Vericek ")

    print("Karşında {} Kurt var ...\n"
          "Kurdun Canı : {}.\n"
          "Kurdun Hasarı : {}\n".format(Kurt_Sayisi,Kurt_Cani,Kurt_Hasari))

    print("Canın : {} \n"
          "Hasarın : {}\n"
          "Savunman : {}\n".format(Hero_Cani,Hero_Hasari,Hero_Savunması))

    while 1 :
        print("----> Saldırmak için 'A'\n"
              "----> Savunmak için 'D' \n")
        secim = input("Secimin : ")
        secim = secim.upper()
        """
        Önce Kurda Vurcagı için Kurdun Canı azalıcak 
        Sonra Kurt Ölmez ise Onun Hasarını Hesapladım 
        Heronun canı 0 ve altı olursa oyun biticek
        """
        if secim == 'A':
            Kurt_Cani = Kurt_Cani - Hero_Hasari

            if Kurt_Cani > 0 :
                print("Kurdun Canı : {} \n".format(Kurt_Cani))
                print("Sıra Kurt Hasar Veriyor \n")
                Hero_Cani = Hero_Cani - Kurt_Hasari
                if Hero_Cani <= 0 :
                    print("Öldün ...")
                    exit()
                else :
                    print("Can'ın : {}".format(Hero_Cani))

            else :
                Altın += (Kurt_Sayisi * 5)
                print("{} Altın Kazandın....".format(Altın))
                print("Tebrikler Geçtin ....")
                print("Menüye Dönüyorsun.......")
                print("\n")
                print("CANIN : {}".format(Hero_Cani))

                break
        elif secim == 'D':
            print("Savunma Yaptın.... ")
            print("Canın {} ".format(Hero_Cani))
            KurtYeniHasar = Kurt_Hasari - Hero_Savunması
            print("Kurdun hasarı  {} ' den {} düştü.\n".format(Kurt_Hasari,KurtYeniHasar))
            print("Kurt Vuruyor...\n")
            Hero_Cani = Hero_Cani-KurtYeniHasar
            if Hero_Cani <= 0 :
                print("Öldün...")
                exit()
            else :
                print("Canın : {} kaldı.".format(Hero_Cani))

        else :
            print("Yanlış Tuşlama Tekrar Dene ...")


    """
    Hero Canı Ve altını menu kısmında lazım oldugu ıcın bunları dondurdum ... 
    """
    return Hero_Cani,Altın


"""
Ayı SAYISINI RASTGELE OLUSTURDUM . 

"""
def Ayi(can,hasar,savunma):
    rastgele = random.randint(1,2)
    Hero_Cani = can
    Hero_Hasari = hasar
    Hero_Savunması = savunma
    Ayi_Can = 20 * rastgele
    Ayi_Hasar = 7
    Altın = 0
    Ayi_Sayisi = rastgele

    print("Her Bir Ayı 10 Altın verecek ...")

    print("Karşında {} Ayı var ...\n"
          "Ayının Canı : {}.\n"
          "Ayının Hasarı : {}\n".format(Ayi_Sayisi, Ayi_Can, Ayi_Hasar))

    print("Canın : {} \n"
          "Hasarın : {}\n"
          "Savunman : {}\n".format(Hero_Cani, Hero_Hasari, Hero_Savunması))

    while 1:
        print("----> Saldırmak için 'A'\n"
              "----> Savunmak için 'D' \n")
        secim = input("Secimin : ")
        secim = secim.upper()
        """
        ÖNCE HERO VURUCAK ÜSTTEKİ GİBİ ÖNCE AYININ CANINI DÜSÜRÜP KONTROL ETTİM
        EĞER AYI OLMEZ İSE HERONUN CANINI DUSURUP KONTROL ETTİRDİM..
        AYININ CANI BİTTİĞİNDE HERO KAÇ ALTIN KAZANDIGI GÖSTERILIP MENUYE DONCEK 
        """
        if secim == 'A':
            Ayi_Can = Ayi_Can - Hero_Hasari

            if Ayi_Can > 0:
                print("Ayının Canı : {} \n".format(Ayi_Can))
                print("Sıra Ayı Hasar Veriyor \n")
                Hero_Cani = Hero_Cani - Ayi_Hasar
                if Hero_Cani <= 0:
                    print("Öldün ...")
                    exit()
                else:
                    print("Can'ın : {}".format(Hero_Cani))

            else:
                Altın += (Ayi_Sayisi * 5)
                print("{} Altın Kazandın....".format(Altın))
                print("Tebrikler Geçtin ....")
                print("Menüye Dönüyorsun.......")
                print("\n")
                print("CANIN : {}".format(Hero_Cani))

                break
        elif secim == 'D':
            print("Savunma Yaptın.... ")
            print("Canın {} ".format(Hero_Cani))
            AyiYeni = Ayi_Hasar - Hero_Savunması
            print("Ayının hasarı  {} ' den {} düştü.\n".format(Ayi_Hasar, AyiYeni))
            print("Ayı Vuruyor...\n")
            Hero_Cani = Hero_Cani - AyiYeni
            if Hero_Cani <= 0:
                print("Öldün...")
                exit()
            else:
                print("Canın : {} kaldı.".format(Hero_Cani))

        else:
            print("Yanlış Tuşlama Tekrar Dene ...")

    return Hero_Cani, Altın

"""
ASLAN KISMINI YUKARIDAKI AYI FONKSIYONUNDAN KOPYALADIM USTTEKİ HER ŞEY AŞŞAĞI İÇİNDE GEÇERLİ 


"""
def Aslan(can, hasar, savunma):
    rastgele = 1
    Hero_Cani = can
    Hero_Hasari = hasar
    Hero_Savunması = savunma
    Aslan_Cani = 20 * rastgele
    Aslan_Hasar = 7
    Altın = 0
    Aslan_Sayisi = rastgele

    print("Her Bir Aslan 15 Altın verecek ...")

    print("Karşında {} Aslan var ...\n"
          "Aslanın Canı : {}.\n"
          "Aslanın Hasarı : {}\n".format(Aslan_Sayisi, Aslan_Cani, Aslan_Hasar))

    print("Canın : {} \n"
          "Hasarın : {}\n"
          "Savunman : {}\n".format(Hero_Cani, Hero_Hasari, Hero_Savunması))

    while 1:
        print("----> Saldırmak için 'A'\n"
              "----> Savunmak için 'D' \n")
        secim = input("Secimin : ")
        secim = secim.upper()

        if secim == 'A':
            Aslan_Cani = Aslan_Cani - Hero_Hasari

            if Aslan_Cani > 0:
                print("Aslanın Canı : {} \n".format(Aslan_Cani))
                print("Sıra Aslan Hasar Veriyor \n")
                Hero_Cani = Hero_Cani - Aslan_Hasar
                if Hero_Cani <= 0:
                    print("Öldün ...")
                    exit()
                else:
                    print("Can'ın : {}".format(Hero_Cani))

            else:
                Altın += (Aslan_Sayisi * 15)
                print("{} Altın Kazandın....".format(Altın))
                print("Tebrikler Geçtin ....")
                print("Menüye Dönüyorsun.......")
                print("\n")
                print("CANIN : {}".format(Hero_Cani))

                break
        elif secim == 'D':
            print("Savunma Yaptın.... ")
            print("Canın {} ".format(Hero_Cani))
            AslanYeni = Aslan_Hasar - Hero_Savunması
            print("Aslanın hasarı  {} ' den {} düştü.\n".format(Aslan_Hasar, AslanYeni))
            print("Aslan Vuruyor...\n")
            Hero_Cani = Hero_Cani - AslanYeni
            if Hero_Cani <= 0:
                print("Öldün...")
                exit()
            else:
                print("Canın : {} kaldı.".format(Hero_Cani))

        else:
            print("Yanlış Tuşlama Tekrar Dene ...")

    return Hero_Cani, Altın
