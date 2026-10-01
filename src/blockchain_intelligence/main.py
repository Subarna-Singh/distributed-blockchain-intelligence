from blockchain_intelligence.db.connection import get_connection

def main():
    print("Blockchain Intelligence service started")
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        data = cur.fetchone()
        print(f"Database connection test result: {data[0]}")

    conn.rollback()
    conn.close()


if __name__ == "__main__":
    main()