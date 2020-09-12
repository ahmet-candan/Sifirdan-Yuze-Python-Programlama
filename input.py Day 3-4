#len fonksiyonu sayılarla birlikte kullanılmaz
sayı = 12343423432
kardiz = str(sayı)
print(len(kardiz))

#complex()
print(complex(15))

###############eval() ile Doğalgaz Faturası Hesaplama####################33
#Her bir ayın kaç gün çektiğini tanımlıyoruz
ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28

#Doğalgazın vergiler dahil metreküp fiyatı
birimFiyat = 0.79
#Kullanıcı ayda ne kadar doğalgaz tüketmiş?
aylıkSarfiyat = input("Aylık doğalgaz sarfiyatınızı metreküp olarak giriniz: ")

#Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")

ay = eval(dönem)

#Kullanıcının günlük doğalgaz sarfiyatı
günlükSarfiyat = int(aylıkSarfiyat) / ay
#Fatura tutarı
fatura = birimFiyat * günlükSarfiyat * ay
print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
"tahmini fatura tutarı: \t", fatura, " TL", sep="")

###################################################################

###################  eval() ile Hesap Makinesi #####################3

print("""
Basit bir hesap makinesi uygulaması.
İşleçler:
+ toplama
- çıkarma
* çarpma
/ bölme
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")
islem = input("İşleminiz:")
sonuc = eval(islem)
print(islem," işleminin sonucu: ",sonuc,"")

