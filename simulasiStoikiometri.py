# Problem: “Simulasi Stoikiometri”
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 78
# Subproblem 1: Menghitung Atom
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

def hitung_atom(senyawa):
    unsur_hitungan = {}  # Dictionary untuk menyimpan hitungan unsur

    i = 0
    while i < len(senyawa):
        if senyawa[i].isupper():
            unsur = senyawa[i]
            i += 1
            while i < len(senyawa) and senyawa[i].islower():
                unsur += senyawa[i]
                i += 1

            jumlah = 0
            while i < len(senyawa) and senyawa[i].isdigit():
                jumlah = jumlah * 10 + int(senyawa[i])
                i += 1
            if jumlah == 0:
                jumlah = 1  # Jika tidak ada jumlah yang ditentukan, diasumsikan 1

            if unsur in unsur_hitungan:
                unsur_hitungan[unsur] += jumlah
            else:
                unsur_hitungan[unsur] = jumlah
        else:
            i += 1

    return unsur_hitungan

senyawa = input("Masukkan senyawa kimia: ")
hitungan_unsur = hitung_atom(senyawa)

for unsur, jumlah in hitungan_unsur.items():
    print(f"{unsur} {jumlah}")
