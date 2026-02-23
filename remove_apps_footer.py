import os
import re

directory = "/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/"
files = [f for f in os.listdir(directory) if f.endswith('.php')]

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the apps link line: <a href="apps.php">Apps</a>
    new_content = re.sub(r'\s*<a href="apps\.php">Apps</a>', '', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
