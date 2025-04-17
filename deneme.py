# Kullanıcıdan her derse ait doğru sayısını isteyen basit LGS puan hesaplama programı

# Toplam puan 500 üzerinden hesaplanacak

# Her testin soru sayısını tanımlıyoruz
mat_soru = 20
turkce_soru = 20
fen_soru = 20
inkilap_soru = 10
ingilizce_soru = 10
din_soru = 10
toplam_soru = 90  # Toplam soru sayısı

# Her sorunun puan karşılığını hesaplıyoruz
puan_per_soru = 500 / toplam_soru  # Her doğru cevap bu kadar puan kazandırır

# Kullanıcıdan doğru sayılarını alıyoruz
mat_dogru = int(input("Matematik doğru sayısı (0-20): "))
turkce_dogru = int(input("Türkçe doğru sayısı (0-20): "))
fen_dogru = int(input("Fen Bilimleri doğru sayısı (0-20): "))
inkilap_dogru = int(input("T.C. İnkılap doğru sayısı (0-10): "))
ingilizce_dogru = int(input("İngilizce doğru sayısı (0-10): "))
din_dogru = int(input("Din Kültürü doğru sayısı (0-10): "))

# Toplam doğru sayısını hesaplıyoruz
toplam_dogru = mat_dogru + turkce_dogru + fen_dogru + inkilap_dogru + ingilizce_dogru + din_dogru

# Toplam puanı hesaplıyoruz
puan = toplam_dogru * puan_per_soru

# Sonucu ekrana yazdırıyoruz
print("Toplam Doğru Sayısı:", toplam_dogru)
print("Yaklaşık LGS Puanınız:", round(puan, 2))  # Virgülden sonra 2 basamak gösteriyoruz
