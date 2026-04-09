while True:
    print("\n=== OPERASI MATRIKS ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")
    pilih = input("Pilih menu: ")

    if pilih == "0":
        print("Keluar.")
        break

    baris = int(input("Masukkan baris: "))
    kolom = int(input("Masukkan kolom: "))

    print("Input matriks A:")
    A = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            angka = int(input(f"  [{i}][{j}] = "))
            baris_data.append(angka)
        A.append(baris_data)

    print("Input matriks B:")
    B = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            angka = int(input(f"  [{i}][{j}] = "))
            baris_data.append(angka)
        B.append(baris_data)

    C = []

    if pilih == "1":
        for i in range(baris):
            baris_c = []
            for j in range(kolom):
                baris_c.append(A[i][j] + B[i][j])
            C.append(baris_c)
        print("\nHasil Penjumlahan:")

    elif pilih == "2":
        for i in range(baris):
            baris_c = []
            for j in range(kolom):
                baris_c.append(A[i][j] - B[i][j])
            C.append(baris_c)
        print("\nHasil Pengurangan:")

    elif pilih == "3":
        for i in range(baris):
            baris_c = []
            for j in range(baris):
                total = 0
                for k in range(kolom):
                    total += A[i][k] * B[k][j]
                baris_c.append(total)
            C.append(baris_c)
        print("\nHasil Perkalian:")

    for baris_hasil in C:
        print(baris_hasil)
