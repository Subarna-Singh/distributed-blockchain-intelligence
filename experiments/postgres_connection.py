import psycopg 

conn = psycopg.connect(
    host = "localhost",
    port = 5432,
    dbname = "mydatabase",
    user = "postgres",
    password = "password"
)

with conn.cursor() as cur:
    cur.execute("SELECT 1")
    print(cur.fetchone())

conn.rollback()
print(conn)
conn.close()
print(conn)