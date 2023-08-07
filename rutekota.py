# Aktivitas SAP-K11-08: Latihan Larik soal no 3
# Menghitung total jarak dari rute antar kota
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 48
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023


def hitung_jarak(rute, jarak_kota):
    total_jarak = 0
    
    for i in range(len(rute) - 1):
        kota_awal = rute[i]
        kota_tujuan = rute[i + 1]
        
        if kota_awal in jarak_kota and kota_tujuan in jarak_kota[kota_awal]:
            total_jarak += jarak_kota[kota_awal][kota_tujuan]
        else:
            print(f"Tidak ada informasi jarak antara {kota_awal} dan {kota_tujuan}.")
            return None
    
    return total_jarak

# Data jarak antar kota
jarak_kota = {
    "Kota A": {"Kota B": 10, "Kota C": 8},
    "Kota B": {"Kota A": 10, "Kota C": 5},
    "Kota C": {"Kota A": 8, "Kota B": 5}
}

# Input rute dari pengguna
rute_input = input("Masukkan rute (pisahkan dengan tanda '-' tanpa spasi): ")
rute = rute_input.split('-')

# Hitung total jarak
total_jarak = hitung_jarak(rute, jarak_kota)

if total_jarak is not None:
    print(f"Total jarak dari rute {rute_input} adalah {total_jarak} km.")
