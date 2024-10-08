function init() {
  preloadTheme();

  const lightThemeButton = document.getElementById("light-theme-button");
  lightThemeButton?.addEventListener("click", () => {
    localStorage.setItem("theme", "light");
    toggleTheme(false);
  });

  const darkThemeButton = document.getElementById("dark-theme-button");
  darkThemeButton?.addEventListener("click", () => {
    localStorage.setItem("theme", "dark");
    toggleTheme(true);
  });

  const systemThemeButton = document.getElementById(
    "system-theme-button",
  );

  systemThemeButton?.addEventListener("click", () => {
    localStorage.setItem("theme", "system");
    toggleTheme(
      window.matchMedia("(prefers-color-scheme: dark)").matches,
    );
  });

  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", (event) => {
      if (localStorage.theme === "system") {
        toggleTheme(event.matches);
      }
    });
}

function toggleTheme(dark) {
  const css = document.createElement("style");

  css.appendChild(
    document.createTextNode(
      `* {
       -webkit-transition: none !important;
       -moz-transition: none !important;
       -o-transition: none !important;
       -ms-transition: none !important;
       transition: none !important;
    }
  `,
    ),
  );

  document.head.appendChild(css);

  if (dark) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }

  window.getComputedStyle(css).opacity;
  document.head.removeChild(css);
}

function preloadTheme() {
  const userTheme = localStorage.theme;

  if (userTheme === "light" || userTheme === "dark") {
    toggleTheme(userTheme === "dark");
  } else {
    toggleTheme(
      window.matchMedia("(prefers-color-scheme: dark)").matches,
    );
  }
}

document.addEventListener("DOMContentLoaded", () => init());
document.addEventListener("astro:after-swap", () => init());
preloadTheme();