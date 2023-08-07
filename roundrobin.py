# Simulasi Algoritma Round Robin 
# Buku Siswa IKM Informatika untuk SMA Kelas X Hal. 77
# Bab 4 Sistem Komputer
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

class Proses:
    def __init__(self, nama, waktu_kedatangan, waktu_eksekusi):
        self.nama = nama
        self.waktu_kedatangan = waktu_kedatangan
        self.waktu_eksekusi = waktu_eksekusi
        self.sisa_waktu = waktu_eksekusi

def round_robin(proseses, kuantum_waktu):
    n = len(proseses)
    total_waktu = 0
    waktu_tunggu = [0] * n
    waktu_putaran = [0] * n
    waktu_sekarang = 0
    antrian = []

    while True:
        selesai = True
        for proses in proseses:
            if proses.sisa_waktu > 0:
                selesai = False
                if proses.waktu_kedatangan <= waktu_sekarang:
                    if proses.sisa_waktu > kuantum_waktu:
                        waktu_sekarang += kuantum_waktu
                        proses.sisa_waktu -= kuantum_waktu
                    else:
                        waktu_sekarang += proses.sisa_waktu
                        proses.sisa_waktu = 0
                        waktu_putaran[proseses.index(proses)] = waktu_sekarang - proses.waktu_kedatangan
            else:
                continue
        
        if selesai:
            break
    
    for i in range(n):
        waktu_tunggu[i] = waktu_putaran[i] - proseses[i].waktu_eksekusi
        total_waktu += waktu_putaran[i]

    print("Proses\tWaktu Kedatangan\tWaktu Eksekusi\tWaktu Tunggu\tWaktu Putaran")
    for i in range(n):
        print(f"{proseses[i].nama}\t{proseses[i].waktu_kedatangan}\t\t{proseses[i].waktu_eksekusi}\t\t{waktu_tunggu[i]}\t\t{waktu_putaran[i]}")
    
    rata_rata_waktu_putaran = total_waktu / n
    print(f"\nRata-rata Waktu Putaran: {rata_rata_waktu_putaran:.2f}")

# Program utama
proseses = [
    Proses("P0", 0, 250),
    Proses("P1", 50, 170),
    Proses("P2", 120, 70),
    Proses("P3", 170, 100),
    Proses("P4", 200, 130),
    Proses("P5", 350, 50)
]

kuantum_waktu = 100
round_robin(proseses, kuantum_waktu)
