import random

listA = {
    "A": 1, "B": 2, "C": 3, "Ç": 4, "D": 5, "E": 6, "F": 7, "G": 8, "Ğ": 9,
    "H": 10, "I": 11, "İ": 12, "J": 13, "K": 14, "L": 15, "M": 16, "N": 17,
    "O": 18, "Ö": 19, "P": 20, "R": 21, "S": 22, "Ş": 23, "T": 24, "U": 25,
    "Ü": 26, "V": 27, "Y": 28, "Z": 29, " ": 30, "!": 31, "'": 32, "^": 33,
    "+": 34, "%": 35, "&": 36, "/": 37, "(": 38, ")": 39, "=": 40, "*": 41,
    "?": 42, "-": 43, "_": 44, "|": 45, ",": 46, ".": 47, ":": 48, ";": 49,
    "@": 50, "<": 51, ">": 52, "#": 53, "$": 54, "{": 55, "[": 56, "]": 57,
    "}": 58, "~": 59,
}

def ues_sifrele(metin):
    metin = metin.upper().replace("i", "İ").replace("ı", "I")
    
    tuz_anahtari = random.randint(100, 999)
    sifreli_liste = []
    
    for sira, harf in enumerate(metin):
        if harf in listA:
            orijinal_deger = listA[harf]
            karmasik_sayi = (orijinal_deger * (sira + 1)) + tuz_anahtari + (orijinal_deger ** 2)
            sifreli_liste.append(str(karmasik_sayi))

    sifreli_metin = "x".join(sifreli_liste)

    dosya = open("history.txt", "a", encoding="utf-8")
    dosya.write("\n\nmetin:\n" + metin)
    dosya.write("\nşifreli metin:\n" + sifreli_metin)
    dosya.write("\nkey'i:\n" + str(tuz_anahtari))
    dosya.close()
    
    return sifreli_metin, tuz_anahtari
 
