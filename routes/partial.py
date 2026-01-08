from flask import Blueprint, render_template, session, abort
from psycopg2.extras import RealDictCursor
from db import get_db
from dao.db_time import fetch_db_now
from services.data import fetch_latest_user_data,fetch_planet_data 

partial_bp = Blueprint("partial", __name__, url_prefix="/partial")

@partial_bp.route("/main")
def partial_main():
    if "self_id" not in session:
        abort(401)

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        db_now = fetch_db_now(cur)
        self_data = fetch_latest_user_data(cur, session["self_id"],db_now)
        planet_data = fetch_planet_data(cur, self_data.planet_id)
    finally:
        cur.close()
        conn.close()

    return render_template(
        "main.jinja",
        self_data=self_data,
        planet_data=planet_data,
    )
