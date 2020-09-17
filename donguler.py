"""  While
Gördügünüz gibi, tekrar degiskeninin degeri her döngüde 1 artıyor. tekrar <= 3 ifadesinin
bool degeri, tekrar adlı degiskenin degeri 3 ‘ü asana kadar hep True olacaktır. Bu degiskenin
degeri 3 ‘ü astıgı anda tekrar <= 3 ifadesinin bool degeri False ‘a dönüyor ve böylece while
döngüsü sona eriyor."""

tekrar = 1
while tekrar <= 3:
    print("tekrar: ", tekrar)
    tekrar += 1
    input("Nasılsınız, iyi misiniz?")
    print("bool değeri: ", bool(tekrar <= 3))


""" range fonkisyonu ile 3 ile 8 karakter arası parola uzunluğu kontrolü"""

while True:
    parola = input("parola belirleyin: ")
    if not parola:
        print("parola bölümü boş geçilemez!")
        break

    elif len(parola) in range(3,9):
        print("Yeni parolanız",parola)

    else:
        print("parola 3 ile 8 karakter arası olmalıdır")


#for döngüsü olmadan range fonksiyonun içindekileri görme
print(*range(10),sep=",")


""" Eval fonkisyonu için izinli_karakterler tanımlayarak kontrol mekanizması oluşturduk"""
izinli_karakterler = "0123456789+-/*= "
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

while True:
    islem = input("işlminizi seçin:")
    if islem == "q":
        break

    else:
        for i in islem:
            if i not in izinli_karakterler:
                print("nabıyonn laaaa")
                quit
        sonuc = eval(islem)
        print(sonuc)
