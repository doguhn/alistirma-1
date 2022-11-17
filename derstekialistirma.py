import random
def sifre(n):
    alfabe=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","w"]
    if type(n)!= str:
         print("Lütf-en bir kelime ya da cümle yazin")
    else:
        t = []
        yenialfabe = []
        sayisayisi = 29
        for i in range(0,29):
            k = random.randint(0,sayisayisi)
            sayisayisi = sayisayisi-1
            yeniharf = alfabe[k]
            sifrelenenharf = alfabe[k]
            alfabe.remove(sifrelenenharf)
            yenialfabe.append(yeniharf)

        alfabe=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","w"]
        yenikelime = ""
        print(yenialfabe)
        print(alfabe)
        for i in range(0,len(n)):
            kelimeninilkharfialfabedekacinci = alfabe.index(n[i])
            t.append(yenialfabe[kelimeninilkharfialfabedekacinci])
        for i in range(0,len(t)):
            yenikelime = yenikelime + t[i] #listedeki yeni kelimemizi birleþtiriyoruz
        print(yenikelime)


sifre("baba")
