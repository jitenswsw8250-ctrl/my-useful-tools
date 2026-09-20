# MY USEFUL TOOLS — Standalone Web Application Deployment Guide

This folder (`public/`) contains the complete standalone responsive web version of **MY USEFUL TOOLS** built purely with standard HTML5, CSS3, and modern JavaScript.

- **Zero backend dependencies**: 100% client-side calculation engine.
- **Zero APIs or keys**: No database, login, payments, or subscription services.
- **Includes all 5 functional calculators**:
  1. **Age Calculator** (Date of birth, exact age breakdown, next birthday countdown, zodiac sign, total days & hours lived).
  2. **EMI Loan Calculator** (Monthly EMI, total interest, total payment, visual proportion breakdown, year/month tenure).
  3. **Percentage Calculator** (3 modes: X% of Y, Percentage Increase/Decrease, and X is what % of Y).
  4. **Discount Calculator** (Original price, discount percentage chips, sales tax toggle, savings summary).
  5. **BMI Calculator** (Metric [cm/kg] and Imperial [ft/in/lbs], WHO health category badges, ideal weight range, visual scale).
- **All Legal & Informational Pages**: About Us, Contact Us with local feedback form, Privacy Policy, Terms & Conditions, and Disclaimer.
- **Responsive & Theme-ready**: Light/Dark mode toggle, mobile navigation drawer, and AdSense placeholder slots.

---

## Free Web Hosting Option 1: GitHub Pages (Recommended)

1. Create a free repository on [GitHub](https://github.com) named `my-useful-tools` (or `<your-username>.github.io`).
2. Upload or commit the files inside the `public/` directory:
   - `index.html`
   - `style.css`
   - `script.js`
   - `robots.txt`
   - `sitemap.xml`
   *(Ensure `index.html` is at the root of your GitHub repository or in the `/docs` folder).*
3. In your GitHub repository:
   - Go to **Settings** > **Pages**.
   - Under **Build and deployment**, set **Source** to `Deploy from a branch`.
   - Select the `main` (or `master`) branch and `/ (root)` folder, then click **Save**.
4. Within 1 minute, GitHub will provide a live, permanent HTTPS URL:
   `https://<your-username>.github.io/my-useful-tools/`

---

## Free Web Hosting Option 2: Vercel

1. Go to [Vercel](https://vercel.com) and log in (with your GitHub, GitLab, or email).
2. Click **Add New...** > **Project**.
3. Import your GitHub repository or use the **Vercel CLI** / drag-and-drop:
   - If using the repository, set the **Root Directory** to `public` (or place these 3 files in the repo root).
   - Framework Preset: Choose **Other** (Static HTML).
4. Click **Deploy**.
5. Vercel will instantly generate a free, global CDN web address:
   `https://my-useful-tools.vercel.app` (with free SSL and custom domain support).

---

## Free Web Hosting Option 3: Cloudflare Pages

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com) > **Workers & Pages**.
2. Click **Create Application** > **Pages** > **Upload assets**.
3. Create a project name (e.g. `my-useful-tools`).
4. Drag and drop the `public/` folder containing `index.html`, `style.css`, and `script.js`.
5. Click **Deploy Site**. Your website is immediately live at `https://my-useful-tools.pages.dev`.
