<?php include('server.php'); ?>
<!DOCTYPE html>
<html>
    <head>
        <title>Login Page</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
<body>
    <div class="header">
        <h2>Login </h2>
    </div>
    <form method="POST" action="signin.php">
        <!-- display validation errors here -->
        <?php include('errors2.php'); ?>
        <div class="input-group">
            <label>Username</label>
            <input type="text" id="username" name="username">
        </div>
        <div class="input-group">
            <label>Email</label>
            <input type="text" id="email" name="email">
        </div>
        <div class="input-group">
            <label>Password</label>
            <input type="password" id="password" name="password">
        </div>
        <div class="input-group">
            <button type="submit" name="login" class="btn">Login</button>
        </div>
        <p>
            Not yet registered? <a href="login.php">Sign up</a>
        </p>
    </form>      
</body>
</html>