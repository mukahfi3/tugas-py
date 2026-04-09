nama = ["Asep", "Budi", "Cecep"]
nilai = [
    [50, 70, 40, 80],
    [78, 78, 80, 65],
    [57, 88, 67, 69]
]
mata_kuliah = ["MK1", "MK2", "MK3", "MK4"]

#nyari mahasiswa terpintar
rata_tertinggi = 0
mhs_terpintar = ""

for i in range(len(nama)):
    rata = sum(nilai[i]) / len(nilai[i])
    if rata > rata_tertinggi:
        rata_tertinggi = rata
        mhs_terpintar = nama[i]

#nyari mata kuliah terkecil
rata_terkecil = 999
mk_terkecil = ""

for j in range(len(mata_kuliah)):
    total = 0
    for i in range(len(nama)):
        total += nilai[i][j]
    rata = total / len(nama)
    if rata < rata_terkecil:
        rata_terkecil = rata
        mk_terkecil = mata_kuliah[j]

print(f"Mahasiswa Terpintar : {mhs_terpintar} (Nilai :{rata_tertinggi:.2f})")
print(f"Mata Kuliah Nilai Terkecil : {mk_terkecil} (Nilai : {rata_terkecil:.2f})")
