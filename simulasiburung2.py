# Problem Simulasi Burung (kasus Boro menghitung waktu)
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 55
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023


import math

def hitung_waktu_tempuh(sudut, kecepatan_awal):
    sudut_radian = math.radians(sudut)
    waktu_tempuh = (2 * kecepatan_awal * math.sin(sudut_radian)) / 10
    return waktu_tempuh

# Meminta input pengguna untuk sudut peluncuran dan kecepatan awal
sudut = int(input("Masukkan Sudut Peluncuran (Nilai S) : "))
kecepatan_awal = int(input("Masukkan Nilai Kecepatan awal : "))

# Menghitung waktu tempuh
waktu = hitung_waktu_tempuh(sudut, kecepatan_awal)

# Menampilkan waktu dengan format 3 angka di belakang koma
print("Waktu yang diperlukan Boro:", format(waktu, ".3f"))
