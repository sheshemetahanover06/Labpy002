def hitung_tiket_bioskop():
    # Harga tiket
    HARGA_REGULER = 50000
    HARGA_VIP = 100000
    DISKON_MEMBER = 0.2  # 20%
    
    # Input dari user
    print("\n=== Program Hitung Tiket Bioskop ===")
    print("1. Reguler (Rp50.000)")
    print("2. VIP (Rp100.000)")
    
    while True:
        try:
            pilihan_tiket = int(input("\nPilih tipe tiket (1/2): "))
            if pilihan_tiket in [1, 2]:
                break
            else:
                print("Error: Pilihan tidak valid. Silakan pilih 1 atau 2.")
        except ValueError:
            print("Error: Masukkan angka 1 atau 2.")
    
    while True:
        member = input("Apakah anda memiliki kartu member? (y/n): ").lower()
        if member in ['y', 'n']:
            break
        print("Error: Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    
    # Hitung harga tiket
    if pilihan_tiket == 1:
        harga_dasar = HARGA_REGULER
        tipe_tiket = "Reguler"
    else:
        harga_dasar = HARGA_VIP
        tipe_tiket = "VIP"
    
    # Hitung diskon jika member
    if member == 'y':
        diskon = harga_dasar * DISKON_MEMBER
        harga_akhir = harga_dasar - diskon
        status_member = "Ya"
    else:
        diskon = 0
        harga_akhir = harga_dasar
        status_member = "Tidak"
    
    # Tampilkan rincian pembelian
    print("\n=== Rincian Pembelian ===")
    print(f"Tipe Tiket: {tipe_tiket}")
    print(f"Member: {status_member}")
    print(f"Harga Dasar: Rp{harga_dasar:,}")
    if diskon > 0:
        print(f"Diskon Member: Rp{diskon:,}")
    print(f"Total Bayar: Rp{harga_akhir:,}")

# Jalankan program
hitung_tiket_bioskop()