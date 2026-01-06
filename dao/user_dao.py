from werkzeug.security import generate_password_hash, check_password_hash

def find_user_by_username(cur, username: str):
    cur.execute(
        "SELECT id, password_hash FROM users WHERE username = %s",
        (username,)
    )
    return cur.fetchone()  # dict 前提


def create_user(cur, username: str, password: str) -> int:
    password_hash = generate_password_hash(password)

    cur.execute(
        """
        INSERT INTO users (username, password_hash)
        VALUES (%s, %s)
        RETURNING id
        """,
        (username, password_hash)
    )
    return cur.fetchone()["id"]


def update_user_position(cur, user_id, planet_id, x, y, direction):
    cur.execute(
        """
        UPDATE users
        SET planet_id = %s,
            x = %s,
            y = %s,
            direction = %s
        WHERE id = %s
        """,
        (planet_id, x, y, direction, user_id)
    )
def verify_password(stored_hash: str, password: str) -> bool:
    return check_password_hash(stored_hash, password)

def fetch_user_row(cur, user_id, *, lock=False):
    sql = """
        SELECT
            id,
            username,
            planet_id,
            x,
            y,
            direction,
            stardust,
            last_updated,
            created_at
        FROM users
        WHERE id = %s
    """
    if lock:
        sql += " FOR UPDATE"

    cur.execute(sql, (user_id,))
    return cur.fetchone()

def update_user_stardust(cur, user_id, stardust, last_updated):
    cur.execute(
        """
        UPDATE users
        SET stardust = %s,
            last_updated = %s
        WHERE id = %s
        """,
        (stardust, last_updated, user_id)
    )
