print("=" * 50)
print(" " * 10 + "Nama  = FAVIAN DILAN TRATAMA")
print(" " * 10 + "NIM   = 41037006241050")
print(" " * 10 + "Kelas = A.2/1")
print("=" * 50)

menu = {
    "nasi goreng": 15000,
    "mie ayam": 12000,
    "bakso": 14000
}

print("Menu:")
for item, harga in menu.items():
    print(f"- {item.title()} - Rp{harga}")

pesanan = []

while True:
    pilihan = input("Masukkan menu yang dipilih (ketik selesai untuk berhenti): ").lower()
    if pilihan == "selesai":
        break
    elif pilihan in menu:
        pesanan.append(pilihan)
    else:
        print("Menu tidak tersedia. Silakan pilih dari daftar.")

total = sum(menu[item] for item in pesanan)

print(f"Total sebelum diskon: Rp{total}")

if total > 50000:
    total_setelah_diskon = int(total * 0.9)
    print(f"Total yang harus dibayar (setelah diskon 10%): Rp{total_setelah_diskon}")
else:
    print(f"Total yang harus dibayar: Rp{total}")
