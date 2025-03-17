
            document.addEventListener('DOMContentLoaded', function() {
                // Get all accordion headers
                const accordionHeaders = document.querySelectorAll('.accordion-header');
                
                // Add click event to each header
                accordionHeaders.forEach(header => {
                    header.addEventListener('click', function() {
                        // Toggle active class on parent accordion
                        const accordion = this.parentElement;
                        accordion.classList.toggle('active');
                        
                        // Toggle active class on content
                        const content = this.nextElementSibling;
                        content.classList.toggle('active');
                    });
                });
            });
            