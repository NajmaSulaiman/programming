<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION["username"])) {
    header("Location: login_page.php");
    exit();
}

// Retrieve the username from the session
$loggedInUsername = $_SESSION["username"];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        /* Add your styles here if needed */
        body {
            /* Use a linear gradient for the background */
            background-color:#5B736B;
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
    <title>Success Page</title>
</head>
<body>

    <h2>Welcome, <?php echo $loggedInUsername; ?>!</h2>
    <p>You have successfully logged in.</p>

    <a href="logout.php">Logout</a>

</body>
</html>
