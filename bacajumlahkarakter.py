# Membaca Sandi
# Buku Siswa IKM Informatika untuk SMA Kelas X Hal. 52
# Aktivitas SAP-K11-09: Latihan Karakter dan String
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


def hitung_karakter(password):
    jumlah_angka = 0
    jumlah_huruf = 0

    for karakter in password:
        if karakter.isdigit():
            jumlah_angka += 1
        elif karakter.isalpha():
            jumlah_huruf += 1

    return jumlah_angka, jumlah_huruf

def utama():
    sandi = input("Masukkan kata sandi: ")
    jumlah_angka, jumlah_huruf = hitung_karakter(sandi)

    print("Jumlah karakter angka:", jumlah_angka)
    print("Jumlah karakter huruf:", jumlah_huruf)

if __name__ == "__main__":
    utama()
