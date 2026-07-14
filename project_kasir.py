barang_all = []

while True:
    print("========== KOPERASI MERAH PUTIH ==========")
    beli = input("Item yang dibeli : ")
    jumlah = int(input("Jumlah Item : "))
    harga = int(input("Harga Item : "))
    barang = [beli,jumlah,harga]

    barang_all.append(barang)

    program = input("Y untuk lanjutkan, N untuk selesai")

    if program == "N":
        break

print("========== KOPERASI MERAH PUTIH ==========")
print("========== STRUK TAGIHAN ==========")

for index,brg in enumerate(barang_all):
    print(f"{index}. {brg[0]} | {brg[1]} | {brg[2]} | {brg[1]*brg[2]}")




