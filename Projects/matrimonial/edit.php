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
echo $name;
$email=$_POST['email'];
echo $email;
$dob=$_POST['dob'];
echo $dob;
$gender=$_POST['gender'];
echo $gender;
$iname=$_POST['iname'];
echo $iname;
$course=$_POST['course'];
echo $course;
$stream=$_POST['stream'];
echo $stream;
$event=$_POST['event'];
echo $event; /*UPDATE table_name
SET column1=value, column2=value2,...
WHERE some_column=some_value*/  
$mobile=$_POST['mobile'];
echo $mobile;
$today = date("Y-m-d");
$diff = date_diff(date_create($dob), date_create($today));
echo 'Age is '.$diff->format('%y');
$age = $diff->format('%y');
$sql1= "UPDATE registers SET Name='$name',Email='$email',Date_of_Birth='$dob',Age='$age',Gender='$gender',Institute_Name='$iname',Mobile_No='$mobile',Course='$course',Stream='$stream',Event='$event' WHERE Name='$name'";
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
