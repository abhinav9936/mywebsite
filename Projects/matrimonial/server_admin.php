<?php

// initializing variables
$admin = "admin";
$email    = "admin@gmail.com";
$password = "";
$errors2 = array();
// connect to the database
$db = mysqli_connect('localhost', 'root', 'abhinav9936', 'events');
if (isset($_POST['admin_login'])) {
    $username = mysqli_real_escape_string($db, $_POST['username']);
    $password = mysqli_real_escape_string($db, $_POST['password']);
  
    if (empty($username)) {
        array_push($errors2, "Username is required");
    }
    if (empty($password)) {
        array_push($errors2, "Password is required");
    }
  
    if (count($errors) == 0) {
        $password = md5($password);
        $query = "SELECT * FROM users WHERE Username='$admin' AND Password='$password'";
        $results = mysqli_query($db, $query);
        if (mysqli_num_rows($results) == 1) {
          header('location: index_admin.php');
        }else {
            array_push($errors, "Wrong username/password combination");
        }
    }
  }
  
  ?>