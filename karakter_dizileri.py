kardiz = "istihza"

for i in range(len(kardiz)):
    print(kardiz[i])

isim = input("isminiz: ")

for i in range(len(isim)):
    print("isminizin {}. harfi: {}".format(i+1,isim[i]))
    
    
site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])
    """
    Bu örnek Python’da dilimleme islemlerinin yapısı ve özellikleri hakkında bize epey bilgi
veriyor. Gördügünüz gibi, hem artı hem de eksi degerli sayıları kullanabiliyoruz. Önceki
bölümden hatırlayacagınız gibi, eger verilen sayı eksi degerliyse Python karakter dizisini
sagdan sola (yani sondan basa dogru) okuyacaktır. Yukarıdaki örnekte isim[4:-4] yapısını
kullanarak, site1, site2, site3, site4 adlı karakter dizilerini, ilk dört ve son dört karakterler
hariç olacak sekilde dilimledik. Böylece elimizde ilk dört ve son dört karakter arasındaki bütün
karakterler kalmıs oldu. Yani “google”, “istihza”, “yahoo” ve “gnu”.
"""
