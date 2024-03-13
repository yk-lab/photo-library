import * as Sentry from "@sentry/browser";
import Cookies from "js-cookie";
import { ofetch } from 'ofetch';

/**
 * Logout class
 * @param {string} url - The url to logout
 * @param {string} method - The method to use
 * @param {Record<string, unknown>} data - The data to send
 *
 * @see https://inertiajs.com/links
 */
class Logout {
  constructor(private url: string, private method: string, private data: Record<string, unknown> = {}) { }

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
      Sentry.captureException(err);
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
