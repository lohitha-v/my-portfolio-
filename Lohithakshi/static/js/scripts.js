// Smooth scroll for dropdown menu links
        document.querySelectorAll('.dropdown-content a').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').slice(1);
                document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });
            });
        });