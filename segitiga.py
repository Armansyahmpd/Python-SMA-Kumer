# Program untuk menentukan jenis segitiga
# Buku Siswa IKM Informatika untuk SMA Kelas XI Hal. 20
# 3. Mengimplementasikan Solusi dalam Bentuk Program (Coding)
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id

def cek_segitiga(sisi_a, sisi_b, sisi_c): 
    if sisi_a == sisi_b == sisi_c: 
        return "Segitiga adalah segitiga sama sisi" 
    elif sisi_a == sisi_b or sisi_a == sisi_c or sisi_b == sisi_c: 
        return "Segitiga adalah segitiga sama kaki" 
    elif sisi_a <= sisi_b <= sisi_c: 
      return "Bukan Segitiga" 
    else: 
        return "Segitiga sembarang" 
      
# Mengambil input dari pengguna 
sisi_a = float(input("Masukkan panjang sisi a: ")) 
sisi_b = float(input("Masukkan panjang sisi b: ")) 
sisi_c = float(input("Masukkan panjang sisi c: ")) 

# Memanggil fungsi dan mencetak hasilnya 
jenis_segitiga = cek_segitiga(sisi_a, sisi_b, sisi_c) 
print(jenis_segitiga) 
