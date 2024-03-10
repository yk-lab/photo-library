module.exports = {
  content: [
    './backend/**/*.py',
    './backend/templates/**/*.html',
    './backend/*/templates/**/*.html',
    './frontend/src/**/*.ts',
    './.venv/lib/python3.11/site-packages/crispy_tailwind/templates/**/*.html',
    '/usr/local/lib/python3.11/site-packages/crispy_tailwind/templates/**/*.html',
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
