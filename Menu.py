import HowToPlay
import Yapimcilar
import Hero
import Game
import Savas


def Login():
      """
      Savas Kısmından Gelen Altını ve Canı Burda Tutuyorum....

      """

      while 1 :

            print("--->Savaş Alanına Gitmek İçin 'S' Tuşuna Bas\n"
            "--->Güvenli Eve  Gitmek İçin 'G' Tuşuna Bas\n"
            "--->Markete Gitmek İçin 'M' Tuşuna Bas\n"
            "--->Yapımcıyı Görmek İçin 'Y' Tuşuna Bas\n"
            "--->Nasıl Oynandığı Hakkında Bilgi Almak İçin 'H' Tuşuna Bas\n"
            "--->Oyundan Çıkmak İçin 'Q' Tuşuna Bas\n"
            "--->Oyunu Sıfırlamak İçin 'R' Tuşuna Bas\n")
            secim = input("Seçimin :: ")
            secim = secim.upper()
            if secim == 'S' :
                  Game.SecimKismi()
                  break
            elif secim == 'G':
                  print("Güvenli Eve Gidicek")
                  break
            elif secim == 'M':
                  print("Markete Gidicek")
                  break
            elif secim == 'Y':
                  Yapimcilar.YapimEkibi()
                  break
            elif secim == 'H':
                  HowToPlay.NasılOynanir()
                  break
            elif secim == 'Q':
                  print("Oyundan Çıkıyor...")
                  exit()
            elif secim == 'R':
                  print("Oyunun Sıfırlanmasını İstediğine Eminmisin..")

                  while 1 :
                        cevap = input("Devam Etmek İçin : (E)\n"
                                      "Menüye Dönmek İçin :(Q)\n"
                                      "Seçimin Nedir :: ")
                        cevap = cevap.upper()
                        if cevap == 'E':
                              print("Oyunu Sıfırlayacak")
                        elif cevap =='Q':
                              print("Menüye Dönülüyor.......\n")
                              Login()
                              break
                        else :
                              print("Yanlış Tuşlama Yaptın Tekrar Dene..")
                              print("\n")

                  break
            else :
                  print("Yanlış Tuşlama Yaptın Tekrar Dene ! ....")
