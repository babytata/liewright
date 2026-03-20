import glob
import re

files = glob.glob('*.html')
updated = []

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    orig_content = content

    # Add to Navigation
    nav_item_pattern = r'(<li><a href="contact\.html"[^>]*>Contact</a></li>)'
    nav_replacement = r'<li><a href="https://liewright.company.site" target="_blank">Shop</a></li>\n                        \1'

    if '<li><a href="https://liewright.company.site"' not in content:
        content = re.sub(nav_item_pattern, nav_replacement, content)

    # Add to Footer
    footer_pattern = r'(<a href="contact\.html"[^>]*>Contact</a>)'
    footer_replacement = r'\1\n                <a href="https://liewright.company.site" target="_blank">Shop</a>'

    if '<a href="https://liewright.company.site" target="_blank">Shop</a>' not in content:
        content = re.sub(footer_pattern, footer_replacement, content)

    if content != orig_content:
        with open(filepath, 'w') as f:
            f.write(content)
        updated.append(filepath)

print(f"Updated {len(updated)} files: {', '.join(updated)}")
