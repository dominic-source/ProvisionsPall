function validateForm(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;

    var errorElement = document.getElementById('error');

    // validation to ensure passwords match
    if (password !== confirmPassword) {
        errorElement.textContent = 'Passwords do not match';
        return;
    }

    else {
        errorElement.textContent = '';
    

    // If the validation passes, form can be submitted to the server
    // this logs the values to the console (not the server yet)
    console.log('Username:', username);
    console.log('Email:', email);
    console.log('Password:', password);

    console.log('Form submitted successfully!');
    }
    // document.getElementById('registrationForm').submit(); can be used to submit form to server using AJAX
}