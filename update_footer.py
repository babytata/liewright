import os

directory = "/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/"
files = [f for f in os.listdir(directory) if f.endswith('.php')]

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("<h4>Work</h4>", "<h4>Collections</h4>")
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
