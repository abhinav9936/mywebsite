
<?php
// initializing variables
$username = "";
$email    = "";
$errors = array(); 
$errors2 = array();

// connect to the database
$db = mysqli_connect('localhost', 'root', 'abhinav9936', 'events');

// REGISTER USER
if (isset($_POST['register'])) {
  // receive all input values from the form
  $username = mysqli_real_escape_string($db, $_POST['username']);
  $email = mysqli_real_escape_string($db, $_POST['email']);
  $password1 = mysqli_real_escape_string($db, $_POST['password1']);
  $password2 = mysqli_real_escape_string($db, $_POST['password2']);

  // form validation: ensure that the form is correctly filled ...
  // by adding (array_push()) corresponding error unto $errors array
  if (empty($username)) { array_push($errors, "Username is required"); }
  if (empty($email)) { array_push($errors, "Email is required"); }
  if (empty($password1)) { array_push($errors, "Password is required"); }
  if ($password1 != $password2) {
	array_push($errors, "The two passwords do not match");
  }

  

  // Finally, register user if there are no errors in the form
  if (count($errors) == 0) {
  	$password = md5($password1);//encrypt the password before saving in the database

  	$query = "INSERT INTO users(Username, Email, Password) 
  			  VALUES('$username', '$email', '$password')";
      mysqli_query($db, $query);
      header('location: index.php');
  }
}
if (isset($_POST['login'])) {
    // receive all input values from the form
    $username = mysqli_real_escape_string($db, $_POST['username']);
    $email = mysqli_real_escape_string($db, $_POST['email']);
    $password = mysqli_real_escape_string($db, $_POST['password']);
  
    // form validation: ensure that the form is correctly filled ...
    // by adding (array_push()) corresponding error unto $errors array
    if (empty($username)) { array_push($errors2, "Username is required"); }
    if (empty($email)) { array_push($errors2, "Email is required"); }
    if (empty($password1)) { array_push($errors2, "Password is required"); }
  
    
  
    // Finally, register user if there are no errors in the form
    if (count($errors2) == 0) {
        $password = md5($password);//encrypt the password before saving in the database
  
        $query = "SELECT * FROM users where Username='$username' AND Email='$email' AND Password='$password'" ;
        $result = mysqli_query($db, $query);
        if (mysqli_num_rows($result) ==1 ){
            header('location: index.php');  
        }
        else{
            array_push($errors,"wrong username/password combination");
            header('location: signin.php');
        }
        
    }
  }

?>