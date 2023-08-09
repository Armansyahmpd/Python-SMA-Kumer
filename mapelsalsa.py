# Program Pemilihan Mata Pelajaran (Kasus Salsa)
# Jawaban soal Tes Sumatif 1 (SMAN Sumatera Selatan) terkait Implementasi Algoritma Greedy
# Adaptasi dan pengembangan dari kasus pada Aktivitas SAP-K11-05-U: Mengunjungi Kebun Binatang
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 33
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

# Buat Daftar kelas dengan waktu mulai dan selesai
kelas = [
    ("Matematika", 7.00, 8.30),
    ("Fisika", 8.00, 9.30),
    ("Biologi", 9.00, 10.45),
    ("Informatika", 9.45, 11.00),
    ("Sejarah", 11.05, 12.30),
    ("Bahasa Inggris Wajib", 10.45, 13.20),
    ("Bahasa Inggris", 13.20, 14.00),
    ("PKWU", 13.00, 14.10),
    ("Bahasa Indonesia", 14.15, 15.00),
    ("Sosiologi", 14.00, 15.30),
    ("Ekonomi", 15.45, 16.45),
    ("Seni Tari", 17.06, 18.10)
]

# Mengurutkan kelas berdasarkan waktu selesai
kelas_terurut = sorted(kelas, key=lambda x: x[2])

# Inisialisasi variabel
maks_kelas = 0
daftar_kelas_maks = []

# Memilih kelas secara greedy
waktu_sekarang = 0
for kls in kelas_terurut:
    if kls[1] >= waktu_sekarang:
        daftar_kelas_maks.append(kls[0])
        waktu_sekarang = kls[2]
        maks_kelas += 1

# Menampilkan hasil
print("Maksimal kelas yang dapat diikuti:", maks_kelas)
print("Kelas-kelas yang dapat diikuti:", daftar_kelas_maks)
