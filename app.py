# Hitung Luas Segitiga sederhana
def luas_segitiga():
    a = int(input("Masukkan alas segitiga:"))
    t = int(input("Masukkan tinggi segitiga"))
    luas = a * t /2

    print("Luas segitiga adalah:", luas)
    luas_segitiga()

    # Hitung Luas Persegi Panjang
    def luas_persegi_panjang():
        p = int (input("Masukkan Panjang persegi"))
        l = int (input("Masukkan lebar persegi:"))

        luas = p * l
        print("Luas Persegi adalah: ", luas)
    luas_persegi_panjang()