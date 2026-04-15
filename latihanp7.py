def pangkat(a, b):
    hasil = 1
    for i in range(1, b + 1):
        hasil *= a
        print(f"hasil {a} pangkat {i} adalah {hasil}")

def deret(n):
    num, den = 1, 1
    total = 0
    for i in range(n):
        suku = num / den
        if i % 2 == 0:
            total += suku
        else:
            total -= suku
        # update untuk suku berikutnya
        num, den = num + den, den + (num + den)
    print(round(total, 7))

while True:
    print("\nNim Ganjil")
    print("1. A pangkat B")
    print("2. Hitung 1 - 2/3 + 5/8 - 13/21 + ...")
    print("0. keluar")
    pilih = input("Masukkan : ")

    if pilih == "1":
        a = int(input("masukan suatu bilangan bulat : "))
        b = int(input("masukan pangkat yang diinginkan : "))
        pangkat(a, b)
    elif pilih == "2":
        n = int(input("Masukkan jumlah N : "))
        deret(n)
    elif pilih == "0":
        break
