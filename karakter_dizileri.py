import locale
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")

"""kardiz = "istihza"

for i in range(len(kardiz)):
    print(kardiz[i])

isim = input("isminiz: ")

for i in range(len(isim)):
    print("isminizin {}. harfi: {}".format(i+1,isim[i]))"""

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])


print(*range(10))

#karakter dizisini ters çevirme
for i in reversed("Sana gül bahçesi vadettim"):
    print(i, end="")
print("\n",*reversed("Sana gül bahçesi vadettim"),sep="")


#Karakter Dizilerini Alfabe Sırasına Dizmek
print(sorted("kitap"))
print(*sorted("kitap"),sep="")

#türkçe karakterlerin doğru  sıralnması için bu malülü kullandık
for i in sorted("çiçek",key = locale.strxfrm):
    print(i,end="")


harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
cevirim = {i:harfler.index(i) for i in harfler}
print(cevirim)

for i in sorted("alşskjdfiı", key=cevirim.get):
    print(i,end="")


#Karakter Dizileri Üzerinde Degisiklik Yapmak

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for i in site1,site2,site3,site4:
    print("https://"+i)

#Diyelim ki, bir kelime içindeki sesli ve sessiz har2eri birbirinden ayırmanız gereken bir program yazıyorsunuz.

sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesli = ""
sessiz = ""

kelime = input("Kelimenizi girin")

for i in kelime:
    if i in sesli_harfler:
        sesli+=i
    elif i in sessiz_harfler:
        sessiz+=i
    
print("Girdiğiniz Kelimedeki Sesli Harfler:",sesli,"\n","Girdiğiniz Kelimedeki Sessiz Harfler:",sessiz)


#ÖNEMLİ 3 FONKSİYON dir() metot bize Python’daki bir nesnenin özellikleri hakkında bilgi edinme imkanı verecek.

for i in dir(""):
    if "_" not in i[0]:
        print(i)


#enumerate()
print(*enumerate("ahmet"))

for sıra, harf in enumerate(dir("")):
    print(sıra,harf)

"""Bu arada, gördügünüz gibi, enumerate() fonksiyonu numaralandırmaya 0 ‘dan baslıyor.
Elbette eger isterseniz bu fonksiyonun numaralandırmaya kaçtan baslayacagını kendiniz de
belirleyebilirsiniz."""
for i,j in enumerate("ahmet candan",1):
    print(i,j)
