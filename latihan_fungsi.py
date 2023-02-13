'''fungsi pada python didefinisikan dengan def'''

'''def nama_fungsi():'''

def salam():
    print("assalamu'alaikum !! akhi ukhty")

salam()
salam()
salam()

'''buatlah sebuah fungsi versi kalian'''

def jawab():
    print("wa'alaikumsalam")

jawab()
jawab()
jawab()

'''fungsi dengan parameter'''
'''def nama_fungsi(p1, p2)'''

def say_hi(nama):
    print("halo perkenalkan nama saya", nama)

say_hi("jawir")
say_hi("ambatukam")

'''buatlah fungsi dengan 3 parameter'''

def hy(nama,umur,kelas):

    print("halo nama saya:",nama)
    print("umur:",umur)
    print("kelas:",kelas)

hy("sadam","17","10")
hy("dhafin","16","10")
hy("dayat","17","10")

'''buatlah program menghitung luas banggun datar menggunakan fungsi.gunakam parameter
-segitiga
-persegi panjang
'''

def segitiga(alas,tinggi):
    luas = alas*tinggi/2
    print("luas segitiga adalah:%i cm"%luas)
segitiga(15,20)

def persegi_panjang(panjang,lebar):
    luas = panjang*lebar
    print("luas persegi panjang adalah:%i cm"%luas)


