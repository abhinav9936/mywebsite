<html>
  <body>
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
$sql1= "SELECT Name,Email,Date_of_Birth,Gender,Institute_Name,Mobile_No,Course,Stream,Event FROM  registers";
$results = mysqli_query($con, $sql1);
echo "Total Registers-".mysqli_num_rows($results);
echo '<br>';

while($row = mysqli_fetch_array($results)) { 
  echo "<br>";
  echo "<tr>"; 

  echo "<td>" . $row['Name'] ."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Email']."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Date_of_Birth']."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Gender'] ."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Institute_Name'] ."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Mobile_No'] ."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Course'] ."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Stream'] ."&nbsp&nbsp&nbsp&nbsp"."</td>";
  echo"<td>". $row['Event'] ."&nbsp&nbsp&nbsp&nbsp"."</td>";
echo "</tr>";
}
header("refresh:5; url=register.php");

?>
</body>
