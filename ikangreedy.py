# Program ikan (kasus Algoritma Greedy)
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 30
# Contoh 1: Membawa Ikan 1
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023

def greedy_bag_selection(kantong_ikan, jumlah_kantong): 
    kantong_ikan.sort(reverse=True)  # Urutkan kantong-kantong berdasarkan jumlah ikan (terbesar ke terkecil) 
    kantong_terpilih = kantong_ikan[:jumlah_kantong]  # Ambil n kantong teratas sesuai dengan jumlah yang diinginkan 
    total_ikan = sum(kantong_terpilih)  # Hitung total ikan dalam kantong yang terpilih 
    return kantong_terpilih, total_ikan  

if __name__ == "__main__": 
    kantong_ikan = [3, 5, 2, 8, 4, 6, 6, 3]  # Jumlah ikan dalam setiap kantong 
    jumlah_kantong_yang_dibawa = 4  # Jumlah kantong yang dapat dibawa oleh Pak Arman (aka Pak Budi :-)
    kantong_terpilih, total_ikan = greedy_bag_selection(kantong_ikan, jumlah_kantong_yang_dibawa) 
  
    print("Kantong-kantong yang harus dibawa oleh Pak Arman beserta jumlah ikan di setiap kantong:") 
    for i, jumlah in enumerate(kantong_terpilih, start=1): 

        print(f"Kantong {i}: {jumlah} ikan") 
    print(f"Total ikan dalam {jumlah_kantong_yang_dibawa} kantong: {total_ikan} ikan") 
