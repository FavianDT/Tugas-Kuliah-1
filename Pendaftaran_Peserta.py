peserta_sah = []

while True:
    nama = input("Masukkan nama peserta (ketik final untuk berhenti): ")
    if nama.lower() == "final":
        break
    try:
        usia = int(input(f"Masukkan usia {nama}: "))
        if usia >= 50:
            peserta_sah.append({"nama": nama, "usia": usia})
        else:
            print("Usia tidak memenuhi syarat.")
    except ValueError:
        print("Usia harus berupa angka. Coba lagi.")

print("\nDaftar Peserta Sah:")
for peserta in peserta_sah:
    print(f"{peserta['nama']} - {peserta['usia']} tahun")
