import os

directory = "/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/"
files = [f for f in os.listdir(directory) if f.endswith('.php')]

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the text inside the anchor tag
    new_content = content.replace(">Other Projects</a>", ">Archives</a>")
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
