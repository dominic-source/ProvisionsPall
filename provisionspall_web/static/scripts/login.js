function login(event) {
    // This prevents form from submitting in the traditional way
    event.preventDefault();

    // This gets the input values inserted by the user
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // This performs the client-side validation
    if (username && password) {
        // Redirect to the dashboard page
        window.location.href = '/dashboard.html';
    } else {
        // This provides eeror message to the user
        alert('Please enter both username and password.');
    }

    document.getElementById('username').addEventListener('keypress', function (event) {
        var keyCode = event.keyCode;
        // This allows only letters (A-Z and a-z)
        if (!((keyCode >= 65 && keyCode <= 90) || (keyCode >= 97 && keyCode <= 122))) {
            event.preventDefault();
        }
    });

    document.getElementById('username').addEventListener('keypress', function (event) {
        var keyCode = event.keyCode;
        // Allow only letters (A-Z and a-z) and numbers (0-9)
        if (!((keyCode >= 65 && keyCode <= 90) || (keyCode >= 97 && keyCode <= 122) || (keyCode >= 48 && keyCode <= 57))) {
            event.preventDefault();
        }
    });

    function setCookie(name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }

    // This function is to get a cookie by name once user logins in
    function getCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    // this function handles login
    function login(event) {
        event.preventDefault();

        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;
        var remember = document.getElementById('remember').checked;

        // Performs authentication logic here (replace with your server-side authentication)

        if (remember) {
            // Sets the username in a cookie that expires in 7 days (expiration time can be changed)
            setCookie('rememberedUsername', username, 7);
        } else {
            // this removes the cookie if "Remember Me" is not checked
            setCookie('rememberedUsername', '', -1);
        }

        // this redirects or performs other actions based on successful authentication
        console.log('Authenticated. Redirect to the dashboard or perform other actions.');
    }

    // Retrieve remembered username on page load
    document.addEventListener('DOMContentLoaded', function () {
        var rememberedUsername = getCookie('rememberedUsername');
        if (rememberedUsername) {
            document.getElementById('username').value = rememberedUsername;
            document.getElementById('remember').checked = true;
        }
    });
}