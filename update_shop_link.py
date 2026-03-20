import glob

files = glob.glob('*.html')
updated = []

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    orig_content = content

    # Replace the old URL with the new URL
    content = content.replace('https://liewright.company.site', 'https://shop.liewright.com')

    if content != orig_content:
        with open(filepath, 'w') as f:
            f.write(content)
        updated.append(filepath)

print(f"Updated {len(updated)} files: {', '.join(updated)}")
