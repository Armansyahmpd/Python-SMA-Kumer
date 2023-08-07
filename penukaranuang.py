# Program pecahan uang
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 34
# Aktivitas SAP-K11-06-U: Menukarkan Uang
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id


def cari_kombinasi_minimal(nilai_target, pecahan):
    pecahan.sort(reverse=True)  # Urutkan pecahan secara menurun
    kombinasi = []
    
    for pecahan_uang in pecahan:
        while nilai_target >= pecahan_uang:
            kombinasi.append(pecahan_uang)
            nilai_target -= pecahan_uang
            
    return kombinasi

def main():
    pecahan = [20000, 10000, 5000, 2000, 1000]
    nilai_target = int(input("Masukkan nilai uang yang diinginkan (kelipatan ribuan): "))
    
    if nilai_target % 1000 != 0:
        print("Masukkan nilai yang merupakan kelipatan ribuan.")
    else:
        kombinasi = cari_kombinasi_minimal(nilai_target, pecahan)
        print("Kombinasi minimal pecahan uang yang diperlukan:")
        print(kombinasi)

if __name__ == "__main__":
    main()
