def fetch_planet_size(cur, planet_id):
    cur.execute(
        "SELECT width, height FROM planets WHERE id = %s",
        (planet_id,)
    )
    return cur.fetchone()

def fetch_planet_row(cur, planet_id):
    cur.execute(
        """
        SELECT
            id,
            name,
            width,
            height,
            created_at,
            created_name
        FROM planets
        WHERE id = %s
        """,
        (planet_id,)
    )
    return cur.fetchone()
