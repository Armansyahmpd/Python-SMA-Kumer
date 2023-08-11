# Mencari jalur terpendek antar titik ABCD berdasar algoritma Greedy
# Buku Siswa IKM Informatika untuk SMA Kelas XI hal. 47
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


def cari_jalur_terpendek(cabang, posisi_awal, posisi_tujuan):
    posisi_sekarang = posisi_awal
    jalur = [posisi_sekarang]
    total_jarak = 0

    while posisi_sekarang != posisi_tujuan:
        cabang_selanjutnya = None
        jarak_terpendek = float('inf')

        for cabang_tetangga, jarak in cabang[posisi_sekarang].items():
            if cabang_tetangga not in jalur and jarak < jarak_terpendek:
                cabang_selanjutnya = cabang_tetangga
                jarak_terpendek = jarak

        if cabang_selanjutnya is None:
            print("Tidak ada jalan yang bisa diambil.")
            return None, None

        jalur.append(cabang_selanjutnya)
        total_jarak += jarak_terpendek
        posisi_sekarang = cabang_selanjutnya

    return jalur, total_jarak


if __name__ == "__main__":
    cabang_cadangan = {
        'A': {'B': 0, 'C': 0},
        'B': {'D': 0},
        'C': {'D': 0},
        'D': {},
    }

    posisi_awal = input("Masukkan posisi awal (A, B, C, atau D): ")
    posisi_tujuan = input("Masukkan posisi tujuan (B, C, atau D): ")

    # Input panjang jalan setiap cabang
    for simpul in cabang_cadangan:
        for tetangga in cabang_cadangan[simpul]:
            print(f"Masukkan panjang jalan dari {simpul} ke {tetangga}:")
            jarak = int(input())
            cabang_cadangan[simpul][tetangga] = jarak

    jalur_terpendek, total_jarak = cari_jalur_terpendek(cabang_cadangan, posisi_awal, posisi_tujuan)

    if jalur_terpendek and total_jarak is not None:
        print(f"Jalur terpendek dari {posisi_awal} ke {posisi_tujuan} yang harus dilalui:")
        print(" -> ".join(jalur_terpendek))
        print("Total jarak yang harus ditempuh:", total_jarak)
