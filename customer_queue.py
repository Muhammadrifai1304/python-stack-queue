from collections import deque

queue = deque()  # Membuat antrean kosong

while True:
    print("Pilihan: ")
    print("1. Tambahkan transaksi")
    print("2. Hapus transaksi yang telah dilayani")
    print("3. Tampilkan transaksi berikutnya")
    print("4. Keluar")

    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        name = input("Masukkan nama pelanggan: ")
        transaction_type = input("Masukkan jenis transaksi: ")
        queue.append((name, transaction_type))
        print("Transaksi berhasil ditambahkan ke dalam antrean")

    elif choice == "2":
        if not queue:
            print("Antrean kosong")
        else:
            name, transaction_type = queue.popleft()
            print(f"Transaksi '{transaction_type}' untuk '{name}' telah dilayani dan dihapus dari antrean")

    elif choice == "3":
        if not queue:
            print("Antrean kosong")
        else:
            name, transaction_type = queue[0]
            print(f"Transaksi berikutnya adalah '{transaction_type}' untuk '{name}'")

    elif choice == "4":
        break

    else:
        print("Pilihan tidak valid")
