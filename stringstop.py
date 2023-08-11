# Aktivitas SAP-K11-09: Latihan Karakter dan String
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 51
# Membaca banyak string hingga membaca string “STOP”. Setiap string yang dibaca akan diubah ke huruf non kapital dan dicetak.
# Dalam bahasa Python
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Validasi Sertifikat : https://bit.ly/ceksertifikatcs50
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas

while True:
    input_string = input("Masukkan string (ketik 'STOP' untuk berhenti): ")
    
    if input_string == "STOP":
        break
    
    input_string = input_string.lower()
    print(input_string)
