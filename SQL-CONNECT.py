import sqlite3
Koneksi = sqlite3.connect('database_hewan.db')


Koneksi.execute('''
                CREATE TABLE HEWAN(
                id_hewan  INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_hewan VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_skrng INTEGER(10),
                thn_ditemukan INTEGER(10)
                )
                ''')
Koneksi.close()