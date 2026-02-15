
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Apps - Liewright</title>
    <style>
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: #111;
            color: #eee;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background: #1c1c1c;
            padding: 1rem 20px;
            border-bottom: 2px solid #bbbdbf;
        }
        nav {
            max-width: 900px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        /* --- CHANGED RULE --- */
        nav a.logo img {
            height: 20px !important; /* Made size smaller and more specific */
            vertical-align: middle;
        }
        nav ul li a.logo {
            padding: 0;
        }
        nav ul li a.logo:hover {
            background-color: transparent;
        }

        /* Carousel Styles */
        .nav-carousel {
            display: flex;
            align-items: center;
            flex-grow: 1;
            position: relative;
            overflow: hidden;
        }
        .nav-items-container {
            overflow: hidden;
            flex-grow: 1;
            position: relative;
        }
        .nav-items-container::before,
        .nav-items-container::after {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 50px; /* Width of the fade */
            z-index: 2;
            pointer-events: none; /* Allows clicking through the fade */
        }
        .nav-items-container::before {
            left: 0;
            background: linear-gradient(to right, #1c1c1c, transparent);
        }
        .nav-items-container::after {
            right: 0;
            background: linear-gradient(to left, #1c1c1c, transparent);
        }

        nav ul.nav-items {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            transition: transform 0.5s ease; /* Smooth scrolling */
        }
        nav ul.nav-items li {
            margin: 0 15px; /* Adjust spacing */
            flex-shrink: 0; /* Prevent items from shrinking */
        }
        nav ul li a {
            color: #eee;
            text-decoration: none;
            font-weight: 600;
            padding: 5px 10px;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
            display: block;
            white-space: nowrap;
        }
        nav ul li a:hover, nav ul li a.active {
            background-color: #bbbdbf;
            color: #111;
        }

        .scroll-btn {
            background: transparent;
            border: none;
            color: #eee;
            font-size: 2rem;
            cursor: pointer;
            z-index: 3;
            padding: 0 10px;
        }
        .scroll-btn:hover {
            color: #bbbdbf;
        }
        .scroll-btn.prev {
            margin-right: 10px;
        }
        .scroll-btn.next {
            margin-left: 10px;
        }


        h1 {
            font-size: 2.8rem;
            letter-spacing: 1px;
            font-weight: 700;
            color: #bbbdbf;
            text-align: center;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
        }
        p {
            margin-top: 1rem;
            font-size: 1.15rem;
            text-align: center;
        }
        .highlight {
            color: #bbbdbf;
            font-weight: 700;
        }
        footer {
            margin-top: 3rem;
            font-size: 0.9rem;
            color: #555;
            text-align: center;
            border-top: 1px solid #333;
            padding: 40px 20px;
        }
        .footer-logo {
            text-align: center;
            margin-bottom: 30px;
        }
        /* --- CHANGED RULE --- */
        .footer-logo img {
            height: 25px !important; /* Made size smaller and added !important */
        }
        .sitemap {
            max-width: 900px;
            margin: 0 auto 30px auto;
            display: flex;
            justify-content: space-around;
            text-align: left;
            flex-wrap: wrap;
        }
        .sitemap-col {
            margin: 0 20px;
            min-width: 150px;
        }
        .sitemap-col h4 {
            color: #bbbdbf;
            font-size: 1.1rem;
            margin-bottom: 10px;
        }
        .sitemap-col a {
            color: #ccc;
            text-decoration: none;
            display: block;
            margin-bottom: 5px;
            transition: color 0.3s;
        }
        .sitemap-col a:hover {
            color: #bbbdbf;
        }
        .copyright {
            text-align: center;
            font-size: 0.9rem;
            color: #555;
            border-top: 1px solid #333;
            padding-top: 20px;
            margin-top: 20px;
        }
    </style>

</head>
<body>
 <header>
        <nav>
            <div class="nav-carousel">
                <button class="scroll-btn prev" aria-label="Previous"><</button>
                <div class="nav-items-container">
                    <ul class="nav-items">
                        <li><a href="/" class="logo"><img src="images/liewright_logo.png" alt="Liewright Logo"></a></li>
                        <li><a href="/">Home</a></li>
                        <li><a href="#">Art</a></li>
                        <li><a href="#">Apparel</a></li>
                        <li><a href="/" class="logo"><img src="images/liewright_logo.png" alt="Liewright Logo"></a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </div>
                <button class="scroll-btn next" aria-label="Next">></button>
            </div>
        </nav>
    </header>

    <div class="container">
        <h1>Apps</h1>
        <ul class="app-list">
            <li><a href="soundulator.php">Soundulator</a></li>
        </ul>
    </div>

    <footer>
        <div class="footer-logo">
            <a href="/"><img src="images/liewright_logo.png" alt="Liewright Logo"></a>
        </div>
        <div class="sitemap">
            <div class="sitemap-col">
                <h4>Liewright</h4>
                <a href="/">Home</a>
                <a href="#">About Us</a>
                <a href="#">Contact</a>
            </div>
            <div class="sitemap-col">
                <h4>Work</h4>
                <a href="#">Art</a>
                <a href="#">Apparel</a>
            </div>
            <div class="sitemap-col">
                <h4>Projects</h4>
                <a href="apps.php">Apps</a>
            </div>
            <div class="sitemap-col">
                <h4>Legal</h4>
                <a href="liewright-privacy-policy.php">Privacy Policy</a>
            </div>
        </div>
        <div class="copyright">
            © <?php echo date("Y"); ?> Liewright — All Rights Reserved.
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const carousel = document.querySelector('.nav-carousel');
            const container = carousel.querySelector('.nav-items-container');
            const navItems = carousel.querySelector('.nav-items');
            const prevBtn = carousel.querySelector('.prev');
            const nextBtn = carousel.querySelector('.next');

            // Clone items for the infinite scroll effect
            const items = navItems.querySelectorAll('li');
            items.forEach(item => {
                const clone = item.cloneNode(true);
                navItems.appendChild(clone);
            });
             // Clone again to ensure enough items to fill the container and scroll
             items.forEach(item => {
                const clone = item.cloneNode(true);
                navItems.appendChild(clone);
            });


            let scrollAmount = 0;
            // Base scroll step on a text item's width for more consistent scrolling.
            const itemWidth = items.length > 1 ? items[1].offsetWidth : 150;
            const scrollStep = itemWidth; // Scroll by one item width

            function scroll(direction) {
                const containerWidth = container.offsetWidth;
                const scrollWidth = navItems.scrollWidth;
                const maxScroll = scrollWidth - containerWidth;

                scrollAmount += direction * scrollStep;

                // Infinite scroll logic
                if (scrollAmount < 0) {
                    // If scrolling past the beginning, jump to the equivalent position in the second set of clones
                    scrollAmount = (scrollWidth / 2) - scrollStep;
                    navItems.style.transition = 'none'; // Disable transition for the jump
                    navItems.style.transform = `translateX(-${scrollAmount}px)`;
                    // Force a reflow to apply the transform immediately
                    navItems.offsetHeight;
                    // Re-enable transition for the next scroll
                    navItems.style.transition = 'transform 0.5s ease';
                } else if (scrollAmount > scrollWidth / 2) {
                     // If scrolling past the end of the first set, jump to the beginning
                    scrollAmount = scrollStep;
                    navItems.style.transition = 'none';
                    navItems.style.transform = 'translateX(0px)';
                    navItems.offsetHeight;
                    navItems.style.transition = 'transform 0.5s ease';
                }

                navItems.style.transform = `translateX(-${scrollAmount}px)`;
            }

            prevBtn.addEventListener('click', () => scroll(-1));
            nextBtn.addEventListener('click', () => scroll(1));

            // Optional: Auto-scroll
            // setInterval(() => scroll(1), 3000);
        });
    </script>
</body>
</html>