import os
import glob
import re

files = glob.glob('*.html')
updated = []

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    orig_content = content

    # Swap CSS classes
    content = content.replace(
        '.mobile-logo-link { display: block; margin-left: 15px; }',
        '.mobile-logo-link { display: block; margin-right: 15px; margin-left: auto; }'
    )
    content = content.replace(
        '.mobile-menu-btn { margin-left: auto !important; margin-right: 15px !important; }',
        '.mobile-menu-btn { margin-left: 15px !important; margin-right: auto !important; }'
    )

    # Swap HTML order
    # The current order is:
    # <nav>
    # <a href="/" class="mobile-logo-link"><img src="images/liewright_logo.png" alt="Liewright Logo" class="mobile-logo"></a>
    # <!-- Mobile Menu Button -->
    # <button class="mobile-menu-btn" aria-label="Toggle Menu">
    #     <span class="hamburger-line"></span>
    #     <span class="hamburger-line"></span>
    #     <span class="hamburger-line"></span>
    # </button>

    pattern = re.compile(
        r'(<a href="/" class="mobile-logo-link"><img src="images/liewright_logo\.png" alt="Liewright Logo" class="mobile-logo"></a>)\s*'
        r'(<!-- Mobile Menu Button -->\s*'
        r'<button class="mobile-menu-btn" aria-label="Toggle Menu">\s*'
        r'<span class="hamburger-line"></span>\s*'
        r'<span class="hamburger-line"></span>\s*'
        r'<span class="hamburger-line"></span>\s*'
        r'</button>)'
    )

    content = pattern.sub(r'\2\n        \1', content)

    if content != orig_content:
        with open(filepath, 'w') as f:
            f.write(content)
        updated.append(filepath)

print(f"Updated {len(updated)} files: {', '.join(updated)}")

