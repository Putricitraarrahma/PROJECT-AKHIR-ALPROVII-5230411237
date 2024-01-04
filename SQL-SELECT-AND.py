import sqlite3
Koneksi = sqlite3.connect('database_hewan.db')
kursor = Koneksi.cursor()


kursor.execute("SELECT * FROM HEWAN WHERE jenis = 'Mamalia' AND asal = 'Sumatera'")
baris_tabel = kursor.fetchall()

# BUAT TABEL HEWAN
print("DATA POPULASI HEWAN LANGKA")
print('='*110)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}" .format("id_hewan","nama_hewan","jenis", "asal", "jml_skrng", "thn_ditemukan"))

print("-"*110)

for baris in baris_tabel:
  print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3], baris[4], baris[5]))

print("-"*110)  
Koneksi.close()