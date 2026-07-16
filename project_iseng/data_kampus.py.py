import os

data_mahasiswa = {}

os.system('cls')

def login():
    """
    Node flowchart:
    [input USERNAME, user=admin, pw=123] -> <input == user,pw ?>
    - YES -> lanjut
    - NO  -> "coba lagi" (kembali) -> ulangi input
    """
    while True:
        print("=" * 40)
        print("LOGIN SISTEM KAMPUS APA YA? ")
        print("=" * 40)
        user = input("Username : ")
        pw = input("Password : ")

        if user == "admin" and pw == "123":
            print("\nLogin berhasil!\n")
            return True

        if user == "lufy" and pw == "456":
            print("\nLogin berhasil!\n")
            return True
        
        if user == "raihan" and pw == "789":
            print("\nLogin berhasil!\n")
            return True
        
        else:
            print("\nUsername/Password salah. Coba lagi...\n")
            # loop otomatis mengulang -> sesuai panah "kembali" pada flowchart


def input_data_mahasiswa():
    """
    Node flowchart:
    [masukkan: nama, nim, kelas, prodi, fakultas]
    """
    print("\n--- Input Data Mahasiswa ---")
    nama = input("Nama     : ").strip()
    nim = input("NIM      : ").strip()
    kelas = input("Kelas    : ").strip()
    prodi = input("Prodi    : ").strip()
    fakultas = input("Fakultas : ").strip()

    data_mahasiswa.setdefault(nim, {})
    data_mahasiswa[nim].update({
        "nama": nama,
        "nim": nim,
        "kelas": kelas,
        "prodi": prodi,
        "fakultas": fakultas,
    })
    print(f"Data mahasiswa {nama} berhasil dimasukkan.\n")


def input_data_nilai():
    """
    Node flowchart:
    [masukkan: nama, nim, nilai: matkul1= ... matkul6=]
    -> [matkul 1 s.d 6 di rata-rata]
    """
    print("\n--- Input Data Nilai ---")
    nama = input("Nama : ").strip()
    nim = input("NIM  : ").strip()

    nilai = []
    for i in range(1, 7):
        while True:
            try:
                n = float(input(f"Nilai Matkul {i} : "))
                nilai.append(n)
                break
            except ValueError:
                print("Masukkan angka yang valid!")

    rata_rata = sum(nilai) / len(nilai)

    data_mahasiswa.setdefault(nim, {})
    data_mahasiswa[nim].update({
        "nama": nama,
        "nim": nim,
        "nilai": nilai,
        "rata_rata": rata_rata,
    })
    print(f"Rata-rata nilai {nama} = {rata_rata:.2f}\n")


def input_data():
    """
    Node flowchart:
    <input data: 1. data mahasiswa   2. data nilai>
    -> looping sampai jawaban <sudah selesai belum?> = "sudah"
    """
    while True:
        print("Input Data:")
        print("1. Data Mahasiswa")
        print("2. Data Nilai")
        pilihan = input("Pilih (1/2): ").strip()

        if pilihan == "1":
            input_data_mahasiswa()
        elif pilihan == "2":
            input_data_nilai()
        else:
            print("Pilihan tidak valid!\n")
            continue

        selesai = input("Sudah selesai input data? (y = sudah / n = belum): ").strip().lower()
        if selesai == "y":
            break
        # jika "n" (belum) -> loop kembali ke pilihan input data (1/2)


def simpan_data():
    """
    Node flowchart: [simpan data]
    (disimpan di memori; bisa dikembangkan ke file/database bila perlu)
    """
    print("\nData berhasil disimpan.\n")


def tampilkan_data():
    """
    Node flowchart: [tampilkan data]
    """
    print("\n" + "=" * 60)
    print("DAFTAR DATA MAHASISWA")
    print("=" * 60)

    if not data_mahasiswa:
        print("Belum ada data.")
    else:
        for nim, d in data_mahasiswa.items():
            print(f"Nama     : {d.get('nama', '-')}")
            print(f"NIM      : {d.get('nim', nim)}")
            print(f"Kelas    : {d.get('kelas', '-')}")
            print(f"Prodi    : {d.get('prodi', '-')}")
            print(f"Fakultas : {d.get('fakultas', '-')}")
            if "nilai" in d:
                print(f"Nilai    : {d['nilai']}")
                print(f"Rata-rata: {d['rata_rata']:.2f}")
            print("-" * 60)

    print()


def menu_utama():
    """
    Node flowchart:
    [user ingin apa?] -> <input data / lihat data>
    """
    while True:
        print("=" * 40)
        print("USER INGIN APA?")
        print("=" * 40)
        print("1. Input Data")
        print("2. Lihat Data")
        pilihan = input("Pilih (1/2): ").strip()

        if pilihan == "1":
            input_data()
            simpan_data()
            break
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!\n")

    tampilkan_data()


def main():
    """ START """
    if login():
        menu_utama()
    print("=== SELESAI ===")


if __name__ == "__main__":
    main()