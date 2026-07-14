celcius = int(input("Masukkan celcius yg mau diubah: "))

print("===== PROGRAM KONVERTER CELCIUS =====")
print("1. Celcius ke Kelvin")
print("2. Celcius ke Reamur")
print("3. Celcius ke Farenheit")

pilihan = input("Pilih salah satu (Ketik 1/2/3): ")

if pilihan == "1":
    a = celcius + 273
    b = "Kelvin"
if pilihan == "2":
    a = 9/5 * celcius + 32
    b = "Reamur"
if pilihan == "3":
    a = 4/5 * celcius
    b = "Farenheit"
else:
    print("ERROR")

print("===== PROGRAM KONVERTER CELCIUS =====")
print(f"Hasil dari {celcius} celcius adalah = {a} {b}")


