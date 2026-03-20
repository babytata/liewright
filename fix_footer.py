import glob
import re

files = glob.glob('*.html')
updated = []

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    orig_content = content

    # Replace "<h4>Liewright</h4>" with "<h4>Company</h4>" or something else.
    # User said "rename the word Liewright in the first column in the footer."
    # We will rename it to "Company" for now, and I will mention it to the user.
    content = content.replace('<h4>Liewright</h4>', '<h4>Company</h4>')

    # Add Shop to the first column after About Us and before Contact:
    # 
    #                 <a href="about.html">About Us</a>
    #                 <a href="contact.html">Contact</a>
    
    if '<a href="https://shop.liewright.com" target="_blank">Shop</a>' not in content.split('<footer>')[1]:
        content = content.replace(
            '<a href="about.html">About Us</a>\n                <a href="contact.html">Contact</a>',
            '<a href="about.html">About Us</a>\n                <a href="https://shop.liewright.com" target="_blank">Shop</a>\n                <a href="contact.html">Contact</a>'
        )

    if content != orig_content:
        with open(filepath, 'w') as f:
            f.write(content)
        updated.append(filepath)

print(f"Updated {len(updated)} files")
