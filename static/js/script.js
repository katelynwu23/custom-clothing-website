// ========================================
// Mobile navigation toggle
// ========================================
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
}

// ========================================
// Custom order form (order.html only)
// No backend yet — this just shows a
// confirmation message instead of submitting.
// ========================================
const orderForm = document.getElementById('orderForm');
const formMessage = document.getElementById('formMessage');

if (orderForm && formMessage) {
  orderForm.addEventListener('submit', (event) => {
    event.preventDefault();

    formMessage.textContent = 'Thanks! Your custom order request has been noted (this form isn\'t connected to anything yet).';
    formMessage.classList.add('visible');

    orderForm.reset();
  });
}
