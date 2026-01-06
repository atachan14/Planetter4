// top.js

document.addEventListener("DOMContentLoaded", () => {
  const loginButton = document.getElementById("login-button");
  const usernameInput = document.getElementById("login-username");
  const passwordInput = document.getElementById("login-password");
  const errorEl = document.getElementById("login-error");

  loginButton.addEventListener("click", async () => {
    errorEl.textContent = "";

    const username = usernameInput.value.trim();
    const password = passwordInput.value;

    if (!username) {
      errorEl.textContent = "アカウント名が未入力です";
      return;
    }
     if (!password) {
      errorEl.textContent = "パスワードが未入力です";
      return;
    }
    try {
      const res = await fetch("/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        errorEl.textContent = data.message || "パスワードが間違っています";
        return;
      }

      // 認証成功 → main へ
      const html = await fetch("/partial/main").then(r => r.text());
      document.getElementById("app-root").innerHTML = html;

    } catch (e) {
      errorEl.textContent = "通信エラー";
    }
  });

  // Enterキー対応（任意）
  passwordInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      loginButton.click();
    }
  });
});