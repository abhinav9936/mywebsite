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
$name2=$_POST['name2'];
$sql= "INSERT INTO test(Name,Name2) VALUES ('$name','$name2')";
if(!mysqli_query($con,$sql))
{
    echo 'Not Inserted';
}
else
{
    echo 'Inserted';
}

header("refresh:200; url=index.html");
?>
