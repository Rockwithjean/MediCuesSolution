import os
import re

new_footer = """        <!-- Footer Start -->
        <div class="container-fluid footer py-5 wow fadeIn" data-wow-delay="0.2s">
            <div class="container py-5">
                <div class="row g-5">
                    <div class="col-md-6 col-lg-4">
                        <div class="footer-item">
                            <h3 class="text-white mb-4"><i class="fas fa-heartbeat text-primary me-3"></i>Medi Cues</h3>
                            <p class="mb-4">Trusted supplier of medical equipment, accessories, consumables, and clinical services across East Africa.</p>
                            <div class="d-flex align-items-center">
                                <a class="btn btn-secondary btn-md-square rounded-circle me-3" href="#"><i class="fab fa-facebook-f"></i></a>
                                <a class="btn btn-secondary btn-md-square rounded-circle me-3" href="#"><i class="fab fa-twitter"></i></a>
                                <a class="btn btn-secondary btn-md-square rounded-circle me-3" href="#"><i class="fab fa-instagram"></i></a>
                                <a class="btn btn-secondary btn-md-square rounded-circle me-0" href="#"><i class="fab fa-linkedin-in"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4">
                        <div class="footer-item d-flex flex-column">
                            <h4 class="text-white mb-4">Quick Links</h4>
                            <a href="about.html"><i class="fas fa-angle-right me-2"></i> About Us</a>
                            <a href="service.html"><i class="fas fa-angle-right me-2"></i> Our Services</a>
                            <a href="product.html"><i class="fas fa-angle-right me-2"></i> Our Products</a>
                            <a href="contact.html"><i class="fas fa-angle-right me-2"></i> Contact Us</a>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4">
                        <div class="footer-item d-flex flex-column">
                            <h4 class="text-white mb-4">Contact Info</h4>
                            <a href="#"><i class="fa fa-map-marker-alt me-2"></i> Kilimanjaro City Arcade, Nairobi</a>
                            <a href="mailto:medicuesltd@gmail.com"><i class="fas fa-envelope me-2"></i> medicuesltd@gmail.com</a>
                            <a href="tel:+254116263263"><i class="fas fa-phone me-2"></i> +254 116 263 263</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer End -->

        <!-- Copyright Start -->
        <div class="container-fluid copyright py-4">
            <div class="container">
                <div class="row g-4 align-items-center">
                    <div class="col-md-6 text-center text-md-start mb-md-0">
                        <span class="text-body"><a href="#" class="border-bottom text-white"><i class="fas fa-copyright text-light me-2"></i>Medi Cues Medical Solutions</a>, All rights reserved.</span>
                    </div>
                    <div class="col-md-6 text-center text-md-end text-body">
                        <span class="text-white">&copy; 2024 Medi Cues Solutions Limited | Nairobi, Kenya</span>
                    </div>
                </div>
            </div>
        </div>
        <!-- Copyright End -->"""

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
