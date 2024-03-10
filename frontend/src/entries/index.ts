import "vite/modulepreload-polyfill";

import focus from "@alpinejs/focus";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import ui from "@alpinejs/ui";
import Alpine from "alpinejs";
import ScrollHint from "scroll-hint";

import "../styles/index.css";

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
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", () => {
            onDOMContentLoaded();
        });
    } else {
        onDOMContentLoaded();
    }
})();
