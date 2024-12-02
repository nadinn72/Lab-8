class Mahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah(self, nama, nim, nilai):
        self.daftar_mahasiswa.append({'nama': nama, 'nim': nim, 'nilai': nilai})
        print(f"Data {nama} (NIM: {nim}) berhasil ditambahkan.")

    def tampilkan(self):
        if not self.daftar_mahasiswa:
            print("Daftar mahasiswa kosong.")
            return
        print("Daftar Nilai Mahasiswa:")
        for index, mahasiswa in enumerate(self.daftar_mahasiswa):
            print(f"{index + 1}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Nilai: {mahasiswa['nilai']}")

    def hapus(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nim'] == nim:
                self.daftar_mahasiswa.remove(mahasiswa)
                print(f"Data {mahasiswa['nama']} (NIM: {nim}) berhasil dihapus.")
                return
        print(f"Data dengan NIM {nim} tidak ditemukan.")

    def ubah(self, nim, nilai_baru):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nim'] == nim:
                mahasiswa['nilai'] = nilai_baru
                print(f"Data {mahasiswa['nama']} (NIM: {nim}) berhasil diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Data dengan NIM {nim} tidak ditemukan.")

# Fungsi utama untuk interaksi pengguna
def main():
    mhs = Mahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            mhs.tambah(nama, nim, nilai)

        elif pilihan == '2':
            mhs.tampilkan()

        elif pilihan == '3':
            nim = input("Masukkan NIM mahasiswa yang ingin diubah nilainya: ")
            nilai_baru = input("Masukkan nilai baru: ")
            mhs.ubah(nim, nilai_baru)

        elif pilihan == '4':
            nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
            mhs.hapus(nim)

        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()