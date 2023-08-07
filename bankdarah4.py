# Problem Pengelolaan Bank Darah Kasus 4
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 65
# Tingkatkan Penyimpanan dan Kecepatan Olah Data DDS
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
    
    gol_darah_habis, volume_dibutuhkan = input().split()
    volume_dibutuhkan = int(volume_dibutuhkan)
    
    total_volume_habis = 0
    selected_desa = []
    
    for kode_dsa in range(1, M+1):
        if gol_darah_habis in desa_pendonor.get(kode_dsa, {}) and desa_volume.get(kode_dsa, {}).get(gol_darah_habis, 0) > 0:
            total_volume_habis += desa_volume[kode_dsa][gol_darah_habis]
            selected_desa.append(kode_dsa)
            if total_volume_habis >= volume_dibutuhkan:
                break
    
    if total_volume_habis >= volume_dibutuhkan:
        print("Keluaran:")
        for kode_dsa in selected_desa:
            print(f"Desa {kode_dsa}: Golongan {gol_darah_habis}, Jumlah darah: {desa_volume[kode_dsa][gol_darah_habis]} ml")
        surplus = total_volume_habis - volume_dibutuhkan
        print(f"Kebutuhan darah dipenuhi dengan surplus {surplus} ml")
    else:
        kurang = volume_dibutuhkan - total_volume_habis
        print(f"Kebutuhan darah masih kurang {kurang} ml")

if __name__ == "__main__":
    main()
