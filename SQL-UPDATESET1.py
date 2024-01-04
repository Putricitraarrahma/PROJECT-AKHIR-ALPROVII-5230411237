import sqlite3
Koneksi = sqlite3.connect('database_hewan.db')
kursor = Koneksi.cursor()


id_hewan = 1
jml_skrng= '900'


kursor.execute(f"UPDATE HEWAN SET asal = 'Nusa Tenggara Timur' WHERE id_hewan = '1'")
Koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data hewan dengan ID{id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")
    
Koneksi.close()    
