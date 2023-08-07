# Aktivitas SAP-K11-08: Latihan Larik soal no 1
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 48
# Algoritma dan Pemrograman
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023


def main():
    try:
        n = int(input("Masukkan jumlah bilangan: "))
        numbers = []

        for i in range(n):
            num = int(input(f"Masukkan bilangan ke-{i + 1}: "))
            numbers.append(num)

        print("Bilangan secara terbalik:")
        for num in reversed(numbers):
            print(num, end=" ")
            # Jika ingin membuat output turun secara vertikal gunakan :
            #  print(num)

    except ValueError:
        print("Masukan harus berupa bilangan bulat.")
