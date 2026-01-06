from flask import Blueprint, request, session, jsonify
from services.auth_service import login_or_signup, AuthError
from psycopg2.extras import RealDictCursor
from db import get_db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        user_id = login_or_signup(cur, username, password)
        conn.commit()
    except AuthError as e:
        conn.rollback()
        return jsonify(message=str(e)), 401
    except Exception:
        conn.rollback()
        return jsonify(message="サーバーエラー"), 500
    finally:
        cur.close()
        conn.close()

    session["self_id"] = user_id
    return "", 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return "", 200
