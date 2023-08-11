# Aktivitas SAP-K11-03-U: Menerapkan Konsep Rekursi
# Permasalahan 1: Memasang Keramik
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 27
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Validasi Sertifikat : https://bit.ly/ceksertifikatcs50
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

def hitung_cara_pemasangan_keramik(N):
    if N == 0:
        return 1
    if N == 1:
        return 1

    # Inisialisasi array untuk menyimpan jumlah cara pemasangan keramik
    dp = [0] * (N + 1)

    # Kasus dasar
    dp[0] = 1
    dp[1] = 1

    # Hitung jumlah cara pemasangan keramik untuk setiap N
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

def utama():
    try:
        N = int(input("Masukkan nilai N (bilangan bulat positif): "))
        if N < 0:
            raise ValueError("N harus merupakan bilangan bulat positif.")
        
        cara = hitung_cara_pemasangan_keramik(N)
        print(f"Jumlah cara pemasangan keramik untuk N={N}: {cara} cara.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    utama()
