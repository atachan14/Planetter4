from dao.user_dao import (
    find_user_by_username,
    create_user,
    verify_password,
)


class AuthError(Exception):
    pass



def login_or_signup(cur, username: str, password: str) -> int:
    if not username or not password:
        raise AuthError("未入力です")

    user = find_user_by_username(cur, username)

    if user is None:
        # 新規作成
        user_id = create_user(cur, username, password)
        return user_id

    # 既存ユーザー
    if not verify_password(user["password_hash"], password):
        raise AuthError("パスワードが違います")

    return user["id"]
