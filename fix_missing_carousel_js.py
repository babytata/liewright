import os
import re

hover_js = """            // --- Nav Carousel Logic ---
            const carousel = document.querySelector('.nav-carousel');
            if (carousel) {
                const navItems = carousel.querySelector('.nav-items');
                if (navItems) {
                    const items = navItems.querySelectorAll('li');
                    items.forEach(item => {
                        let c = item.cloneNode(true);
                        c.classList.add('nav-clone');
                        navItems.appendChild(c);
                    });
                    items.forEach(item => {
                        let c = item.cloneNode(true);
                        c.classList.add('nav-clone');
                        navItems.appendChild(c);
                    });

                    let trackPos = 0;
                    let currentScrollSpeed = 0;
                    let targetScrollSpeed = 0;
                    let isNavMouseOver = false;
                    let mouseX = 0;

                    carousel.addEventListener('mouseenter', (e) => { isNavMouseOver = true; mouseX = e.clientX; currentScrollSpeed = 0; targetScrollSpeed = 0; });
                    carousel.addEventListener('mouseleave', () => {
                        isNavMouseOver = false;
                    });
                    carousel.addEventListener('mousemove', (e) => {
                        mouseX = e.clientX;
                    });

                    function navLoop() {
                        if (isNavMouseOver) {
                            const rect = carousel.getBoundingClientRect();
                            const width = rect.width;
                            const relativeX = mouseX - rect.left;
                            
                            const leftThreshold = width * 0.25;
                            const rightThreshold = width * 0.75;
                            
                            const maxSpeed = 3; 

                            if (relativeX < leftThreshold) {
                                const ratio = 1 - (relativeX / leftThreshold);
                                targetScrollSpeed = -1 * maxSpeed * ratio;
                            } else if (relativeX > rightThreshold) {
                                const ratio = (relativeX - rightThreshold) / (width - rightThreshold);
                                targetScrollSpeed = maxSpeed * ratio;
                            } else {
                                targetScrollSpeed = 0;
                            }
                        } else {
                            targetScrollSpeed = 0;
                        }

                        currentScrollSpeed += (targetScrollSpeed - currentScrollSpeed) * 0.05;

                        if (Math.abs(currentScrollSpeed) > 0.01) {
                            trackPos += currentScrollSpeed;
                            const scrollWidth = navItems.scrollWidth;
                            const oneSetWidth = scrollWidth / 3;
                            
                            if (trackPos >= oneSetWidth) {
                                trackPos = trackPos % oneSetWidth;
                            } else if (trackPos < 0) {
                                trackPos = oneSetWidth + (trackPos % oneSetWidth);
                            }
                            
                            navItems.style.transform = `translateX(-${trackPos}px)`;
                        }

                        requestAnimationFrame(navLoop);
                    }
                    navLoop();
                }
            }"""

# Fix contact.html
contact_path = '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/contact.html'
with open(contact_path, 'r', encoding='utf-8') as f:
    contact_content = f.read()

# Replace the nav carousel part
# Let's find: // Nav carousel up to prevBtn.addEventListener... nextBtn.addEventListener...
# The target to replace:
target_regex = r'\s*// Nav carousel.*prevBtn\.addEventListener\(\'click\', \(\) => scroll\(-1\)\);\s*\n\s*nextBtn\.addEventListener\(\'click\', \(\) => scroll\(1\)\);\s*\n\s*\}\);\s*\n'
contact_content = re.sub(target_regex, '\n' + hover_js + '\n', contact_content, flags=re.DOTALL)

with open(contact_path, 'w', encoding='utf-8') as f:
    f.write(contact_content)
print("Updated contact.html carousel JS.")


# Fix privacy policies
mobile_menu_js = """            // Mobile Menu Toggle
            const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
            const nav = document.querySelector('nav');
            if (mobileMenuBtn && nav) {
                mobileMenuBtn.addEventListener('click', () => {
                    nav.classList.toggle('active');
                    const itemsContainers = document.querySelectorAll('.nav-items-container, .nav-carousel, .nav-carousel-container');
                    itemsContainers.forEach(el => {
                        if (nav.classList.contains('active')) {
                            el.style.display = 'flex';
                        } else {
                            el.style.display = '';
                        }
                    });
                });
            }"""

script_block = f"""    <script>
        document.addEventListener('DOMContentLoaded', function () {{
{mobile_menu_js}
{hover_js}
        }});
    </script>
"""

policies = [
    '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/soundulator-privacy-policy.html',
    '/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/liewright-privacy-policy.html'
]

for p in policies:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script>' not in content:
        # Insert script block right before HubSpot script loader if it exists, otherwise before </body>
        if '<!-- Start of HubSpot Embed Code -->' in content:
            content = content.replace('<!-- Start of HubSpot Embed Code -->', script_block + '<!-- Start of HubSpot Embed Code -->')
        else:
            content = content.replace('</body>', script_block + '</body>')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added script to {os.path.basename(p)}")
    else:
        print(f"Script already exists in {os.path.basename(p)}")
