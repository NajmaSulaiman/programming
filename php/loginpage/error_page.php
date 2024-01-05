<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        /* Add your styles here if needed */
        body {
            /* Use a linear gradient for the background */
            background-color:#735B6F;
            background: linear-gradient(to bottom,   black 100%);
            color: white; /* Set text color to white for better visibility */
            height: 100vh; /* Ensure full viewport height */
            margin: 0; /* Remove default body margin */
            display: flex;
            flex-direction: column;
            justify-content: center;
            font-family: "Trirong", serif;
            align-items: center;
        }

        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        #chatbox {
            height: 200px;
            width: 400px;
            overflow-y: auto;
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 10px;
            background-color: white; /* Set chatbox background color to white */
            color: black; /* Set font color to black */
        }
        #user-input {
            width: 80%;
            padding: 8px;
            margin-right: 5px;
        }
        #send-button {
            padding: 8px;
            border: 1px solid #32e4cd;
            background-color: #800000;
            color: #fff;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error Page</title>
</head>
<body>

    <h2>Login Failed</h2>
    <p>The entered username or password is incorrect.</p>

    <a href="login_page.php">Back to Login</a>

</body>
</html>
