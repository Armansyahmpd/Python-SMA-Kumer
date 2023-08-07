# Mencari jalur terpendek antar titik ABCD berdasar algoritma Floyd Warshall
# Buku Siswa IKM Informatika untuk SMA Kelas XI 
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

TAK_TERHINGGA = float('inf')

def floyd_warshall(graf):
    n = len(graf)
    jarak = [[TAK_TERHINGGA] * n for _ in range(n)]
    titik_selanjutnya = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                jarak[i][j] = 0
            elif graf[i][j] != TAK_TERHINGGA:
                jarak[i][j] = graf[i][j]
                titik_selanjutnya[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if jarak[i][k] + jarak[k][j] < jarak[i][j]:
                    jarak[i][j] = jarak[i][k] + jarak[k][j]
                    titik_selanjutnya[i][j] = titik_selanjutnya[i][k]

    return jarak, titik_selanjutnya

def konstruksi_jalur(titik_selanjutnya, awal, akhir):
    if titik_selanjutnya[awal][akhir] is None:
        return []
    
    jalur = [awal]
    while awal != akhir:
        awal = titik_selanjutnya[awal][akhir]
        jalur.append(awal)
    return jalur

# Input panjang jalan
panjang_jalan = {}
panjang_jalan[('A', 'B')] = int(input("Masukkan panjang jalan dari A ke B: "))
panjang_jalan[('A', 'C')] = int(input("Masukkan panjang jalan dari A ke C: "))
panjang_jalan[('B', 'D')] = int(input("Masukkan panjang jalan dari B ke D: "))
panjang_jalan[('C', 'D')] = int(input("Masukkan panjang jalan dari C ke D: "))

# Inisialisasi matriks adjacency graf dengan nilai TAK_TERHINGGA
graf = [
    [0, TAK_TERHINGGA, TAK_TERHINGGA, TAK_TERHINGGA],
    [TAK_TERHINGGA, 0, TAK_TERHINGGA, TAK_TERHINGGA],
    [TAK_TERHINGGA, TAK_TERHINGGA, 0, TAK_TERHINGGA],
    [TAK_TERHINGGA, TAK_TERHINGGA, TAK_TERHINGGA, 0],
]

# Update matriks adjacency graf dengan panjang jalan
for (asal, tujuan), panjang in panjang_jalan.items():
    graf[ord(asal) - ord('A')][ord(tujuan) - ord('A')] = panjang

# Input titik awal dan tujuan
titik_awal = input("Masukkan titik awal (A, B, C, D): ").upper()
titik_tujuan = input("Masukkan titik tujuan (A, B, C, D): ").upper()

# Validasi input titik awal dan tujuan
titik_valid = set(['A', 'B', 'C', 'D'])
if titik_awal not in titik_valid or titik_tujuan not in titik_valid:
    print("Titik awal atau tujuan tidak valid.")
else:
    indeks_awal = ord(titik_awal) - ord('A')
    indeks_tujuan = ord(titik_tujuan) - ord('A')

    jarak, titik_selanjutnya = floyd_warshall(graf)
    jalur = konstruksi_jalur(titik_selanjutnya, indeks_awal, indeks_tujuan)

    if not jalur:
        print(f"Tidak ada jalur yang tersedia dari titik {titik_awal} ke titik {titik_tujuan}.")
    else:
        print(f"Jalur terpendek dari titik {titik_awal} ke titik {titik_tujuan}:")
        print(" -> ".join(chr(indeks + ord('A')) for indeks in jalur))
