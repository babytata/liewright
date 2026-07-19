import os
import glob

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'
html_files = glob.glob(os.path.join(directory, '*.html'))

version_str = ' (v1.1.0)'

for filepath in html_files:
    basename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Update Liewright copyright
    liewright_target = '© 2026 Liewright LLC. All rights reserved. Designed & Developed by Liewright.'
    if liewright_target in content:
        # Check if version is already appended
        if version_str not in content:
            content = content.replace(liewright_target, liewright_target + version_str)
            
    # 2. Update Rooster Cleaning copyright
    rooster_target = '© 2026 Rooster Cleaning. All rights reserved.'
    if rooster_target in content:
        if version_str not in content:
            content = content.replace(rooster_target, rooster_target + version_str)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added version to {basename}")
    else:
        print(f"No copyright change in {basename}")
