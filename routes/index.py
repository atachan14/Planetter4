from flask import Blueprint, render_template, request,session
index_bp = Blueprint("index", __name__)

@index_bp.route("/", methods=["GET"])
def index_get():
    if "self_id" not in session:
        return render_template("login.jinja")

    return render_template("world_shell.jinja")

@index_bp.route("/", methods=["POST"])
def index_post():
    action = request.form.get("action")

    if action == "login":
        handle_login()
        return redirect("/")

    if action == "logout":
        handle_logout()
        return redirect("/")

    # ここから下はログイン後専用
    if "self_id" not in session:
        return redirect("/")

    # in-game action
    dispatch_action(action)
    return redirect("/")
