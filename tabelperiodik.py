# Menampilkan semua nama unsur dan atribut lainnya pada tabel periodik 
# Memanfaatkan pustaka/library periodictable
# Jika menggunakan VSCode, install dulu librarynya di terminal dengan cara mengetikkan :
# pip install periodictable
# Adaptasi bebas dari Buku Siswa IKM Informatika untuk SMA Kelas XI hal. 77
# Problem: “Simulasi Stoikiometri”
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

import periodictable

def main():
    print("Daftar unsur dalam tabel periodik:\n")
    print("{:<20} {:<10} {:<15} {:<15}".format("Nama Unsur", "Simbol", "Nomor Atom", "Massa Atom"))
    print("="*60)
    
    for element in periodictable.elements:
        print("{:<20} {:<10} {:<15} {:<15}".format(element.name, element.symbol, element.number, element.mass))

if __name__ == "__main__":
    main()
