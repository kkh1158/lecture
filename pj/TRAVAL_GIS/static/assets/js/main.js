/* ===================================================================
    Author          : ModinaTheme
    Template Name   : Listico - Listing & Directory HTML Template
    Version         : 2.0
* ================================================================= */

(function($) {
    "use strict";

    $(document).on('ready', function() {


    // Preloading
    $(window).on('load', function() {
        // Animate loader off screen
        $(".loader-wrap").delay(300).fadeOut();
    });

    //# Smooth Scroll
    $('.details-nav a').on('click', function(event) {
        var $anchor = $(this);
        var headerH = '30';
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - headerH + "px"
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });

  /*==========================
       map slider init
    ============================*/
    $('.listico-slider').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '.slider-nav',
      initialSlide: 2
    });
    $('.slider-nav').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      asNavFor: '.listico-slider',
      dots: false,
      centerMode: true,
      focusOnSelect: true,
      initialSlide: 2,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });

  /*==========================
       Gallery init
    ============================*/
    $('.photo-gallery').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '.gallery_nav',
      initialSlide: 2
    });
    $('.gallery_nav').slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      asNavFor: '.photo-gallery',
      dots: false,
      centerMode: true,
      focusOnSelect: true,
      initialSlide: 2,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });


    /*==================================
     # Listico Item Carousel 
     ==================================*/
    $('.listico-item-carousel, .top-locations-carousel').owlCarousel({
        autoplay: true,
        loop: true,
        margin: 30,
        nav: false,
        dots: true,
        responsive: {
            0: {
                items: 1
            },
            700: {
                items: 2
            },
            1000: {
                items: 2
            },
            1300: {
                items: 3
            }
        }
    });

    /*==================================
     # Listico testimonials Carousel 
     ==================================*/
    $('.testimonial-carousel').owlCarousel({
        autoplay: true,
        loop: true,
        margin: 30,
        nav: false,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            700: {
                items: 2
            },
            1000: {
                items: 2
            },
            1300: {
                items: 3
            }
        }
    });

    /*==================================
     # meanmenu active - mobile menu 
     ==================================*/
    $('#responsive-menu').meanmenu({
        meanMenuContainer: '.responsive-menu',
        meanScreenWidth: "992"
    });


    /* =============================================
        # Magnific popup init
     ===============================================*/
    $(".popup-link").magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        },
        // other options
    });

    $(".popup-gallery").magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        },
        // other options
    });

    $(".popup-video, .popup-vimeo, .popup-gmaps").magnificPopup({
        type: "iframe",
        mainClass: "mfp-fade",
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

    var wow = new WOW(
        {
            mobile: false,
        }
    )
    wow.init();

    $(".range-slider").ionRangeSlider();


    $(".rating").rate();
    var options = {
        max_value: 5,
        step_size: 1,
    }
    $(".rating").rate(options);


   /*==========================
       Scroll To Up init
    ============================*/
    $.scrollUp({
      scrollName: 'scrollUp', // Element ID
      topDistance: '1110', // Distance from top before showing element (px)
      topSpeed: 2000, // Speed back to top (ms)
      animation: 'slide', // Fade, slide, none
      animationInSpeed: 300, // Animation in speed (ms)
      animationOutSpeed: 300, // Animation out speed (ms)
      scrollText: '<i class="fas fa-angle-up"></i>', // Text for element
      activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
    });

    
    }); // end document ready function
})(jQuery); // End jQuery

