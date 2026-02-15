<?php
// Initialize variables
$name = $email = $message = "";
$name_err = $email_err = $message_err = "";
$form_submitted = false;
$success = false;

// Process form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $form_submitted = true;

    // Validate name
    if (empty(trim($_POST["name"]))) {
        $name_err = "Please enter your name.";
    } else {
        $name = trim($_POST["name"]);
    }

    // Validate email
    if (empty(trim($_POST["email"]))) {
        $email_err = "Please enter your email.";
    } elseif (!filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL)) {
        $email_err = "Invalid email format.";
    } else {
        $email = trim($_POST["email"]);
    }

    // Validate message
    if (empty(trim($_POST["message"]))) {
        $message_err = "Please enter a message.";
    } else {
        $message = trim($_POST["message"]);
    }

    // Check for errors before sending email
    if (empty($name_err) && empty($email_err) && empty($message_err)) {
        // Recipient email address
        $to = "privacy@liewright.com";
        // Email subject
        $subject = "Contact Form Submission from " . $name;
        // Email body
        $body = "You have received a new message from your website contact form.\n\n";
        $body .= "Here are the details:\n";
        $body .= "Name: $name\n";
        $body .= "Email: $email\n";
        $body .= "Message:\n$message\n";
        // Email headers
        $headers = "From: " . $email;

        // Send email
        if (mail($to, $subject, $body, $headers)) {
            $success = true;
        } else {
            // Optional: Handle mail server errors
            // For now, we'll just assume it failed if mail() returns false
            $success = false;
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Contact - Liewright</title>
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
        nav a.logo img {
            height: 20px !important;
            vertical-align: middle;
        }
        nav ul li a.logo {
            padding: 0;
        }
        nav ul li a.logo:hover {
            background-color: transparent;
        }
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
            width: 50px;
            z-index: 2;
            pointer-events: none;
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
            transition: transform 0.5s ease;
        }
        nav ul.nav-items li {
            margin: 0 15px;
            flex-shrink: 0;
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
        .contact-form {
            background: #1c1c1c;
            padding: 30px;
            border-radius: 5px;
            border: 1px solid #333;
            max-width: 600px;
            margin: 2rem auto;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            color: #ccc;
            margin-bottom: 5px;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border-radius: 3px;
            border: 1px solid #555;
            background: #333;
            color: #eee;
            box-sizing: border-box; /* Ensures padding doesn't affect width */
        }
        .form-group .error {
            color: #ff6b6b;
            font-size: 0.9rem;
            margin-top: 5px;
        }
        .form-submit {
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
        .form-submit:hover {
            background: #ccc;
        }
        .form-message {
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
            text-align: center;
        }
        .form-message.success {
            background-color: #28a745;
            color: #fff;
        }
        .form-message.error {
            background-color: #dc3545;
            color: #fff;
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
        .footer-logo img {
            height: 25px !important;
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
                        <li><a href="apps.php">Apps</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="contact.php">Contact</a></li>
                    </ul>
                </div>
                <button class="scroll-btn next" aria-label="Next">></button>
            </div>
        </nav>
    </header>

    <div class="container">
        <h1>Contact Us</h1>
        <p>Have a question, a project idea, or just want to say hello? Drop us a line below.</p>

        <div class="contact-form">
            <?php if ($form_submitted): ?>
                <?php if ($success): ?>
                    <div class="form-message success">
                        Thank you for your message! We'll get back to you shortly.
                    </div>
                <?php else: ?>
                    <div class="form-message error">
                        Oops! Something went wrong. Please correct the errors and try again.
                    </div>
                <?php endif; ?>
            <?php endif; ?>

            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name); ?>">
                    <span class="error"><?php echo $name_err; ?></span>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email); ?>">
                    <span class="error"><?php echo $email_err; ?></span>
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" rows="6"><?php echo htmlspecialchars($message); ?></textarea>
                    <span class="error"><?php echo $message_err; ?></span>
                </div>
                <input type="submit" class="form-submit" value="Send Message">
            </form>
        </div>
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
                <a href="contact.php">Contact</a>
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
        // Reusing the same carousel script from other pages
        document.addEventListener('DOMContentLoaded', function() {
            const carousels = document.querySelectorAll('.nav-carousel');
            carousels.forEach(carousel => {
                const container = carousel.querySelector('.nav-items-container');
                const navItems = carousel.querySelector('.nav-items');
                const prevBtn = carousel.querySelector('.prev');
                const nextBtn = carousel.querySelector('.next');

                if (!navItems || !prevBtn || !nextBtn || !container) return;

                const items = Array.from(navItems.children);
                if (items.length === 0) return;

                // Clone items for infinite scroll
                items.forEach(item => navItems.appendChild(item.cloneNode(true)));
                items.forEach(item => navItems.appendChild(item.cloneNode(true)));

                let scrollAmount = 0;
                const scrollStep = items[1] ? items[1].offsetWidth : 150; // Use a fallback width

                function scroll(direction) {
                    const scrollWidth = navItems.scrollWidth;
                    const containerWidth = container.offsetWidth;
                    const originalScrollWidth = scrollWidth / 3;

                    scrollAmount += direction * scrollStep;

                    if (direction === -1 && scrollAmount < 0) {
                        scrollAmount = originalScrollWidth - scrollStep;
                        navItems.style.transition = 'none';
                        navItems.style.transform = `translateX(-${scrollAmount}px)`;
                        navItems.offsetHeight; // Force reflow
                        navItems.style.transition = 'transform 0.5s ease';
                    } else if (direction === 1 && scrollAmount >= originalScrollWidth) {
                        scrollAmount = scrollAmount % originalScrollWidth;
                        navItems.style.transition = 'none';
                        navItems.style.transform = `translateX(-${scrollAmount}px)`;
                        navItems.offsetHeight; // Force reflow
                        navItems.style.transition = 'transform 0.5s ease';
                    }
                    
                    navItems.style.transform = `translateX(-${scrollAmount}px)`;
                }

                prevBtn.addEventListener('click', () => scroll(-1));
                nextBtn.addEventListener('click', () => scroll(1));
            });
        });
    </script>
</body>
</html>