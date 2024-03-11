import Cookies from "js-cookie";
import { ofetch } from 'ofetch';

class Logout {
  constructor(private url: string, private method: string, private data: Record<string, unknown> = {}) {
    this.url = url;
    this.method = method;
  }

  public async logout() {
    try {
      const resp = await ofetch<{
        location?: string | null;
      }>(this.url, {
        method: this.method,
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": Cookies.get("csrftoken") || "",
        },
        body: JSON.stringify(this.data),
      });
      if (resp.location) {
        window.location.href = resp.location;
      }
    } catch (err) {
      console.error("Failed to logout", err);
    }
  }
}


const LogoutButton = {
  capture() {
    for (const btn of document.querySelectorAll<HTMLButtonElement>("button[data-logout-button]")) {
      const url = btn.dataset.href || "";
      const method = btn.dataset.method || "GET";

      const logout = new Logout(url, method);
      btn.addEventListener("click", () => {
        logout.logout();
      });
    }
  },
}

export default LogoutButton;
