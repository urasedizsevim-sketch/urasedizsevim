import time


def s(saniye):
    time.sleep(saniye)
    return 0


sifreli_girdi = input("UESLocker(decoder): ").strip()
tuz_anahtari = int(input("UESLocker(key): "))

ters_listA = {
    1: "A", 2: "B", 3: "C", 4: "Ç", 5: "D", 6: "E", 7: "F", 8: "G", 9: "Ğ",
    10: "H", 11: "I", 12: "İ", 13: "J", 14: "K", 15: "L", 16: "M", 17: "N",
    18: "O", 19: "Ö", 20: "P", 21: "R", 22: "S", 23: "Ş", 24: "T", 25: "U",
    26: "Ü", 27: "V", 28: "Y", 29: "Z", " ": 30, "!": 31, "'": 32, "^": 33,
    "+": 34, "%": 35, "&": 36, "/": 37, "(": 38, ")": 39, "=": 40, "*": 41,
    "?": 42, "-": 43, "_": 44, "|": 45, ",": 46, ".": 47, ":": 48, ";": 49,
    "@": 50, "<": 51, ">": 52, "#": 53, "$": 54, "{": 55, "[": 56, "]": 57,
    "}": 58, "~": 59,
}

print("decoder...")
for _ in range(5):
    s(0.1)

parcalar = sifreli_girdi.split("x")
cozulen_harfler = []

for sira, parca in enumerate(parcalar):
    if parca.isdigit():
        karmasik_sayi = int(parca)

        bulundu = False
        for muhtemel_deger in range(1, 30):
            test_sayisi = (muhtemel_deger * (sira + 1)) + tuz_anahtari + (muhtemel_deger ** 2)

            if test_sayisi == karmasik_sayi:
                if muhtemel_deger in ters_listA:
                    cozulen_harfler.append(ters_listA[muhtemel_deger])
                    bulundu = True
                    break

        if not bulundu:
            cozulen_harfler.append("?")

orijinal_metin = "".join(cozulen_harfler)
print("\n" + "=" * 40)
print("UESLocker: ", orijinal_metin)
print("=" * 40)
