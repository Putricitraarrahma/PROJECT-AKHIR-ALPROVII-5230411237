import sqlite3
Koneksi = sqlite3.connect('database_hewan.db')
kursor = Koneksi.cursor()

#MENAMPILKAN SEMUA DATA  DALAM DATABASE
kursor.execute("SELECT * FROM ")
baris_tabel = kursor.fetchall()

# BUAT TABEL PEAWAI
print("DATA HEWAN LANGKA")
print('='*80)
print("{:<5} {:<20} {:<20} {:<20} {:<20}" .format("ID","Nama","Jenis", "Asal", "jml_skrng", "Thn_ditemukan"))

print("-"*80)

for baris in baris_tabel:
  print("{:<5} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3], baris[4]))

print("-"*80)  
Koneksi.close()