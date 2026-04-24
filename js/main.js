(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);
    
    
    // Initiate the wowjs
    new WOW().init();


    // Navbar Scroll Effect
    var lastScrollTop = 0;
    var delta = 5;
    $(window).scroll(function () {
        var st = $(this).scrollTop();
        
        // Handle background change
        if (st > 45) {
            $('.navbar').addClass('scrolled shadow-sm');
        } else {
            $('.navbar').removeClass('scrolled shadow-sm');
        }

        // Handle Hide/Show on Scroll Up
        if (Math.abs(lastScrollTop - st) <= delta) return;

        // Handle Hide on Scroll (Both Directions)
        if (st > 100) {
            $('.navbar').addClass('nav-up');
        } else {
            $('.navbar').removeClass('nav-up');
        }
        
        // Handle Back to Top Button
        if (st > 300) {
            $('.back-to-top').addClass('show');
        } else {
            $('.back-to-top').removeClass('show');
        }
        
        lastScrollTop = st;
    });

    // Back to Top Click
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 800, 'easeInOutExpo');
        return false;
    });

    // Side Menu Logic
    window.toggleMenu = function() {
        const isOpen = $('#sideMenu').hasClass('open');
        isOpen ? closeMenu() : openMenu();
    }

    window.openMenu = function() {
        $('#sideMenu').addClass('open');
        $('#overlay').addClass('show');
        $('#menuBtn').addClass('open');
        $('body').css('overflow', 'hidden');
    }

    window.closeMenu = function() {
        $('#sideMenu').removeClass('open');
        $('#overlay').removeClass('show');
        $('#menuBtn').removeClass('open');
        $('body').css('overflow', '');
    }

    // Close on Escape
    $(document).keydown(function(e) {
        if (e.key === 'Escape') closeMenu();
    });


    // testimonial carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="fa fa-angle-right"></i>',
            '<i class="fa fa-angle-left"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:1
            },
            992:{
                items:2
            },
            1200:{
                items:2
            }
        }
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 5,
        time: 2000
    });





})(jQuery);

