document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // In a real application, this would be replaced with backend authentication logic
    let userId = document.getElementById('userId').value;
    let password = document.getElementById('password').value;

    // Simulate successful login for demonstration
    if (userId === 'vendor123' && password === 'password') {
        window.location.href = 'punchin.html'; // Redirect to punch-in page
    } else {
        alert('Invalid credentials. Please try again.');
    }
});
