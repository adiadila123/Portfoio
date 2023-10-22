document.addEventListener("DOMContentLoaded", function() {
    // Reference to the parallax background element
    var parallaxBackground = document.querySelector('.parallax-background');

    if (parallaxBackground) { // Ensure the element exists
        document.addEventListener("scroll", function() {
            var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            var parallaxSpeed = 0.5; // Adjust this value to control the parallax speed
            var offset = scrollTop * parallaxSpeed;

            parallaxBackground.style.transform = `translateY(-${offset}px)`;
        });
    }
});

// You can add other JavaScript functionalities or scripts below
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
