import os
import glob
import re

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'

# Find all php files
php_files = glob.glob(os.path.join(directory, '*.php'))

for filepath in php_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Replacements
    # 1. replace <?php echo date("Y"); ?>
    content = re.sub(r'<\?php\s+echo\s+date\("Y"\);\s+\?>', '2026', content)
    
    # 2. replace <?php echo date("F j, Y"); ?>
    content = re.sub(r'<\?php\s+echo\s+date\("F j, Y"\);\s+\?>', 'February 21, 2026', content)
    
    # 3. internal .php links to .html (excluding dynamic PHP paths for contact form, which we'll handle separately but this regex is safe enough)
    content = re.sub(r'href="([^"]+)\.php"', r'href="\1.html"', content)

    # Note: Contact.php specific PHP code will be removed by the agent's tool separately.

    with open(filepath, 'w') as f:
        f.write(content)

# Rename files
for filepath in php_files:
    new_filepath = filepath[:-4] + '.html'
    os.rename(filepath, new_filepath)

print(f"Processed and renamed {len(php_files)} files.")
