import random
import time

class Kumanda():
    def __init__(self, tv_durumu="Kapalı", tv_ses=0, kanal_listesi = ["Trt"], kanal = "Trt" ):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if (self.tv_durumu == "Açık" ) :
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor...")
            time.sleep(1)
            self.tv_durumu="Açık"


    def tv_kapat(self):
        if(self.tv_durumu == "Kapalı"):
            print("Televizyon zatrn kapalı")
        else:
            print("Televizyon kapatılıyor...")
            time.sleep(1)
            self.tv_durumu="Kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("Sesa Azalt : '<'\nSes Arttırma :'>'\nSessize Al: 'X,x'\nÇıkış için : Çıkış yaz.... ")
            if(cevap=="<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses: ",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses != 60):
                    self.tv_ses +=1
                    print("Ses: ",self.tv_ses)
            elif(cevap == "X" or "x"):
                if(self.tv_ses !=0 or self.tv_ses>0):
                    self.tv_ses = 0
                    print ("Sesize alındı",self.tv_ses)
            else:
                print("ses Güncellendi:" ,self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor")
        time.sleep(2)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")

    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şuan ki kanal: ",self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durumu,
                                                                                          self.tv_ses,
                                                                                          self.kanal_listesi,
                                                                                          self.kanal)
kumanda=Kumanda()
print("""
\t\t\t\tTELEVİZYON UYGULAMASI
*************************************************
[1] Tv Aç

[2] Tv Kapat

[3] Ses Ayarı

[4] Kanal Ekle

[5] Kanal Sayısını Öğrenme

[6] Rastgele Kanal Değiştir

[7] İnfo

Çıkş İşlemi İçin 'Q'ya Basın
************************************************
""")
while True:

    islem=input("İşlem seçiniz:")

    if(islem == "Q"):
        print("Çıkış işleminiz gerçekleşiyor...")
        time.sleep(3)
        break

    elif(islem == "1"):
        kumanda.tv_ac()

    elif(islem == "2"):
        kumanda.tv_kapat()

    elif(islem == "3"):
        kumanda.ses_ayarları()

    elif(islem == "4"):

        kanal_isimleri= input("Kanal İsimlerini ',' İle Ayıraraak Girin...")
        kanal_listesi= kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(islem == "5"):
        print("Kanal sayısı: ",len(kumanda))

    elif(islem == "6"):
        kumanda.rastgele_kanal()

    elif(islem == "7"):
        print(kumanda)

    else:
        print("!!!!!! GEÇERSİZ İŞLEM !!!!!!")


















