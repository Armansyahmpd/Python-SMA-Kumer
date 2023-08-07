# Aktivitas SAP-K11-08: Latihan Larik soal no 2
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 48
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


def transpose_matriks(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])
    hasil_transpose = [[0 for _ in range(baris)] for _ in range(kolom)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil_transpose[j][i] = matriks[i][j]
    
    return hasil_transpose

def utama():
    try:
        n = int(input("Masukkan jumlah baris (N): "))
        m = int(input("Masukkan jumlah kolom (M): "))
        
        matriks = []
        for i in range(n):
            baris = []
            for j in range(m):
                elemen = int(input(f"Masukkan elemen matriks [{i}][{j}]: "))
                baris.append(elemen)
            matriks.append(baris)
        
        print("Matriks awal:")
        for baris in matriks:
            print(baris)
        
        hasil_transpose = transpose_matriks(matriks)
        
        print("Hasil transpose matriks:")
        for baris in hasil_transpose:
            print(baris)
    
    except ValueError:
        print("Input harus berupa angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    utama()


if __name__ == "__main__":
    main()
