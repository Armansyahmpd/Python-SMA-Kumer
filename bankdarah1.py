# Problem Pengelolaan Bank Darah Kasus 1
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 60
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

def main():
    N = int(input("Masukkan jumlah DDS: "))
    M = int(input("Masukkan jumlah desa: "))
    
    desa_pendonor = {}
    
    for _ in range(N):
        kode_dsa, gol_darah, volume = input().split()
        kode_dsa = int(kode_dsa)
        volume = int(volume)
        
        if kode_dsa not in desa_pendonor:
            desa_pendonor[kode_dsa] = 1
        else:
            desa_pendonor[kode_dsa] += 1
    
    for kode_dsa in range(1, M+1):
        banyak_pendonor = desa_pendonor.get(kode_dsa, 0)
        print(f"Desa {kode_dsa}: {banyak_pendonor} Pendonor")

if __name__ == "__main__":
    main()
