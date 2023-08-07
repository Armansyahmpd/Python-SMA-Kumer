# Program Stack/Tumpukan (algoritma PUSH dan POP) 
# Buku Siswa IKM Informatika untuk SMA Kelas X Hal. 41
# Bab 2 Berpikir Komputasional
# Aktivitas BK-K10-04-U: Simulasi Stack
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


class Tumpukan:
    def __init__(self):
        self.item_tumpukan = []

    def PUSH(self, item):
        self.item_tumpukan.append(item)

    def POP(self):
        if not self.kosong():
            return self.item_tumpukan.pop()
        else:
            return None

    def kosong(self):
        return len(self.item_tumpukan) == 0

    def tampilkan(self):
        return ", ".join(str(item) for item in self.item_tumpukan)


def utama():
    tumpukan = Tumpukan()
    while True:
        perintah = input("Masukkan perintah (PUSH [angka] / POP / Selesai): ").split()

        if perintah[0].lower() == "push":
            if len(perintah) == 2:
                item = int(perintah[1])
                tumpukan.PUSH(item)
                print(f"Isi Tumpukan: {tumpukan.tampilkan()}")
        elif perintah[0].lower() == "pop":
            if not tumpukan.kosong():
                tumpukan.POP()
                print(f"Isi Tumpukan: {tumpukan.tampilkan()}")
            else:
                print("Nilai tumpukan saat ini kosong, Anda tidak dapat melakukan operasi POP")
        elif perintah[0].lower() == "selesai":
            break

        perintah_lain = input("Apakah Anda ingin memasukkan perintah lagi? (Ya / Tidak): ")
        if perintah_lain.lower() != "ya":
            break

    print(f"Isi Tumpukan akhir: {tumpukan.tampilkan()}")


if __name__ == "__main__":
    utama()
