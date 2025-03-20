
            document.addEventListener('DOMContentLoaded', function() {
                
                const accordionHeaders = document.querySelectorAll('.accordion-header');
                
                
                accordionHeaders.forEach(header => {
                    header.addEventListener('click', function() {
                        // Toggle active class on parent accordion
                        const accordion = this.parentElement;
                        accordion.classList.toggle('active');
                        
                        
                        const content = this.nextElementSibling;
                        content.classList.toggle('active');
                    });
                });
            });
            