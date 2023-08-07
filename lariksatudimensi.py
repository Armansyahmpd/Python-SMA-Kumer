# Program Demonstrasi larik satu dimensi dengan vektor 
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 46
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id

def cetak_larik(ukuran, larik):
    for i in range(ukuran):
        print(larik[i])

def main():
    bilangan = []
    for i in range(10):
        bilangan.append(i)
    cetak_larik(10, bilangan)

if __name__ == "__main__":
    main()
