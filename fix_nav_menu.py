import os
import re
import glob

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'
html_files = glob.glob(os.path.join(directory, '*.html'))

# The canonical nav order (from index.html):
# [LOGO] | Home | Graphic Design | Logo | Illustration | Photography | [LOGO] | Hire Me | About Us | Shop | Contact

for filepath in html_files:
    basename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Find the nav-items ul block
    match = re.search(r'(<ul class="nav-items">)(.*?)(</ul>)', content, re.DOTALL)
    if not match:
        continue
    
    # Determine which page is active
    active_page = None
    if basename == 'index.html':
        active_page = 'home'
    elif basename == 'graphic-design.html':
        active_page = 'graphic-design'
    elif basename == 'logo.html':
        active_page = 'logo'
    elif basename == 'illustration.html':
        active_page = 'illustration'
    elif basename == 'photography.html':
        active_page = 'photography'
    elif basename == 'services.html':
        active_page = 'services'
    elif basename == 'about.html':
        active_page = 'about'
    elif basename == 'contact.html':
        active_page = 'contact'
    elif basename == 'projects.html':
        active_page = 'projects'
    # Other pages don't have an active nav item
    
    def make_link(href, text, page_key):
        if active_page == page_key:
            return f'                        <li><a href="{href}" class="active">{text}</a></li>'
        return f'                        <li><a href="{href}">{text}</a></li>'
    
    # Build the canonical nav
    nav_items = []
    nav_items.append('                        <li><a href="/" class="logo"><img src="images/liewright_logo.png" alt="Liewright Logo"></a></li>')
    nav_items.append(make_link('/', 'Home', 'home'))
    nav_items.append(make_link('graphic-design.html', 'Graphic Design', 'graphic-design'))
    nav_items.append(make_link('logo.html', 'Logo', 'logo'))
    nav_items.append(make_link('illustration.html', 'Illustration', 'illustration'))
    nav_items.append(make_link('photography.html', 'Photography', 'photography'))
    nav_items.append('                        <li><a href="/" class="logo"><img src="images/liewright_logo.png" alt="Liewright Logo"></a></li>')
    nav_items.append(make_link('services.html', 'Hire Me', 'services'))
    nav_items.append(make_link('about.html', 'About Us', 'about'))
    nav_items.append('                        <li><a href="https://shop.liewright.com" target="_blank">Shop</a></li>')
    nav_items.append(make_link('contact.html', 'Contact', 'contact'))
    
    new_nav_content = '\n'.join(nav_items)
    new_nav_block = f'<ul class="nav-items">\n{new_nav_content}\n                    </ul>'
    
    content = content[:match.start()] + new_nav_block + content[match.end():]
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Standardized nav in {basename}")
    else:
        print(f"Nav already correct in {basename}")
