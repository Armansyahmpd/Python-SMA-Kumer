# Problem Simulasi Burung (kasus Boro Prediksi Ketinggian Dicapai Boro dan Teman-temannya)
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 58
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023


import math

def hitung_ketinggian_maksimal(sudut, kecepatan_awal):
    sudut_radian = math.radians(sudut)
    waktu_tempuh = (2 * kecepatan_awal * math.sin(sudut_radian)) / 10
    ketinggian_maksimal = (kecepatan_awal ** 2) * (math.sin(sudut_radian) ** 2) / (2 * 10)
    return waktu_tempuh, ketinggian_maksimal

# Meminta input pengguna untuk jumlah burung
jumlah_burung = int(input("Masukkan jumlah burung: "))

# Inisialisasi list untuk menyimpan hasil status dan ketinggian maksimal burung
status_burung = []
ketinggian_maksimal_burung = []

for i in range(jumlah_burung):
    print(f"Masukkan data untuk Burung {i+1}:")
    sudut = int(input("Sudut Peluncuran (0-90): "))
    kecepatan_awal = int(input("Kecepatan awal: "))
    waktu, ketinggian_maksimal = hitung_ketinggian_maksimal(sudut, kecepatan_awal)
    status = 1 if ketinggian_maksimal >= tinggi_pohon else 0
    status_burung.append(status)
    ketinggian_maksimal_burung.append(ketinggian_maksimal)

# Meminta input pengguna untuk tinggi pohon
tinggi_pohon = int(input("Masukkan Tinggi Pohon Tempat Burung Bersarang: "))

# Menampilkan hasil untuk setiap burung
for i in range(jumlah_burung):
    print(f"Burung {i+1} - Status: {status_burung[i]}, Ketinggian Maksimal: {format(ketinggian_maksimal_burung[i], '.3f')}")


