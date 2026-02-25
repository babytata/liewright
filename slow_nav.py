import os
import re

directory = "/Users/babytatalie/Desktop/BAA (Building an App)/liewright_php/"

files_to_check = [f for f in os.listdir(directory) if f.endswith('.html')]

# Regular expression to match the entire existing nav carousel script block
regex_js_script = re.compile(
    r"\/\/\s*---\s*Nav Carousel Logic\s*---.*?(?=\/\/ --- Hero Grid Logic ---|<\/script>)", 
    re.DOTALL
)

new_js = """// --- Nav Carousel Logic ---
            const carousel = document.querySelector('.nav-carousel');
            if (carousel) {
                const navItems = carousel.querySelector('.nav-items');
                if (navItems) {
                    const items = navItems.querySelectorAll('li');
                    items.forEach(item => navItems.appendChild(item.cloneNode(true)));
                    items.forEach(item => navItems.appendChild(item.cloneNode(true)));

                    let trackPos = 0;
                    let currentScrollSpeed = 0;
                    let targetScrollSpeed = 0;
                    let isNavMouseOver = false;
                    let mouseX = 0;

                    carousel.addEventListener('mouseenter', () => isNavMouseOver = true);
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
                            
                            // ⬇️ Reduced from 8 to 3 to make scrolling slower and less erratic
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

                        // ⬇️ Reduced multiplier from 0.1 to 0.05 for smoother ease-in/ease-out acceleration
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
            }
            """

files_modified = []

for filename in files_to_check:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Replace JS
    content = regex_js_script.sub(new_js, content)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_modified.append(filename)

print("Modified files:", files_modified)
