document.getElementById("login-button").addEventListener("click", async () => {
  const username = document.getElementById("login-username").value.trim();
  const password = document.getElementById("login-password").value;

  const errorEl = document.getElementById("login-error");
  errorEl.textContent = "";

  if (!username || !password) {
    errorEl.textContent = "未入力";
    return;
  }

  const res = await fetch("/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      action: "login",
      username,
      password,
    }),
  });

  if (!res.ok) {
    const data = await res.json();
    errorEl.textContent = data.message ?? "ログイン失敗";
    return;
  }

  // 成功したら state を進める
  appState.screen = "landing";
  render();
});
