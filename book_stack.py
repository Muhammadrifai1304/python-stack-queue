# buat tumpukan kosong untuk buku
tumpukan_buku = []

while True:
    print("1. Tambahkan buku")
    print("2. Hapus buku terakhir")
    print("3. Tampilkan buku teratas")
    print("4. Keluar")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        nama_buku = input("Masukkan nama buku: ")
        pengarang = input("Masukkan nama pengarang: ")
        tumpukan_buku.append((nama_buku, pengarang))
        print("Buku berhasil ditambahkan ke tumpukan")

    elif pilihan == 2:
        if len(tumpukan_buku) == 0:
            print("Tumpukan buku kosong")
        else:
            buku_terakhir = tumpukan_buku.pop()
            print(f"{buku_terakhir[0]} oleh {buku_terakhir[1]} berhasil dihapus dari tumpukan")

    elif pilihan == 3:
        if len(tumpukan_buku) == 0:
            print("Tumpukan buku kosong")
        else:
            buku_teratas = tumpukan_buku[-1]
            print(f"Buku teratas: {buku_teratas[0]} oleh {buku_teratas[1]}")

    elif pilihan == 4:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
