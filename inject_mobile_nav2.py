import glob

html_injection = """
        <!-- Mobile Menu Button -->
        <button class="mobile-menu-btn" aria-label="Toggle Menu">
            <span class="hamburger-line"></span>
            <span class="hamburger-line"></span>
            <span class="hamburger-line"></span>
        </button>"""

css_injection = """
        /* Mobile Menu */
        .mobile-menu-btn { display: none; flex-direction: column; justify-content: space-between; width: 30px; height: 21px; background: transparent; border: none; cursor: pointer; z-index: 1001; margin-left: auto; margin-right: 15px; margin-top: 15px; margin-bottom: 15px; }
        .hamburger-line { width: 100%; height: 2px; background-color: #bdccd4; transition: all 0.3s ease; }
        
        @media (max-width: 768px) {
            .mobile-menu-btn { display: flex; }
            nav { flex-wrap: wrap; position: relative; }
            .nav-carousel, .nav-carousel-container { display: none; width: 100%; }
            nav.active .nav-carousel, nav.active .nav-carousel-container { display: flex; position: absolute; top: 100%; left: 0; right: 0; width: 100vw; background-color: #1c1c1c; flex-direction: column; align-items: center; padding: 20px 0; border-bottom: 2px solid #bbbdbf; z-index: 1000; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5); overflow: visible; }
            nav.active .nav-items-container { overflow: visible; display: flex; justify-content: center; width: 100%; }
            nav.active .nav-items { display: flex; flex-direction: column; width: 100%; transform: none !important; animation: none; gap: 20px; text-align: center; justify-content: center; overflow: visible; }
            nav.active .scroll-btn { display: none; }
            nav.active .nav-items > li, nav.active .nav-items > a { display: block; width: 100%; }
            .current-page { display: none; }
            
            nav.active .mobile-menu-btn .hamburger-line:nth-child(1) { transform: translateY(9.5px) rotate(45deg); }
            nav.active .mobile-menu-btn .hamburger-line:nth-child(2) { opacity: 0; }
            nav.active .mobile-menu-btn .hamburger-line:nth-child(3) { transform: translateY(-9.5px) rotate(-45deg); }
        }
    </style>"""

js_injection_replacement = """        document.addEventListener('DOMContentLoaded', function () {
            // Mobile Menu Toggle
            const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
            const nav = document.querySelector('nav');
            if (mobileMenuBtn && nav) {
                mobileMenuBtn.addEventListener('click', () => {
                    nav.classList.toggle('active');
                });
            }"""

target_files = []
for file in glob.glob("*.html"):
    if file.startswith("freenote-") or file.startswith("youtwo-"):
        continue
    target_files.append(file)

for file in target_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Re-inject HTML properly
    # If the old button is there from the first script but in the wrong place, it won't be there because the condition failed.
    if "<!-- Mobile Menu Button -->" not in content:
        if '<nav>' in content:
            content = content.replace('<nav>', f'<nav>{html_injection}', 1)
        elif '<nav ' in content:
            # handle case where nav has attributes
            parts = content.split('<nav ', 1)
            rest = parts[1].split('>', 1)
            content = parts[0] + '<nav ' + rest[0] + '>' + html_injection + rest[1]

    # Re-inject CSS
    # Let's remove the previous CSS block to keep it clean if it exists
    if "/* Mobile Menu */" in content:
        start_idx = content.find("/* Mobile Menu */")
        end_idx = content.find("</style>", start_idx) + len("</style>")
        if end_idx > start_idx:
            content = content[:start_idx] + css_injection + content[end_idx:]
    else:
        if "</style>" in content:
            content = content.replace('</style>', css_injection, 1)

    # Re-inject JS
    # Determine if old JS was injected
    if "// Mobile Menu Toggle" in content:
        # replace the old JS block
        start_idx = content.find("// Mobile Menu Toggle")
        end_idx = content.find("}", content.find("});", start_idx) + 3) + 1
        
        new_js = """            // Mobile Menu Toggle
            const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
            const nav = document.querySelector('nav');
            if (mobileMenuBtn && nav) {
                mobileMenuBtn.addEventListener('click', () => {
                    nav.classList.toggle('active');
                    // Force display block on nav-items-container for older browsers/stuck elements
                    const itemsContainers = document.querySelectorAll('.nav-items-container, .nav-carousel, .nav-carousel-container');
                    itemsContainers.forEach(el => {
                        if (nav.classList.contains('active')) {
                            el.style.display = 'flex';
                        } else {
                            el.style.display = '';
                        }
                    });
                });
            }"""
        if end_idx > start_idx and "mobileMenuBtn.addEventListener" in content[start_idx:end_idx]:
             content = content[:start_idx] + new_js + content[end_idx:]
    else:
        if "document.addEventListener('DOMContentLoaded', function () {" in content:
             content = content.replace("document.addEventListener('DOMContentLoaded', function () {", js_injection_replacement, 1)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed {len(target_files)} files.")
