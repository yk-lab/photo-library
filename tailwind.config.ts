module.exports = {
  content: [
    './backend/**/*.py',
    './backend/templates/**/*.html',
    './backend/*/templates/**/*.html',
    './frontend/src/**/*.ts',
    './.venv/lib/python3.12/site-packages/allauth/**/*',
    './.venv/lib/python3.12/site-packages/crispy_tailwind/**/*',
    '/usr/local/lib/python3.12/site-packages/allauth/**/*',
    '/usr/local/lib/python3.12/site-packages/crispy_tailwind/**/*',
  ],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {},
  },
  plugins: [
    // tailwindcss typography
    require('@tailwindcss/typography'),
    // tailwindcss forms
    require('@tailwindcss/forms'),
  ],
};
