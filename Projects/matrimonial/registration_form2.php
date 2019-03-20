<?php include('index2.php') ?>
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
$name2=$_SESSION['username'];




$sql = "SELECT * FROM registers WHERE Name='$name2'";
$result = $con->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        
     $email2= $row["Email"];
     $dob2=$row['Date_of_Birth'];
     $gender2=$row['Gender'];
     $iname2=$row['Institute_Name'];
     $course2=$row['Course'];
     $stream2=$row['Stream'];
     $event2=$row['Event'];
     $mobile2=$row['Mobile_No'];
     
    }
}
mysqli_close($con);
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>
        Edit Form
    </title>
    <meta charset="utf-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
    <link rel="stylesheet" type="text/css" href=https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    
<script type="text/javascript">
    function func_course(){
        var element=document.getElementById('course');
        var val = element.options[element.selectedIndex].value;
        if(val=='others')
            document.getElementById('box1').style.display='block';
        else  
            document.getElementById('box1').style.display='none';
    }
    function func_stream(){
        var element=document.getElementById('stream');
        var val = element.options[element.selectedIndex].value;
        if(val=='others2')
            document.getElementById('box2').style.display='block';
        else  
            document.getElementById('box2').style.display='none';
    }
    function validation(){
        var s_mobile=document.getElementById('mobile').value;
        var s_email=document.getElementById('email').value;
        if (s_mobile == "") {
                document.getElementById('mobile').focus();
                document.getElementById('error_no').innerHTML = "**Please fill the valid number";
                return false;
            }
            else if (isNaN(Number(s_mobile)) ){
                document.getElementById('mobile').focus();
                document.getElementById('error_no').innerHTML = "**Characters not allowed";
                return false;
            }
            else if (s_mobile.length != 10) {
                document.getElementById('mobile').focus();
                document.getElementById('error_no').innerHTML = "**Not a Valid Number";
                return false;
            }
            else{
                document.getElementById('error_no').innerHTML = "";
            }
        if (s_email == "") {
                document.getElementById('email').focus();
                document.getElementById('error_email').innerHTML = "**Please fill the valid email-address";
                return false;
            }
        else{   
            var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if(s_email.value.match(mailformat))
        {
            document.getElementById('error_email').innerHTML = "";
        }
        else
        {
            document.getElementById('error_email').innerHTML = "**Not a valid email address.";
            }
    }
    }

</script>
    <style>
        * {
            margin: 10px;
            padding: 0;
        }
        body {
            background-image: url(background.jpg);
            background-repeat: no-repeat;
            background-size: cover;
        }
        #formstyle {
            background-color: powderblue;
            min-height: 700px;
            padding: 5px 40px 40px 40px;
            opacity : 0.8;
        }
    </style>

   
</head>



<body>
<div id="nav">
        <form action=edit.php method="POST" onsubmit="return validation();" id="formstyle" name="formstyle">
            Name :<input type="text" placeholder="Participant Name" id="name" name="name" value="<?php echo $name2 ?>">
            Email:<input type="email" placeholder="Email ID" id="email" name="email" value="<?php echo $email2 ?>"><span id="error_email" class="text-danger font-weight-bold"></span><br>
            Date of Birth: <input type="date" id="dob" name="dob" value="<?php echo $dob2 ?>"><br>
            Gender :<input type="radio" name="gender" value="male"> Male
                   :<input type="radio" name="gender" value="female"> Female
                   :<input type="radio" name="gender" value="others" > Others &nbsp; &nbsp; &nbsp;<br>
            Institute Name : <input type="text" placeholder="Institute Name" id="iname" name="iname" value="<?php echo $iname2 ?>"><br>
            Mobile Number : <input type="text" placeholder="Enter your number" id="mobile" name="mobile" value="<?php echo $mobile2 ?>"><span id="error_no" class="text-danger font-weight-bold"></span><br>

            Course : <select id="course" name="course" onchange='return func_course(); value="<?php echo $course2 ?>"'> 
                        <option value="" selected disabled hidden>Choose here</option>
                        <option value="science">Engineering Science </option>
                        <option value="arts">Arts </option>
                        <option value="commerce">Commerce </option>
                        <option value="management">Management </option>
                        <option value="others">Others </option>
                    </select>
                    <input type="text" id="box1" name="box1" style='display:none;'><br><br><br>
                
            Stream : <select id="stream" name="stream" onchange='return func_stream(); value="<?php echo $stream2 ?>"'>
                        <option value="" selected disabled hidden>Choose here</option> 
                        <option value="BE"> BE </option>
                        <option value="BTech">BTech </option>
                        <option value="Bsc">Bsc </option>
                        <option value="BCOM">BCOM </option>
                        <option value="BA">BA </option>
                        <option value="BBA">BBA </option>
                        <option value="BCA">BCA </option>
                        <option value="others2">Others </option>
                    </select><input type="text" id="box2" name="box2" style='display:none;'><br><br><br>
            Events :  <input type="checkbox" name="event" value="Cultural">Cultural
                      <input type="checkbox" name="event" value="Academics">Academics<br>
                      <input type="checkbox" name="event" value="IT">IT
                      <input type="checkbox" name="event" value="Sports">Sports<br>
                      <input type="checkbox" name="event" value="Academics">Academics
                      <input type="checkbox" name="event" value="Seminars">Seminars<br>
            Others :  <input type="text" name="other_events" >
            <input type="submit" value="Submit">
            <p>
                <?php echo "<b>"."Selected Choices"."</b>"."<br>";
                      echo "Gender:-".$gender2;
                      echo "<br>";
                      echo "Course:-".$course2;
                      echo "<br>";
                      echo "Stream:-".$stream2;
                      echo "<br>";
                      echo "Event:-".$event2; ?>
            </p>



                        
                

        </form>

    </div>
    </body>
</html>