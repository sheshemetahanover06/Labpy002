def kalkulator_sederhana():
    print("\n=== Kalkulator Sederhana ===")
    print("Operator yang tersedia:")
    print("+ : Penjumlahan")
    print("- : Pengurangan")
    print("* : Perkalian")
    print("/ : Pembagian")
    
    try:
        # Input angka pertama
        angka1 = float(input("\nMasukkan angka pertama: "))
        
        # Input operator
        operator = input("Masukkan operator (+, -, *, /): ")
        
        # Input angka kedua
        angka2 = float(input("Masukkan angka kedua: "))
        
        # Proses perhitungan menggunakan if elif else
        if operator == '+':
            hasil = angka1 + angka2
            operasi = 'Penjumlahan'
        elif operator == '-':
            hasil = angka1 - angka2
            operasi = 'Pengurangan'
        elif operator == '*':
            hasil = angka1 * angka2
            operasi = 'Perkalian'
        elif operator == '/':
            if angka2 == 0:
                print("\nError: Pembagian dengan nol tidak diperbolehkan!")
                return
            hasil = angka1 / angka2
            operasi = 'Pembagian'
        else:
            print("\nError: Operator tidak valid!")
            return
        
        # Tampilkan hasil
        print("\n=== Hasil Perhitungan ===")
        print(f"Operasi: {operasi}")
        print(f"{angka1} {operator} {angka2} = {hasil}")
        
    except ValueError:
        print("\nError: Masukkan angka yang valid!")
        
# Jalankan program
kalkulator_sederhana()