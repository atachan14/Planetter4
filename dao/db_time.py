def fetch_db_now(cur):
    cur.execute("SELECT now()")
    return cur.fetchone()["now"]
