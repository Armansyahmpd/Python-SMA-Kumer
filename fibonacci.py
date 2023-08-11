# Studi Kasus Deret Fibonacci
# Adaptasi bebas Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 25
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

def fibonacci(n):
    if n <= 0:
        return "Masukkan angka bulat positif yang lebih besar dari 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Penggunaan fungsi fibonacci
angka_ke = int(input("Masukkan angka ke-n untuk mencari angka Fibonacci: "))

# Validasi input angka bulat positif
if angka_ke <= 0:
    print("Masukkan angka bulat positif yang lebih besar dari 0.")
else:
    hasil_fibonacci = fibonacci(angka_ke)
    print("Angka Fibonacci ke-", angka_ke, "adalah", hasil_fibonacci)
