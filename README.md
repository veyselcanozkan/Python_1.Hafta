# Python To-Do List Uygulaması

Bu proje, Python programlama dili kullanılarak geliştirilmiş, **Nesne Yönelimli Programlama (OOP)** temellerine dayanan basit bir yapılacaklar listesi uygulamasıdır. Kullanıcı konsol üzerinden görev ekleyebilir, silebilir ve durumunu güncelleyebilir.

## Özellikler

Bu proje aşağıdaki temel işlevleri yerine getirir:
* **Görev Ekleme:** Listeye yeni bir görev ekler.
* **Listeleme:** Mevcut görevleri ve durumlarını (Yapıldı/Yapılmadı) gösterir.
* **Tamamlama:** Seçilen görevi "Tamamlandı" `[X]` olarak işaretler.
* **Silme:** Seçilen görevi listeden kalıcı olarak siler.

## Proje Yapısı ve Gereksinimler

Proje, ödev gereksinimlerine uygun olarak tasarlanmıştır:

1.  **Sınıf (Class) Yapısı:**
    * `Gorev`: Sadece veriyi (görev adı ve durumunu) tutan temel yapı.
    * `GorevListesi`: Görevleri bir liste içinde saklayan ve üzerinde işlem yapan yönetici sınıf.

2.  **Fonksiyonlar:**
    * `ekle()`: Veri girişi sağlar.
    * `listele()`: Verileri görüntüler.
    * `tamamla()`: Veri durumunu günceller.
    * `sil()`: Veriyi listeden atar.

3.  **Akış Kontrolü:**
    * Kullanıcıdan sürekli veri alan ve çıkış yapılana kadar çalışan bir döngü yapısı kurulmuştur.

## Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1.  Bu repoyu indirin veya kopyalayın.
2.  Terminal veya komut satırını açın.
3.  Aşağıdaki komutu yazın:

```bash
python main.py
