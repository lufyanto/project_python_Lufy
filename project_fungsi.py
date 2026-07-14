import os

# Program menghitung luas dan keliling persegi panjang

#membuat header program
"""
os.system('cls')

print(f"{"PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG":^50}")
print("="*50)
print(f"{"Dibuat oleh: Lufyanto Eka Fahrezi":^50}")
print('-'*50,'\n')



LEBAR = int(input("Masukkan Lebar Persegi Panjang\t\t: "))
PANJANG = int(input("Masukkan Panjang Persegi Panjang\t: "))

#Program menghitung luas dan keliling persegi panjang
LUAS = LEBAR * PANJANG
KELILING = 2 * (LEBAR + PANJANG)

#Tampilkan hasil perhitungan
print(f"\nLuas Persegi Panjang\t\t: {LUAS}\n")
print(f"\nKeliling Persegi Panjang\t: {KELILING}")

"""
#DEF DARI HEADER -> INPUT -> HITUNG LUAS -> HITUNG KELILING -> DISPLAY HASIL
def header():
    os.system('cls')
    print(f"{"PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG":^50}")
    print("="*50)
    print(f"{"Dibuat oleh: Lufyanto Eka Fahrezi":^50}")
    print('-'*50,'\n')

def input_user():

    #Mengambil input dari user
    LEBAR = int(input("Masukkan Lebar Persegi Panjang\t\t: "))
    PANJANG = int(input("Masukkan Panjang Persegi Panjang\t: "))
    return LEBAR, PANJANG

def hitung_luas(LEBAR, PANJANG):
    #Program menghitung luas persegi panjang
    LUAS = LEBAR * PANJANG
    return LUAS

def hitung_keliling(LEBAR, PANJANG):
    #Program menghitung keliling persegi panjang
    KELILING = 2 * (LEBAR + PANJANG)
    return KELILING

def display_results(LUAS, KELILING):

    #Tampilkan hasil perhitungan
    print(f"\nLuas Persegi Panjang\t\t: {LUAS}\n")
    print(f"\nKeliling Persegi Panjang\t: {KELILING}")


#PROGRAM UTAMA
while True:
    header()

    LEBAR, PANJANG = input_user()

    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display_results(LUAS, KELILING)

    is_continue = input("\nApakah Anda ingin menghitung lagi? (y/n): ")
    if is_continue.lower() == 'n':
        break

print("\nTerima kasih telah menggunakan program ini!")

#NOTE : KETIKA INGIN MEMBUAT FUNGSI
#HARUS LAH TERPISAH SESUAI DENGAN FUNGSINYA MASING
#SUPAYA PROGRAM LEBIH ENAK DIBACA DAN DIPAHAMI
