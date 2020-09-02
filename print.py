print("""
... [H]=========CANDAN========[-][o][x]
... |                                 |
... | Python Programına Hoşgeldiniz!  |
... | 0'dan 100'e Python Öğreneceğiz  |
... | Devam etmek için herhangi       |
... | bir düğmeye basın.              |
... |                                 |
... |=================================|
... """)

#sep
print("http://", "www.","h4cktimes.","com",sep = "")

#end
print("http://", "www.","h4cktimes.","com",sep = "",end = ".")

#file


# flush parametresine True değerini verdiğimizde dosyayı kapatmadan içine  direk yazar
f = open("deneme.txt","w")
print("hemen yaz",file=f,flush =True)
f.close()

#Yıldızlı Parametreler çıktı L.i.n.u.x
print(*"Linux", sep=".")


#sys.stdout’u Kalıcı Olarak Degistirmek
f = open("dosya.txt", "w")
stdout = f
print("deneme metni", flush=True)


# kaçış dizileri \
baslik = "Türkiyenin Doğalgaz Rezervi"
print(baslik,"\n","-"*len(baslik),sep="")

#Aynı Satır Bası (\r)
print("Merhaba\rDünya") """Burada, “Merhaba” karakter dizisi ekrana yazdırıldıktan sonra \r kaçıs dizisinin etkisiyle satır
basına dönülüyor ve bu kaçıs dizisinden sonra gelen “Dünya” karakter dizisi “Merhaba”
karakter dizisinin üzerine yazıyor."""

#Düsey Sekme (\v)


