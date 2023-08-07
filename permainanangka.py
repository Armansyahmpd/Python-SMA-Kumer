# Program permainan angka
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 42
# Aktivitas SAP-K11-07-U: Bermain Angka
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


def langkah_minimum_ke_satu(n):
    if n == 1:
        return 0
    
    angka = [0] * (n + 1)
    
    for i in range(2, n + 1):
        angka[i] = angka[i - 1] + 1
        
        if i % 2 == 0:
            angka[i] = min(angka[i], angka[i // 2] + 1)
        
        if i % 3 == 0:
            angka[i] = min(angka[i], angka[i // 3] + 1)
    
    return angka[n]

# Input dari pengguna
n = int(input("Masukkan bilangan n: "))
langkah = langkah_minimum_ke_satu(n)
print(f"Jumlah langkah minimum untuk mengubah {n} menjadi 1 adalah: {langkah}")
