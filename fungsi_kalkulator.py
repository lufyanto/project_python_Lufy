import os

def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    if b == 0:
        return "Tidak bisa membagi dengan nol"
    return a/b

def pangkat(a,b):
    return a ** b

def display_menu():
    os.system('cls')
    print("="*50)
    print(f"{'SELAMAT DATANG DI PROGRAM KALKULATOR':^50}")
    print('-'*50)
    print(f"{'Dibuat oleh: Lufyanto Eka Fahrezi':^50}")
    print(f"{'NIM : 1234678':^50}")
    print('='*50,'\n')

    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pemangkatan")
    print("0. Keluar")

def operasi_kalkulator():
    while True:
        display_menu()
        pilihan = input("Pilih operasi (1-5) atau 0 untuk keluar: ")
        if pilihan == '0':
            print('\n','='*50)
            print(f"{'\nTerima kasih telah menggunakan kalkulator ini':^50}")
            print('\n','='*50)

            break
        if pilihan in ['1', '2', '3', '4', '5']:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
                continue

            if pilihan == '1':
                hasil = tambah(a, b)
                print(f"Hasil penjumlahan: {hasil}")
            elif pilihan == '2':
                hasil = kurang(a, b)
                print(f"Hasil pengurangan: {hasil}")
            elif pilihan == '3':
                hasil = kali(a, b)
                print(f"Hasil perkalian: {hasil}")
            elif pilihan == '4':
                hasil = bagi(a, b)
                print(f"Hasil pembagian: {hasil}")
            elif pilihan == '5':
                hasil = pangkat(a, b)
                print(f"Hasil pemangkatan: {hasil}")

            input("\nTekan Enter untuk melanjutkan...")
        else:
            print("Pilihan tidak valid. Silakan pilih antara 0-5.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    operasi_kalkulator()





        
