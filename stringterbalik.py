# Membaca sebuah string dan mencetaknya secara terbalik
# Buku Siswa IKM Informatika untuk SMA Kelas X Hal. 52
# Aktivitas SAP-K11-09: Latihan Karakter dan String
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

input_string = input("Masukkan sebuah string: ")
reversed_string = reverse_string(input_string)
print("String terbalik:", reversed_string)
