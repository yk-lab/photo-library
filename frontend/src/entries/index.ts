import "vite/modulepreload-polyfill";

import focus from "@alpinejs/focus";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import ui from "@alpinejs/ui";
import * as Sentry from "@sentry/browser";
import Alpine from "alpinejs";
import ScrollHint from "scroll-hint";

import LogoutButton from "../utils/logout-button";

import "../styles/index.css";

if (import.meta.env.VITE_SENTRY_DSN) {
  Sentry.init({
    dsn: import.meta.env.VITE_SENTRY_DSN,
    environment: import.meta.env.VITE_ENVIRONMENT,

    // Alternatively, use `process.env.npm_package_version` for a dynamic release version
    // if your build tool supports it.
    // release: "my-project-name@2.3.12",
    integrations: [
      Sentry.browserTracingIntegration(),
      Sentry.replayIntegration(),
      Sentry.feedbackIntegration(),
    ],

    // Set tracesSampleRate to 1.0 to capture 100%
    // of transactions for performance monitoring.
    // We recommend adjusting this value in production
    // tracesSampleRate: 1.0,
    tracesSampleRate: 0.1, // TODO: 設定変更できるようにする

    // Set `tracePropagationTargets` to control for which URLs distributed tracing should be enabled
    tracePropagationTargets: [location.hostname],

    // Capture Replay for 10% of all sessions,
    // plus for 100% of sessions with an error
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
  });
}


(() => {
  const onDOMContentLoaded = () => {
    new ScrollHint("[data-scroll-hint]", {
      suggestiveShadow: true,
      i18n: {
        scrollable: "スクロールできます",
      },
    });

    Alpine.plugin(focus);
    Alpine.plugin(ui);
    Alpine.start();

    LogoutButton.capture();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      onDOMContentLoaded();
    });
  } else {
    onDOMContentLoaded();
  }
})();
