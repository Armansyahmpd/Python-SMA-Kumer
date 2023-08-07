# Program PR-Cici 
# Aktivitas SAP-K11-04-U: Mengerjakan Pekerjaan Rumah (PR)
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 32
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023

def maks_nilai_knapsack(bobot, nilai, kapasitas):
    n = len(bobot)
    dp = [[0] * (kapasitas + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, kapasitas + 1):
            if bobot[i - 1] <= w:
                dp[i][w] = max(nilai[i - 1] + dp[i - 1][w - bobot[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp

# Data PR
pr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
waktu = [15, 30, 10, 5, 40, 10, 25, 10, 5, 20]  # Diubah menjadi angka bulat (jam x 10)
nilai = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # Setiap PR memiliki nilai yang sama

total_waktu = 80  # Total waktu yang tersedia (jam x 10)

# Menghitung nilai maksimal dengan mempertimbangkan batasan waktu
dp = maks_nilai_knapsack(waktu, nilai, total_waktu)
maks_nilai = dp[len(pr)][total_waktu]

print("Total nilai akhir yang sebesar-besarnya:", maks_nilai)

# Menentukan PR yang harus dikerjakan dalam waktu maksimal
sisa_waktu = total_waktu
pr_terpilih = []

for i in range(len(pr) - 1, -1, -1):
    if maks_nilai == 0:
        break
    if maks_nilai != dp[i][sisa_waktu]:
        pr_terpilih.append(pr[i])
        maks_nilai -= nilai[i]
        sisa_waktu -= waktu[i]

print("PR yang harus dikerjakan:", pr_terpilih)
