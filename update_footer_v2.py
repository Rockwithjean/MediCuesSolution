import os
import re

new_footer = """    <!-- Waves Start -->
    <div class="wave-container">
        <svg class="wave-svg wave1" viewBox="0 0 1440 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0,60 C180,100 360,20 540,60 C720,100 900,20 1080,60 C1260,100 1380,40 1440,60 L1440,120 L0,120 Z" fill="#0e2a3b"/>
        </svg>
        <svg class="wave-svg wave2" viewBox="0 0 1440 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0,70 C200,30 400,90 600,60 C800,30 1000,90 1200,55 C1320,35 1400,75 1440,65 L1440,120 L0,120 Z" fill="#0e2a3b"/>
        </svg>
        <svg class="wave-svg wave3" viewBox="0 0 1440 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0,50 C240,90 480,10 720,55 C960,95 1200,25 1440,50 L1440,120 L0,120 Z" fill="#0e2a3b"/>
        </svg>
    </div>
    <!-- Waves End -->

    <!-- Footer Start -->
    <footer class="footer-body">
        <div class="footer-grid">
            <!-- Brand -->
            <div>
                <p class="footer-brand-name">Medi Cues</p>
                <p class="footer-brand-desc">Trusted supplier of medical equipment, accessories, consumables, and clinical services across East Africa.</p>
                <div class="social-row">
                    <a href="#" class="social-btn" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" class="social-btn" title="Twitter"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="social-btn" title="Instagram"><i class="fab fa-instagram"></i></a>
                    <a href="#" class="social-btn" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </div>

            <!-- Links -->
            <div class="footer-links-wrap">
                <div>
                    <p class="footer-col-title">Services</p>
                    <ul class="footer-links">
                        <li><a href="service.html">Medical Equipment</a></li>
                        <li><a href="service.html">Hospital Furniture</a></li>
                        <li><a href="service.html">Clinical Training</a></li>
                        <li><a href="service.html">Maintenance</a></li>
                    </ul>
                </div>
                <div>
                    <p class="footer-col-title">Company</p>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="product.html">Our Products</a></li>
                        <li><a href="blog.html">News & Updates</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <hr class="footer-divider">

        <div class="footer-bottom">
            <span class="footer-copy">© 2024 Medi Cues Solutions Limited. All rights reserved.</span>
            <div class="footer-badge">
                <div class="pulse-dot"></div>
                All systems operational
            </div>
        </div>
    </footer>
    <!-- Footer End -->"""

# Pattern to find old footer + copyright blocks
pattern = re.compile(r'[ \t]*<!-- Footer Start -->.*?<!-- Copyright End -->', re.DOTALL)

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, count = pattern.subn(new_footer, content)
        
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            # Try a broader pattern if the first one fails
            # Maybe the Footer End and Copyright Start are separated by more whitespace
            pattern2 = re.compile(r'[ \t]*<!-- Footer Start -->.*?<!-- Footer End -->.*?<!-- Copyright Start -->.*?<!-- Copyright End -->', re.DOTALL)
            new_content, count = pattern2.subn(new_footer, content)
            if count > 0:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file} (pattern2)")
            else:
                # One last try: just replace the Footer and then the Copyright separately if needed
                pass

print("Done.")
