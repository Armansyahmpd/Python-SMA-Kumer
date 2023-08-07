# Program Panekuk / Hanoi Tower Case
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 28
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50x Indonesia-Harvard 2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


def menara_hanoi(jumlah_panekuk, sumber, tujuan, bantu):
    if jumlah_panekuk == 1:
        print(f"Pindahkan panekuk {jumlah_panekuk} dari piring {sumber} ke piring {tujuan}")
        return 1
    else:
        langkah1 = menara_hanoi(jumlah_panekuk - 1, sumber, bantu, tujuan)
        print(f"Pindahkan panekuk {jumlah_panekuk} dari piring {sumber} ke piring {tujuan}")
        langkah2 = menara_hanoi(jumlah_panekuk - 1, bantu, tujuan, sumber)
        return langkah1 + 1 + langkah2

def utama():
    jumlah_panekuk = int(input("Masukkan jumlah buah panekuk: "))
    total_langkah = menara_hanoi(jumlah_panekuk, 'A', 'C', 'B')
    print(f"\nTotal langkah pemindahan yang diperlukan: {total_langkah}")

if __name__ == "__main__":
    utama()
