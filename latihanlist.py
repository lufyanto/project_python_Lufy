data_mahasiswa = [] #Variabel Penampung Utama
while True:
    nama = input("NAMA\t\t: ")
    prodi = input("PRODI\t\t: ")
    kampus = input("KAMPUS\t\t: ")


    data_mahasiswa_all = [nama, prodi, kampus] #Variabel input

    data_mahasiswa.append(data_mahasiswa_all) #Hasil input digabung ke Utama
    print("NO.\t\t|\t\tNAMA\t\t|\t\tPRODI\t\t|\t\tKAMPUS\t\t")
    for index,mhs in enumerate(data_mahasiswa): #Index dengan enumerate
        print(f"{index+1}\t\t|\t\t{mhs[0]}\t\t|\t\t{mhs[1]}\t\t|\t\t{mhs[2]}\t\t")

    lanjut = input('ketik n ketika selesai : ') #Close program jika kondisi terpenuhi

    if lanjut == "n":
        break

