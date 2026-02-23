import os
import re

directory = "/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/"
files = ['graphic-design.php', 'logo.php', 'photography.php', 'illustration.php']

new_ad_block = """                        <!-- Advertisement -->
                        <div class="gallery-item">
                            <a href="https://liewright.com/Dallies-Floral-Hand-&-Body-Wash-p605212100" target="_blank">
                                <img src="Assets/Ad/Dallies.jpg" alt="Advertisement" class="gallery-thumbnail">
                            </a>
                            <div class="gallery-item-title">Sponsored</div>
                        </div>"""

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r"[ \t]*<!-- Ad Placeholder -->\s*<div class=\"gallery-item ad-slot\">\s*<div class=\"gallery-thumbnail\">Ad Space</div>\s*<div class=\"gallery-item-title\">Advertisement</div>\s*</div>"
    
    new_content = re.sub(pattern, "\n" + new_ad_block, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find placeholder in {filename}")
