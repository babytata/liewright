<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Subscribe - Liewright</title>
    <style>
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: #111;
            color: #bdccd4;
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
            color: #bdccd4;
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
            color: #bdccd4;
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
        /* Mailchimp Form Styles */
        #mc_embed_signup {
            background: #1c1c1c;
            clear: left;
            font: 14px Helvetica, Arial, sans-serif;
            width: 100%;
            max-width: 600px;
            margin: 2rem auto;
            padding: 20px;
            border-radius: 5px;
            border: 1px solid #333;
        }
        #mc_embed_signup h2 {
            color: #bbbdbf;
            text-align: center;
        }
        #mc_embed_signup .mc-field-group {
            margin-bottom: 15px;
        }
        #mc_embed_signup .mc-field-group label {
            color: #ccc;
            display: block;
            margin-bottom: 5px;
        }
        #mc_embed_signup .mc-field-group input {
            width: 100%;
            padding: 10px;
            border-radius: 3px;
            border: 1px solid #555;
            background: #333;
            color: #eee;
        }
        #mc_embed_signup .button {
            width: 100%;
            padding: 12px;
            background: #bbbdbf;
            color: #111;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        #mc_embed_signup .button:hover {
            background: #ccc;
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
                        <li><a href="apps.php">Apps</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </div>
                <button class="scroll-btn next" aria-label="Next">></button>
            </div>
        </nav>
    </header>

    <div class="container">
        <h1>Subscribe to Our Newsletter</h1>
        <p>Get the latest news, updates, and special offers from Liewright directly to your inbox.</p>
        
        <div id="mc_embed_signup">
            <form action="https://etsy.us21.list-manage.com/subscribe/post?u=1b5651f6ad958d5e053a39900&amp;id=a595fd551d&amp;f_id=00318ce6f0" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
                <div id="mc_embed_signup_scroll">
                    <h2>Subscribe</h2>
                    <div class="indicates-required"><span class="asterisk">*</span> indicates required</div>
                    <div class="mc-field-group">
                        <label for="mce-EMAIL">Email Address <span class="asterisk">*</span></label>
                        <input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
                    </div>
                    <div class="mc-field-group">
                        <label for="mce-FNAME">First Name </label>
                        <input type="text" value="" name="FNAME" class="" id="mce-FNAME">
                    </div>
                    <div class="mc-field-group">
                        <label for="mce-LNAME">Last Name </label>
                        <input type="text" value="" name="LNAME" class="" id="mce-LNAME">
                    </div>
                    <div id="mce-responses" class="clear">
                        <div class="response" id="mce-error-response" style="display:none"></div>
                        <div class="response" id="mce-success-response" style="display:none"></div>
                    </div>
                    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_1b5651f6ad958d5e053a39900_a595fd551d" tabindex="-1" value=""></div>
                    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
                </div>
            </form>
        </div>
        <script type='text/javascript' src='//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js'></script><script type='text/javascript'>(function($) {window.fnames = new Array(); window.ftypes = new Array();fnames[0]='EMAIL';ftypes[0]='email';fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';}(jQuery));var $mcj = jQuery.noConflict(true);</script>
        
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
                <a href="subscribe.php">Subscribe</a>
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