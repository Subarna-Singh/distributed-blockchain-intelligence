from dotenv import load_dotenv

from blockchain_intelligence.db.connection import get_connection

load_dotenv()

def test_postgres_connection():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            data = cur.fetchone()
            assert data[0] == 1
