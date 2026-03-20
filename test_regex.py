import re

with open('index.html', 'r') as f:
    content = f.read()

pattern = r'(<a href="/" class="mobile-logo-link"><img src="images/liewright_logo\.png" alt="Liewright Logo" class="mobile-logo"></a>)\s*(<!-- Mobile Menu Button -->\s*<button class="mobile-menu-btn" aria-label="Toggle Menu">\s*<span class="hamburger-line"></span>\s*<span class="hamburger-line"></span>\s*<span class="hamburger-line"></span>\s*</button>)'

matches = re.findall(pattern, content)
print(f"Matches: {len(matches)}")
