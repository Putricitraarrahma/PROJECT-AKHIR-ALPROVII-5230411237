import sqlite3
Koneksi = sqlite3.connect('database_hewan.db')
kursor = Koneksi.cursor()


kursor.execute("SELECT SUM(jml_skrng) FROM HEWAN")
# mengambil satu baris gaji fetchone() dimulai dari indeks 0
total_populasi = kursor.fetchone()[0]

print(f"Jumlah total pupolasi hewan sekarang: {total_populasi}")
kursor.close()
