print("=" * 50)
print(" " * 10 + "Nama  = FAVIAN DILAN TRATAMA")
print(" " * 10 + "NIM   = 41037006241050")
print(" " * 10 + "Kelas = A.2/1")
print("=" * 50)

mahasiswa = {}


for i in range(1, 6):
    nama = input(f"Masukkan nama mahasiswa ke-{i}: ")
    while True:
        try:
            nilai = int(input(f"Masukkan nilai {nama}: "))
            break
        except ValueError:
            print("Nilai harus berupa angka. Silakan masukkan lagi.")
    mahasiswa[nama] = nilai

print("\nData Mahasiswa:")
for nama, nilai in mahasiswa.items():
    print(f"{nama}: {nilai}")

rata_rata = sum(mahasiswa.values()) / len(mahasiswa)
print(f"Rata-rata nilai: {rata_rata:.1f}")

nama_tertinggi = max(mahasiswa, key=mahasiswa.get)
nilai_tertinggi = mahasiswa[nama_tertinggi]
print(f"Mahasiswa dengan nilai tertinggi: {nama_tertinggi} ({nilai_tertinggi})")
