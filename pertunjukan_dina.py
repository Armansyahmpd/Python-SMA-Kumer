# Program mengunjungi kebun binatang 
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 33
# Aktivitas SAP-K11-05-U: Mengunjungi Kebun Binatang
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023

def temukan_maksimal_pertunjukan(jadwal):
    jadwal_terurut = sorted(jadwal, key=lambda x: x[1])  # Urutkan jadwal berdasarkan waktu selesai
    maksimal_pertunjukan = []
    waktu_selesai = 0
    
    for pertunjukan in jadwal_terurut:
        if pertunjukan[0] >= waktu_selesai:
            maksimal_pertunjukan.append(pertunjukan)
            waktu_selesai = pertunjukan[1]
    
    return maksimal_pertunjukan

# Format jadwal: (Waktu Mulai, Waktu Selesai, Pertunjukan Hewan)
jadwal = [
    (9.15, 10.30, "Orang Utan"),
    (8.00, 9.30, "Pinguin"),
    (10.00, 12.00, "Harimau"),
    (13.00, 14.30, "Beruang Madu"),
    (11.00, 12.30, "Burung Pemangsa"),
    (14.00, 15.00, "Buaya"),
    (15.30, 16.30, "Panda"),
    (16.00, 17.00, "Ular Piton"),
    (15.00, 15.30, "Singa"),
    (15.30, 16.00, "Anjing Laut")
]

maksimal_pertunjukan = temukan_maksimal_pertunjukan(jadwal)
print("Maksimal pertunjukan yang dapat ditonton:", len(maksimal_pertunjukan))
print("Pertunjukan yang dapat ditonton:")
for pertunjukan in maksimal_pertunjukan:
    print(pertunjukan[2])
