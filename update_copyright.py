import os
import re

new_copyright = '© 2026 Liewright LLC. All rights reserved. Designed & Developed by Liewright.'

updated = 0
for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                
                content_mod, num = re.subn(r'© 2026 Liewright\s*—\s*All Rights Reserved\.', new_copyright, content)
                if num > 0:
                    with open(filepath, 'w') as f:
                        f.write(content_mod)
                    updated += 1
                    print(f"Updated {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total updated: {updated}")
