# Simulasi Enqueue dan Dequeue dalam Queue (tidak case sensitive)
# Buku Siswa IKM Informatika untuk SMA Kelas X Hal. 42
# Aktivitas BK-K10-05-U: Simulasi Queue
# Programmed by : Armansyah, S.Kom, M.Pd
# Guru Informatika SMAN Sumatera Selatan 
# armansyah@smansumsel.sch.id
# Alumni CS50 for Teachers Harvard-Indonesia 2022/2023
# Setiap copy-paste dan pengembangan harus mencantumkan informasi HAKI diatas


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            print("Nilai Queue saat ini 0, anda tidak dapat melakukan operasi Dequeue")
        else:
            return self.queue.pop(0)

    def display(self):
        return ", ".join(map(str, self.queue))

queue = Queue()

while True:
    perintah = input("Masukkan perintah (Enqueue X / Dequeue): ").lower()
    if perintah.startswith("enqueue"):
        _, angka = perintah.split()
        queue.enqueue(int(angka))
        print(queue.display())
    elif perintah == "dequeue":
        dequeued = queue.dequeue()
        if dequeued is not None:
            print(dequeued)
            print(queue.display())
    else:
        print("Perintah tidak valid!")

    jawaban = input("Apakah Anda ingin memasukkan perintah lagi? (Ya/Tidak): ").lower()
    if jawaban != "ya":
        print("Hasil dari total isi queue:", queue.display())
        break

