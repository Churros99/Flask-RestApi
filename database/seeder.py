import sqlite3 as sql

DB_PATH = 'database/streamers.db'

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
                   create table streamers
                   (
                       name text,
                       subs integer,
                       followers integer
                   )
                   """)
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("Alexelcapo", 10000, 800000),
        ("Ibai", 25000, 7000000),
        ("elxokas", 10000, 1000000),
        ("auronplay", 20000, 8000000),
        ("cristinini", 5500, 3000000)
    ]
    cursor.executemany("insert into streamers values (?, ?, ?)", data)
    conn.commit()
    conn.close()
    
    
    
if(__name__=='__main__'):
    createDB()
    addValues()