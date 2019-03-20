<?php include('server.php'); ?>
<!DOCTYPE html>
<html>
    <head>
        <title>Login Page</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
<body>
    <div class="header">
        <h2>Register </h2>
    </div>
    <form method="POST" action="login.php">
        <!-- display validation errors here -->
        <?php include('errors.php'); ?>
        <div class="input-group">
            <label>Username</label>
            <input type="text" id="username" name="username" value="<?php echo $username; ?>">
        </div>
        <div class="input-group">
            <label>Email</label>
            <input type="text" id="email" name="email" value="<?php echo $email; ?>">
        </div>
        <div class="input-group">
            <label>Password</label>
            <input type="password" id="password1" name="password1">
        </div>
        <div class="input-group">
            <label>Confirm Password</label>
            <input type="password" name="password2">
        </div>
        <div class="input-group">
            <button type="submit" id="register" name="register" class="btn">Register</button>
        </div>
        <p>
            Already registered? <a href="signin.php">Sign in</a>
        </p>
    </form>      
</body>
</html>