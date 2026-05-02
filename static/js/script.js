// Contact Form Handler
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const successMessage = document.getElementById('successMessage');

    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            // Collect form data
            const formData = new FormData(contactForm);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                message: formData.get('message')
            };

            try {
                // Send data to backend
                const response = await fetch('{{ url_for("submit_contact") }}', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    // Show success message
                    successMessage.style.display = 'block';
                    contactForm.reset();
                    
                    // Hide success message after 5 seconds
                    setTimeout(() => {
                        successMessage.style.display = 'none';
                    }, 5000);
                } else {
                    alert('Failed to send message. Please try again.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Add animation to elements on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
});

// Observe service cards
document.querySelectorAll('.service-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.6s ease';
    observer.observe(card);
});

// Observe stat items
document.querySelectorAll('.stat-item').forEach(item => {
    observer.observe(item);
});
