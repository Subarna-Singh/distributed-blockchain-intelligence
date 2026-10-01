import psycopg 
import os

os.environ['POSTGRES_HOST']

def test_postgres_connection():
    conn = psycopg.connect(
    host=os.environ["POSTGRES_HOST"],
    port=os.environ["POSTGRES_PORT"],
    dbname=os.environ["POSTGRES_DB"],
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
)

    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        data = cur.fetchone()
        assert data[0] == 1
    
    conn.rollback()
    conn.close()