import sqlite3
Koneksi = sqlite3.connect('database_hewan.db')
kursor = Koneksi.cursor()

id_hewan = 3
asal= 'Nusa Tenggara Timur'



kursor.execute(f"UPDATE HEWAN  SET asal = '900' WHERE id_hewan = '3' ")
Koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data hewan dengan ID{id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")
    
Koneksi.close()   