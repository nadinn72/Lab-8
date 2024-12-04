# Lab-8

# FLOWCHART

# DIAGRAM CLASS

# PENJELASAN

# PENJELASAN DIAGRAM CLASS

# 1. Kelas Mahasiswa

**Deskripsi**
- Kelas yang merepresentasikan data individual mahasiswa.

**Atribut**
- `nama` (String): Nama mahasiswa
- `nim` (int): Nomor Induk Mahasiswa
- `nilai` (int): Nilai akademik mahasiswa

**Metode**
- Konstruktor untuk inisialisasi
- Getter dan setter untuk setiap atribut
- `toString()`: Representasi string objek mahasiswa

# 2. Kelas ManajemenMahasiswa

**Deskripsi**
- Kelas yang bertanggung jawab mengelola kumpulan data mahasiswa.

**Atribut**
- `daftarMahasiswa`: List untuk menyimpan objek Mahasiswa

**Metode**
- `tambahMahasiswa()`: Menambah mahasiswa baru
- `hapusMahasiswa()`: Menghapus mahasiswa berdasarkan NIM
- `cariMahasiswa()`: Mencari mahasiswa berdasarkan NIM
- `tampilkanSemuaMahasiswa()`: Menampilkan seluruh data
- `ubahMahasiswa()`: Mengubah data mahasiswa

# 3. Kelas AplikasiMahasiswa
**Deskripsi**
- Kelas utama untuk menjalankan aplikasi dan berinteraksi dengan pengguna.

**Metode**
- `main()`: Titik awal program
- `tampilkanMenu()`: Menampilkan pilihan menu
- `prosesMenu()`: Memproses pilihan pengguna

**Hubungan Antar Kelas**
- ManajemenMahasiswa mengandung beberapa objek Mahasiswa
- AplikasiMahasiswa menggunakan ManajemenMahasiswa
