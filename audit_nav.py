import os
import re
import glob

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'
html_files = glob.glob(os.path.join(directory, '*.html'))

# The correct nav order should be consistent across all pages.
# Based on index.html (the canonical order):
# Logo | Home | Graphic Design | Logo | Illustration | Photography | Logo | Hire Me | About Us | Shop | Contact
#
# Services.html currently has Hire Me between Logo and Illustration, which is inconsistent.
# Let's check each page and see what nav they have.

for filepath in html_files:
    basename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the nav-items section
    match = re.search(r'<ul class="nav-items">(.*?)</ul>', content, re.DOTALL)
    if match:
        nav_html = match.group(1)
        # Extract link text in order
        links = re.findall(r'<a [^>]*>(.*?)</a>', nav_html)
        # Clean up image tags
        links = [re.sub(r'<img[^>]*>', '[LOGO]', l) for l in links]
        print(f"{basename}: {' | '.join(links)}")
    else:
        print(f"{basename}: NO NAV FOUND")
