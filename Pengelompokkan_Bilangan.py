print("=" * 50)
print(" " * 10 + "Nama  = FAVIAN DILAN TRATAMA")
print(" " * 10 + "NIM   = 41037006241050")
print(" " * 10 + "Kelas = A.2/1")
print("=" * 50)

genap = []
ganjil = []

for i in range(1, 11):
    while True:
        try:
            bil = int(input(f"Masukkan bilangan ke-{i}: "))
            break
        except ValueError:
            print("Input harus berupa bilangan bulat. Coba lagi.")
    
    if bil % 2 == 0:
        genap.append(bil)
    else:
        ganjil.append(bil)

jumlah_tuple = (len(genap), len(ganjil))

print(f"Jumlah bilangan genap dan ganjil (sebagai tuple): {jumlah_tuple}")
print(f"Bilangan Genap: {genap}")
print(f"Bilangan Ganjil: {ganjil}")
