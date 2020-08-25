"""
Bu Astro Kod video serisi için hazırlanmış bir modüldür
"""

pi = 3.14159265359


def faktoriyel(sayi):
    """Bu fonksiyon ile Faktöriyel hesaplayabilirsiniz:
    6! = 1 * 2 * 3 * 4 * 5 * 6 = 120
    """
    if sayi >= 0:
        if sayi == 0:
            return 1

        sonuc = 1
        for i in range(1, sayi + 1):
            sonuc *= i
        return sonuc
    else:
        print("Negatif sayılar kullanılamaz")


def derece2rad(aci):
    """Derece'den Radiyan'a dönüşüm
    180 => pi
    """
    return aci * 3.141592 / 180


def rad2derece(aci):
    """Radiyan'dan Derece'ye dönüşüm
    pi => 180
    """
    return aci * 180 / 3.141592


def sin(aci):
    """Bu fonksiyon ile sin hesaplanabilir.
    Açı derece cinsinden girilmeli"""
    aci = derece2rad(aci)
    sonuc = 0
    for i in range(25):
        tek_sayi = 2 * i + 1
        isaret = pow(-1, i)
        deger = isaret * pow(aci, tek_sayi) / faktoriyel(tek_sayi)
        sonuc += deger

    return sonuc


# Bu bölüm, scrip çalıştırıldığında çalışır.
# İçe aktarıldığında çalışmaz
if __name__ == "__main__":
    print(sin(45))
    print(1 / pow(2, 0.5))
