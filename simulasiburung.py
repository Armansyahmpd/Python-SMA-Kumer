# Problem Simulasi Burung (kasus Boro menghitung jarak horizontal terjauh)
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 53
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023


import math

def hitung_jarak_horizontal(sudut, kecepatan_awal):
    sudut_radian = math.radians(sudut)
    jarak_horizontal = (kecepatan_awal ** 2) * math.sin(2 * sudut_radian) / 10
    return jarak_horizontal

# Meminta input dari pengguna untuk sudut peluncuran dan kecepatan awal
sudut = int(input("Masukkan Sudut Peluncuran (Nilai S) : "))
kecepatan_awal = int(input("Masukkan Nilai Kecepatan awal : "))

# Menghitung jarak horizontal
jarak = hitung_jarak_horizontal(sudut, kecepatan_awal)

# Membulatkan hasil menjadi 1 angka di belakang koma
jarak_bulat = round(jarak, 1)

# Menampilkan hasil
print("Jarak terjauh yang dapat ditempuh oleh Boro:", jarak_bulat)
