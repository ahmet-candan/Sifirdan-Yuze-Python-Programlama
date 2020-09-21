"""ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
fark = ""
for i in ikinci_metin:
    if not i in ilk_metin:
         if not i in fark:
             fark+=i

print(*fark,sep=",")"""

metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""
harf = input("Sorgulamak istediğiniz harf: ")
sayi = ''

for i in metin:
    if harf== i:
        sayi+=i
print(len(sayi))


file = open("C:\\Users\\Lenovo\\Desktop\\python\\python_kitap\\yazi.txt",encoding="UTF-8")
satırlar = file.readlines()

harf = input("Metinde harfinizin kaç tane olduğunu bulmak için harf seçin:")
sayac = 0

for i in satırlar:
    
    for gecici in i:
        if harf==gecici:
            sayac+=1
print("Girdiğiniz {} harfinden {} tane bulunmaktadır".format(harf,sayac))


