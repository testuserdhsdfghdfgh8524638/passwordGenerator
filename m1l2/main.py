import random

karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = len(input("Şifre Uzunluğu Kaç Karakter Olsun?: "))
sifre = ""
# kaynak karakterler, şifre uzunluğu , şifre

for i in range(uzunluk):
    sifre += random.choice(karakterler)

print(sifre)
