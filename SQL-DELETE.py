import sqlite3
Koneksi = sqlite3.connect('database_hewan.db')
kursor = Koneksi.cursor()

jenis = 'Mamalia'
kursor.execute(f"DELETE FROM HEWAN WHERE jenis = ?", (jenis,))
Koneksi.commit()

if kursor.rowcount > 0:
    print(f"DATA hewan dengan jenis {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data hewan dengan jenis {jenis}.")    
    
Koneksi.close()    