import psycopg2


conn = psycopg2.connect(

    host= '127.0.0.1',
    port= '5433',
    database= 'music-tour ',
    user= ' postgres',
    password= 'Azx2c3b#1'
)

cur = conn.cursor()

cur.execute("SELECT * FROM bands, events, stages")
rows = cur.fetchall()

for row in rows:
  print(row)

conn.close()
