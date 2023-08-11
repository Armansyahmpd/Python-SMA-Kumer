# Aktivitas SAP-K11-06-U: Pemrograman Dinamis (Kasus Agria)
# Contoh 1 Tentang total jumlah cabai yang dikumpulkan oleh Agria
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 37
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


def jalur_panen_terbanyak(grid):
    baris = len(grid)
    kolom = len(grid[0])

    dp = [[0] * kolom for _ in range(baris)]

    for i in range(baris):
        dp[i][kolom - 1] = grid[i][kolom - 1]

    for j in range(kolom - 2, -1, -1):
        for i in range(baris):
            if i > 0:
                maks_pilihan = max(dp[i][j + 1], dp[i - 1][j + 1] if i > 0 else 0, dp[i + 1][j + 1] if i < baris - 1 else 0)
            else:
                maks_pilihan = max(dp[i][j + 1], dp[i + 1][j + 1] if i < baris - 1 else 0)
            dp[i][j] = grid[i][j] + maks_pilihan

    maks_panen = 0
    baris_mulai = 0
    for i in range(baris):
        if dp[i][0] > maks_panen:
            maks_panen = dp[i][0]
            baris_mulai = i

    lintasan = [(baris_mulai, 0)]
    baris_sekarang = baris_mulai
    for j in range(1, kolom):
        if baris_sekarang == 0:
            pilihan = [(baris_sekarang, j)]
        elif baris_sekarang == baris - 1:
            pilihan = [(baris_sekarang - 1, j)]
        else:
            pilihan = [(baris_sekarang - 1, j), (baris_sekarang, j), (baris_sekarang + 1, j)]
        
        baris_berikutnya, _ = max(pilihan, key=lambda pilihan: dp[pilihan[0]][pilihan[1]])
        lintasan.append((baris_berikutnya, j))
        baris_sekarang = baris_berikutnya
    
    return lintasan, maks_panen

# Definisikan grid berdasarkan ilustrasi yang diberikan
grid = [
    [0, 1, 2, 3, 10],
    [10, 2, 10, 10, 5],
    [5, 3, 6, 5, 0],
    [0, 4, 0, 2, 3],
    [20, 5, 1, 0, 0]
]

baris = len(grid)
kolom = len(grid[0])
dp = [[0] * kolom for _ in range(baris)]

# Hitung nilai dp
for i in range(baris):
    dp[i][kolom - 1] = grid[i][kolom - 1]
for j in range(kolom - 2, -1, -1):
    for i in range(baris):
        if i > 0:
            maks_pilihan = max(dp[i][j + 1], dp[i - 1][j + 1] if i > 0 else 0, dp[i + 1][j + 1] if i < baris - 1 else 0)
        else:
            maks_pilihan = max(dp[i][j + 1], dp[i + 1][j + 1] if i < baris - 1 else 0)
        dp[i][j] = grid[i][j] + maks_pilihan

# Lacak jalur yang diambil oleh Agria dan hitung jumlah cabai terbanyak
lintasan_agria, total_panen = jalur_panen_terbanyak(grid)

# Cetak ilustrasi jalur
for i in range(baris):
    for j in range(kolom):
        if (i, j) in lintasan_agria:
            print(" * ", end="")
        else:
            print(f"{grid[i][j]:3d}", end="")
    print()

# Cetak total cabai terbanyak yang dikumpulkan oleh Agria
print("Jumlah cabai terbanyak yang dapat dikumpulkan oleh Agria:", total_panen)
