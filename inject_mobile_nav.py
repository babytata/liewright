import os
import glob

# Identify the target files
target_files = []
for file in glob.glob("*.html"):
    if file.startswith("freenote-") or file.startswith("youtwo-"):
        continue
    target_files.append(file)

print(f"Found {len(target_files)} target files.")

html_injection = """        <!-- Mobile Menu Button -->
        <button class="mobile-menu-btn" aria-label="Toggle Menu">
            <span class="hamburger-line"></span>
            <span class="hamburger-line"></span>
            <span class="hamburger-line"></span>
        </button>
        <div class="nav-carousel-container">"""

css_injection = """
        /* Mobile Menu */
        .mobile-menu-btn { display: none; flex-direction: column; justify-content: space-between; width: 30px; height: 21px; background: transparent; border: none; cursor: pointer; z-index: 1001; margin-right: 15px;}
        .hamburger-line { width: 100%; height: 2px; background-color: var(--text-color); transition: all 0.3s ease; }
        
        @media (max-width: 768px) {
            .mobile-menu-btn { display: flex; }
            .nav-carousel-container { display: none; }
            .nav-carousel-container.active { display: flex; position: absolute; top: 100%; left: 0; right: 0; width: 100vw; background-color: var(--bg-color); flex-direction: column; align-items: center; padding: 20px 0; border-bottom: 1px solid var(--border-color); z-index: 1000; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }
            .nav-carousel-container.active .nav-carousel { width: 100%; max-width: none; overflow: visible; padding: 0; mask-image: none; -webkit-mask-image: none; }
            .nav-carousel-container.active .nav-items { display: flex; flex-direction: column; width: 100%; transform: none !important; animation: none; gap: 20px; text-align: center; }
            .nav-carousel-container.active .scroll-btn { display: none; }
            .nav-carousel-container.active .nav-items li, .nav-carousel-container.active .nav-items a { display: block; width: 100%; }
            .current-page { display: none; }
            
            .mobile-menu-btn.open .hamburger-line:nth-child(1) { transform: translateY(9.5px) rotate(45deg); }
            .mobile-menu-btn.open .hamburger-line:nth-child(2) { opacity: 0; }
            .mobile-menu-btn.open .hamburger-line:nth-child(3) { transform: translateY(-9.5px) rotate(-45deg); }
        }
    </style>"""

js_injection = """        document.addEventListener('DOMContentLoaded', function () {
            // Mobile Menu Toggle
            const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
            const navCarouselContainer = document.querySelector('.nav-carousel-container');
            if (mobileMenuBtn && navCarouselContainer) {
                mobileMenuBtn.addEventListener('click', () => {
                    mobileMenuBtn.classList.toggle('open');
                    navCarouselContainer.classList.toggle('active');
                });
            }"""

for file in target_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply HTML Injection
    if "<!-- Mobile Menu Button -->" not in content and '<div class="nav-carousel-container">' in content:
        content = content.replace('<div class="nav-carousel-container">', html_injection, 1)
        
    # Apply CSS Injection
    if "/* Mobile Menu */" not in content and "</style>" in content:
        content = content.replace('</style>', css_injection, 1)
        
    # Apply JS Injection
    if "// Mobile Menu Toggle" not in content and "document.addEventListener('DOMContentLoaded', function () {" in content:
        content = content.replace("document.addEventListener('DOMContentLoaded', function () {", js_injection, 1)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injections complete.")
