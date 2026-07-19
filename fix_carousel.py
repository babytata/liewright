import os
import re
import glob

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'
html_files = glob.glob(os.path.join(directory, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # Fix 1: Update mouseenter to also capture the initial mouseX position 
    # so the carousel doesn't jump when mouse first enters.
    # Also reset currentScrollSpeed to 0 on enter so there's no leftover momentum.
    
    # Pattern with double quotes
    content = content.replace(
        'carousel.addEventListener("mouseenter", () => isNavMouseOver = true);',
        'carousel.addEventListener("mouseenter", (e) => { isNavMouseOver = true; mouseX = e.clientX; currentScrollSpeed = 0; targetScrollSpeed = 0; });'
    )
    
    # Pattern with single quotes
    content = content.replace(
        "carousel.addEventListener('mouseenter', () => isNavMouseOver = true);",
        "carousel.addEventListener('mouseenter', (e) => { isNavMouseOver = true; mouseX = e.clientX; currentScrollSpeed = 0; targetScrollSpeed = 0; });"
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed carousel in {os.path.basename(filepath)}")
    else:
        print(f"No carousel fix needed in {os.path.basename(filepath)}")
