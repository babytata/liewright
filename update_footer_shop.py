import glob

files = glob.glob('*.html')
updated = []

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    orig_content = content

    # 1. Rename the column header
    content = content.replace('<h4>Liewright</h4>', '<h4>Company</h4>')

    # 2. Add the Shop link to the footer list if not present
    if '<a href="https://shop.liewright.com" target="_blank">Shop</a>' not in content.split('<footer>')[1] if '<footer>' in content else True:
        content = content.replace(
            '<a href="about.html">About Us</a>\n                <a href="contact.html">Contact</a>',
            '<a href="about.html">About Us</a>\n                <a href="https://shop.liewright.com" target="_blank">Shop</a>\n                <a href="contact.html">Contact</a>'
        )

    if content != orig_content:
        with open(filepath, 'w') as f:
            f.write(content)
        updated.append(filepath)

print(f"Updated {len(updated)} files")
