# Problem Pengelolaan Bank Darah Kasus 2
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 63
# Menghitung Jumlah Pendonor dan Total Volume Darah
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
    desa_volume = {}
    
    for _ in range(N):
        kode_dsa, gol_darah, volume = input().split()
        kode_dsa = int(kode_dsa)
        volume = int(volume)
        
        if kode_dsa not in desa_pendonor:
            desa_pendonor[kode_dsa] = {gol_darah: 1}
            desa_volume[kode_dsa] = {gol_darah: volume}
        else:
            if gol_darah not in desa_pendonor[kode_dsa]:
                desa_pendonor[kode_dsa][gol_darah] = 1
                desa_volume[kode_dsa][gol_darah] = volume
            else:
                desa_pendonor[kode_dsa][gol_darah] += 1
                desa_volume[kode_dsa][gol_darah] += volume
    
    print("\nKeluaran:")
    for kode_dsa in range(1, M+1):
        print(f"Desa {kode_dsa}:")
        golongan_darah = ['A', 'B', 'AB', 'O']
        for gol_darah in golongan_darah:
            jumlah_pendonor = desa_pendonor.get(kode_dsa, {}).get(gol_darah, 0)
            total_volume = desa_volume.get(kode_dsa, {}).get(gol_darah, 0)
            print(f"  {gol_darah}: {jumlah_pendonor} Pendonor, Total Volume: {total_volume} ml")

if __name__ == "__main__":
    main()
