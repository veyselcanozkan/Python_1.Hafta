# 1. SINIF Her bir görevi temsil eder
class Gorev:
    def __init__(self, isim):
        self.isim = isim
        self.yapildi_mi = False  # Başlangıçta yapılmadı olarak işaretli

# 2. SINIF Görevleri yöneten ana sınıf
class GorevListesi:
    def __init__(self):
        self.liste = []  # Görevleri tutacak boş liste

    # FONKSİYON 1: Listeye ekleme yapar
    def ekle(self, gorev_ismi):
        yeni_gorev = Gorev(gorev_ismi)
        self.liste.append(yeni_gorev)
        print(f"Eklendi: {gorev_ismi}")

    # FONKSİYON 2: Listeyi ekrana yazar
    def listele(self):
        print("\n--- YAPILACAKLAR ---")
        # Döngü ile listeyi gezer
        for i in range(len(self.liste)):
            gorev = self.liste[i]
            # Duruma göre işaret belirle
            durum = "[X]" if gorev.yapildi_mi else "[ ]"
            print(f"{i+1}. {durum} {gorev.isim}")


    # FONKSİYON 3: Görevi tamamlandı olarak işaretler
    def tamamla(self, numara):
        # Kullanıcı 1 girerse biz 0. indekse bakmalıyız (numara - 1)
        index = numara - 1
        if 0 <= index < len(self.liste):
            self.liste[index].yapildi_mi = True
            print("Görev tamamlandı!")
        else:
            print("Hata: Böyle bir numara yok.")

    # FONKSİYON 4: Görevi listeden siler
    def sil(self, numara):
        index = numara - 1
        if 0 <= index < len(self.liste):
            silinen = self.liste.pop(index)
            print(f"Silindi: {silinen.isim}")
        else:
            print("Hata: Böyle bir numara yok.")


class Gorev:
    def __init__(self, isim):
        self.isim = isim
        self.yapildi_mi = False


class GorevListesi:
    def __init__(self):
        self.liste = []

    def ekle(self, isim):
        yeni_gorev = Gorev(isim)
        self.liste.append(yeni_gorev)
        print("--> Eklendi.")

    def listele(self):
        print("\n--- LİSTE ---")
        for i in range(len(self.liste)):
            gorev = self.liste[i]
            durum = "[X]" if gorev.yapildi_mi else "[ ]"
            print(f"{i+1}. {durum} {gorev.isim}")
        print("\n")

    def tamamla(self, numara):
        index = numara - 1
        if 0 <= index < len(self.liste):
            self.liste[index].yapildi_mi = True
            print("İşaretlendi")
        else:
            print("Hata: Numara yok.")

    def sil(self, numara):
        index = numara - 1
        if 0 <= index < len(self.liste):
            self.liste.pop(index)
            print("Silindi")
        else:
            print("Hata: Numara yok.")

def sistemi_baslat():
    uygulama = GorevListesi()
    
    print("To-Do List Programına Hoşgeldiniz!")

    while True:
        print("1.Ekle 2.Listele 3.Tamamla 4.Sil 5.Çıkış")
        secim = input("Seçiniz: ")

        if secim == "1":
            ad = input("Görev: ")
            uygulama.ekle(ad)
        elif secim == "2":
            uygulama.listele()
        elif secim == "3":
            uygulama.listele()
            no = int(input("Tamamlanan No: "))
            uygulama.tamamla(no)
        elif secim == "4":
            uygulama.listele()
            no = int(input("Silinecek No: "))
            uygulama.sil(no)
        elif secim == "5":
            print("Güle güle...")
            break
        else:
            print("Hatalı tuşlama.")

# En altta sadece fonksiyonu çağırıyoruz. 
# O karışık if bloklarına gerek yok.
sistemi_baslat()