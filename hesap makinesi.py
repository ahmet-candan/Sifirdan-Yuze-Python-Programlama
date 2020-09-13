#id()
a =100
print(id(a))
"""Python’da bu isi yapmamızı saglayacak id() adlı bir fonksiyon bulunur (Ingilizcedeki identity
(kimlik) kelimesinin kısaltması)."""

#is işleci 
a = "python"
print(id(a))
print(id("python"))
print(a is "python")
"""is ve == isleçleri birbirleriyle aynı islevi görmez. Bu iki isleç nesnelerin farklı
yönlerini sorgular: is isleci nesnelerin kimliklerine bakıp o nesnelerin aynı nesneler olup
olmadıgını kontrol ederken, == isleci nesnelerin içerigine bakarak o nesnelerin aynı degere
sahip olup olmadıklarını sorgular."""


#Hesap Makinesi
giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) kare kök hesapla
"""
print(giriş)

while True:
    
    secenek = input("Seçiminizi Girin:")
    if secenek.isdigit()==True:
        
        secenek=int(secenek)
        if(secenek>0 and secenek<7):

            if secenek==1:
                sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
                sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
                print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

            elif secenek==2: 
                sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
                sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
                print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

            elif secenek == 3:
                sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
                sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
                print(sayı5, "x", sayı6, "=", sayı5 * sayı6)
            elif secenek == 4:
                sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
                sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
                print(sayı7, "/", sayı8, "=", sayı7 / sayı8)
            elif secenek == 5:
                sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
                print(sayı9, "sayısının karesi =", sayı9 ** 2)
            elif secenek == 6:
                sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
                print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

        
        else:
            print("Lütfen geçerli bir sayı girin")

    else:
        print("Lütfen geçerli bir sayı girin")
        