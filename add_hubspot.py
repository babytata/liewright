import os
import glob

hubspot_code = """<!-- Start of HubSpot Embed Code -->
  <script type="text/javascript" id="hs-script-loader" async defer src="//js-na2.hs-scripts.com/246359500.js"></script>
<!-- End of HubSpot Embed Code -->
</body>"""

directory = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php'

# Get all html files
html_files = glob.glob(os.path.join(directory, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'hs-script-loader' not in content:
        # replace the last occurrence of </body> or just the first occurrence
        # typically there's only one </body> tag
        if '</body>' in content:
            new_content = content.replace('</body>', hubspot_code)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added HubSpot code to {os.path.basename(filepath)}")
        else:
            print(f"Could not find </body> in {os.path.basename(filepath)}")
    else:
        print(f"HubSpot code already in {os.path.basename(filepath)}")
