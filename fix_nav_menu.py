import os
import re
import glob

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'

# Get all html files in root directory only (not subdirectories)
html_files = glob.glob(os.path.join(directory, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix the broken nav pattern:
    # There's a duplicate "Hire Me" <li> where "About Us" is nested inside it.
    # Pattern: <li><a href="services.html">Hire Me</a></li>   (correct first one)
    #          <li><a href="services.html">Hire Me</a>        (duplicate, broken)
    #     <a href="about.html">About Us</a></li>              (About Us trapped inside)
    # 
    # Should become:
    #          <li><a href="services.html">Hire Me</a></li>   (keep only one)
    #          <li><a href="about.html">About Us</a></li>     (About Us in its own <li>)
    
    # Match the broken pattern - the duplicate Hire Me li with About Us nested in it
    # This handles the services.html case with class="active" separately
    
    # For pages OTHER than services.html (no class="active")
    pattern = re.compile(
        r'(\s*<li><a href="services\.html">Hire Me</a></li>\s*\n)'  # First correct Hire Me
        r'\s*<li><a href="services\.html">Hire Me</a>\s*\n'         # Duplicate Hire Me (opening)
        r'\s*<a href="about\.html">About Us</a></li>',              # About Us trapped inside
        re.MULTILINE
    )
    
    replacement = r'\1                        <li><a href="about.html">About Us</a></li>'
    content = pattern.sub(replacement, content)
    
    # Also handle the services.html case where Hire Me has class="active"
    pattern_active = re.compile(
        r'(\s*<li><a href="services\.html" class="active">Hire Me</a></li>\s*\n)'
        r'\s*<li><a href="services\.html" class="active">Hire Me</a>\s*\n'
        r'\s*<a href="about\.html">About Us</a></li>',
        re.MULTILINE
    )
    
    replacement_active = r'\1                        <li><a href="about.html">About Us</a></li>'
    content = pattern_active.sub(replacement_active, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed nav in {os.path.basename(filepath)}")
    else:
        print(f"No nav fix needed in {os.path.basename(filepath)}")
