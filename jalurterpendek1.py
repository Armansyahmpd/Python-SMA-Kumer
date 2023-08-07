# Program Algoritma Greedy untuk mencari jalur terpendek antar percabangan ABCD 
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 29
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teacher Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

def cari_jalur_terpendek(cabang):
    posisi_sekarang = 'A'
    jalur = [posisi_sekarang]
    total_jarak = 0

    while posisi_sekarang != 'B':
        cabang_selanjutnya = None
        jarak_terpendek = float('inf')

        for cabang, jarak in cabang[posisi_sekarang].items():
            if cabang not in jalur and jarak < jarak_terpendek:
                cabang_selanjutnya = cabang
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

    # Input panjang jalan setiap cabang
    for simpul in cabang_cadangan:
        for tetangga in cabang_cadangan[simpul]:
            print(f"Masukkan panjang jalan dari {simpul} ke {tetangga}:")
            jarak = int(input())
            cabang_cadangan[simpul][tetangga] = jarak

    jalur_terpendek, total_jarak = cari_jalur_terpendek(cabang_cadangan)

    if jalur_terpendek and total_jarak is not None:
        print("Jalur terpendek dari A ke B yang harus dilalui:")
        print(" -> ".join(jalur_terpendek))
        print("Total jarak yang harus ditempuh:", total_jarak)
