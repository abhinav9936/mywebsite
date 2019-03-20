<?php

$con=mysqli_connect("localhost","root","abhinav9936");
if(!$con)
{
  echo "not connected to server";
}
if(!mysqli_select_db($con,'events'))
{
  echo "database connection failed";
}
$name=$_POST['name'];
echo $name."<br>";
$email=$_POST['email'];
echo $email."<br>";
$dob=$_POST['dob'];
echo $dob."<br>";
$gender=$_POST['gender'];
echo $gender."<br>";
$iname=$_POST['iname'];
echo $iname."<br>";
$course=$_POST['course'];
echo $course."<br>";
$stream=$_POST['stream'];
echo $stream."<br>";
$event=$_POST['event'];
echo $event."<br>";
$mobile=$_POST['mobile'];
echo $mobile."<br>";
$today = date("Y-m-d");
$diff = date_diff(date_create($dob), date_create($today));
echo 'Age is '.$diff->format('%y');
$age = $diff->format('%y');
$sql1= "INSERT INTO registers(Name,Email,Date_of_Birth,Age,Gender,Institute_Name,Mobile_No,Course,Stream,Event) VALUES ('$name','$email','$dob','$age','$gender','$iname','$mobile','$course','$stream','$event')";
if(!mysqli_query($con,$sql1))
{
    echo 'Not Inserted';
}
else
{
    echo 'Inserted';
}

header("refresh:5; url=register.php");
?>
