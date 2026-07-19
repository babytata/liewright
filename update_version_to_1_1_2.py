import os
import glob

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'
html_files = glob.glob(os.path.join(directory, '*.html'))

for filepath in html_files:
    basename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '(v1.1.1)' in content:
        content = content.replace('(v1.1.1)', '(v1.1.2)')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated version to v1.1.2 in {basename}")
