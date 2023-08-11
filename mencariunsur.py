# Mencari nama unsur dan atribut lainnya pada tabel periodik 
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
    element_name = input("Masukkan nama unsur: ").capitalize()
    
    try:
        element = periodictable.elements.name(element_name)
        print(f"Simbol unsur: {element.symbol}")
        print(f"Nama unsur: {element.name}")
        print(f"Nomor atom: {element.number}")
        print(f"Massa atom: {element.mass}")
    except ValueError:
        print("Unsur tidak ditemukan dalam tabel periodik.")

if __name__ == "__main__":
    main()
