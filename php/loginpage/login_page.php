<?php
session_start();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Define the hardcoded username and password
    $correctUsername = "admin";
    $correctPassword = "admin";

    // Get user inputs
    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    // Check if the entered credentials are correct
    if ($enteredUsername == $correctUsername && $enteredPassword == $correctPassword) {
        // Successful login, redirect to success page
        $_SESSION["username"] = $enteredUsername;
        header("Location: success_page.php");
        exit();
    } else {
        // Incorrect login, redirect to error page
        header("Location: error_page.php");
        exit();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        /* Add your styles here if needed */
        body {
            /* Use a linear gradient for the background */
            background-color:#212F3C ;
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
    <title>Login Page</title>
</head>
<body>

    <h2>Login Page</h2>

    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <input type="submit" value="Login">
    </form>

</body>
</html>
