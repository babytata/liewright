# Liewright Website Development Log

This document serves as a comprehensive log of the steps taken to build and refine the Liewright website, including the structural changes, interactive features, and deployment preparations.

## 1. Initial Setup and Structure
*   **Foundation:** The website was initially built using PHP to allow for dynamic inclusion of components (like footers and headers) across multiple pages.
*   **Page Creation:** Core pages were established, including `index.php` (Home), `about.php`, `contact.php`, and various portfolio pages (`graphic-design.php`, `logo.php`, `illustration.php`, `photography.php`).
*   **Project Pages:** Added an `projects.php` (later renamed Archives) page to showcase apps, websites, and design projects.

## 2. Global Component Standardization
*   **Footer Refinement:** 
    *   Standardized the footer across all pages to ensure a consistent, responsive layout with columns for "Liewright", "Collections", "Network", and "Legal".
    *   Updated footer headings (e.g., changed "Work" to "Collections", "Projects" to "Network").
    *   Renamed "Other Projects" to "Archives" and removed the "Apps" link from the footer.
    *   Added the `liewright_logo.png` to the footer.
*   **Navigation Updates:** 
    *   Implemented an edge-scrolling carousel effect for the top navigation bar, removing the need for manual left/right arrow buttons. The navigation now infinitely scrolls when hovering near the edges of the navigation area.

## 3. Page-Specific Enhancements
*   **Homepage Gallery/Hero Section:**
    *   Replaced standard hero sections with a dynamic, screen-filling typographic grid of letters (`GRAPHICDESIGNLOGOILLUSTRATIONPHOTOGRAPHYART`).
    *   Implemented a "flashlight" / "reverse hole" hover effect where grey filler letters fade cleanly to black based on mouse proximity.
    *   Added custom tooltips to the white header characters that display design-related quotes upon hover. 
    *   **Zoom Fix:** Adjusted the hero section's Flexbox properties (`align-items: flex-start`, `padding-top`) so that scaling/zooming the page forces the text block to grow downwards, preventing the top row (and tooltips) from disappearing off-screen.
*   **Gallery Ad Placement:**
    *   Added a PHP script to seamlessly inject an "Ad Placeholder" specific image into the gallery layouts of the portfolio pages (`graphic-design.php`, etc.). The script ensures the ad never appears as the very first item in the gallery.
*   **Contact Page:**
    *   Added form validation logic with PHP.

## 4. App & Project Integrations (YouTwo & Soundulator)
*   **YouTwo Landing Page:**
    *   Created `rork-youtwo-landing.html` (later renamed to `youtwo-landing.html`).
    *   Removed mentions of "Rork" from the file name and updated internal links.
    *   Adapted features specifically to the current state of the app: removed icons for "Auto-Save Everything" and others, and changed the primary call-to-action buttons to "Coming Soon".
    *   Fixed a bug where the internal smooth-scrolling was extremely slow by changing the scroll behavior to `auto`.
*   **Privacy Policies:**
    *   Created dedicated privacy policy pages for the main site (`liewright-privacy-policy.php`) and the YouTwo app (`youtwo-privacy-policy.html`) to clarify that no user data is collected or tracked.
*   **Archive Page Updates:**
    *   Updated the App 1 thumbnail to use `YouTwo.jpg` (with high-res `@1.5x` support) and initially linked to the YouTwo landing page.
    *   Updated Website 1 thumbnail to use `Calculator.jpg` (with `@1.5x` support) and initially linked to `soundulator.php`.
    *   **Pre-Release Modification:** Later broke the links for both App 1 and Website 1 on the Archives page, replacing them with a JavaScript `alert('Coming Soon!')` and adding "(Coming Soon)" to their titles to restrict access prior to their official launch.

## 5. Netlify Deployment Preparation (Transition to Static HTML)
*   **Requirement:** Netlify hosting required the site to be purely static HTML, as it does not execute PHP natively.
*   **Automation:** Wrote a Python script (`convert_php_to_html.py`) to automate the transition:
    *   Replaced dynamic PHP blocks (e.g., `<?php echo date("Y"); ?>`) with hardcoded static equivalents (e.g., `2026`).
    *   Updated all internal `href` links from `.php` to `.html`.
    *   Bulk-renamed all 13 `.php` files to `.html`.
*   **Contact Form Update:** Stripped the manual PHP email handling from `contact.html` and replaced it with `<form name="contact" method="post" data-netlify="true">`, allowing Netlify's built-in form detection to automatically capture and process user submissions.

*This log serves as a living document and can be referenced for any future debugging or structural restorations.*
