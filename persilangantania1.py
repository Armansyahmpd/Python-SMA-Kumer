# Problem Persilangan Benih Padi Unggulan
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 69
# Menghitung Persentase Suatu Sifat Keturunan Pertama (F1)
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


def hitung_persentase_fenotipe_orang_tua(parent1, parent2, keturunan):
    fenotipe_hitung = {
        'TT': 0, 'Tt': 0, 'aa': 0, 'Aa': 0, 'Aa': 0, 'BB': 0, 'Bb': 0, 'bb': 0,
        'RR': 0, 'Rr': 0, 'rr': 0
    }
    
    kode_fenotipe = ['TT', 'Tt', 'aa', 'Aa', 'Aa', 'BB', 'Bb', 'bb', 'RR', 'Rr', 'rr']
    
    fenotipe_orang_tua_1 = kode_fenotipe[parent1[0]] + kode_fenotipe[parent1[1]]
    fenotipe_orang_tua_2 = kode_fenotipe[parent2[0]] + kode_fenotipe[parent2[1]]
    fenotipe_keturunan = kode_fenotipe[keturunan[0]] + kode_fenotipe[keturunan[1]]
    
    fenotipe_gabungan = fenotipe_orang_tua_1 + fenotipe_orang_tua_2
    
    total_keturunan = 4  # Karena total keturunan ada 4
    jumlah_fenotipe_target = fenotipe_gabungan.count(fenotipe_keturunan)
    
    persentase = (jumlah_fenotipe_target / total_keturunan) * 100
    
    return persentase

# Masukkan karakteristik orang tua dan karakteristik keturunan
orang_tua_1 = list(map(int, input().split()))
orang_tua_2 = list(map(int, input().split()))
keturunan = list(map(int, input().split()))

# Hitung dan cetak persentase kemunculan fenotipe keturunan yang diinginkan
hasil = hitung_persentase_fenotipe_orang_tua(orang_tua_1, orang_tua_2, keturunan)
print(f"{hasil:.2f}%")
