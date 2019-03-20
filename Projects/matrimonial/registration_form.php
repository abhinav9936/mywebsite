<!DOCTYPE html>
<html lang="en">

<head>
    <title>
        Registration Form
    </title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href=https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
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
        #form {
            background-color: powderblue;
            min-height: 700px;
            padding: 5px 40px 40px 40px;
            opacity : 0.8;
        }


        .text {
            height: 43px;

        }

        label {
            font-size: 18px;
        }

        .btn-primary {
            border-radius: 5px;
            padding: 10px;
            width: 60%
        }

    </style>
   
</head>

<body>
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
            else if (isNaN(Number(s_mobile))) {
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

    <div class="container">
        <div class="row">
        <h1 style="font-size:60px;color:green;"><center>Registration Form</center></h1><br>
        <center>
        <div class="col-md-6 col-md-offset-3" id="form">
        <form action=test2.php method="POST" onsubmit="return validation();">
        <table border="0" cellspacing="10" cellpadding="2">
        <div class="form-group">    
        <tr>
            <td><label>Name :</label></td><td><input type="text" placeholder="Participant Name" id="name" name="name" size="30"></td>
             </tr>
            </div><br>
           
            <div class="form-group"><tr>
            <td><label>Email:</label></td><td><input type="email" placeholder="Email ID" id="email" name="email"><span id="error_email" class="text-danger font-weight-bold" ></span><br></td></tr></div>
            <div class="form-group"><tr>
            <td><label>Date of Birth:</label></td><td> <input type="date" id="dob" name="dob" ><br></td></tr></div>
            <div class="form-group"><tr>
            <td><label>Gender :</label></td><td><input type="radio" name="gender" value="male"> Male
                   :<input type="radio" name="gender" value="female" checked="checked"> Female
                   :<input type="radio" name="gender" value="others" checked="checked"> Others<br></td></tr></div>
                   <div class="form-group"><tr>
            <td><label>Institute Name :</label></td><td> <input type="text" placeholder="Institute Name" id="iname" name="iname" ><br></td></tr></div>
            <div class="form-group"><tr>
            <td><label>Mobile Number :</label></td><td> <input type="text" placeholder="Enter your number" id="mobile" name="mobile"><span id="error_no" class="text-danger font-weight-bold" ></span><br></td></tr></div>
            <div class="form-group"><tr>
            <td><label>Course :</label> </td><td><select id="course" name="course" onchange='return func_course();'> 
                        <option value="" selected disabled hidden>Choose here</option>
                        <option value="science">Engineering Science </option>
                        <option value="arts">Arts </option>
                        <option value="commerce">Commerce </option>
                        <option value="management">Management </option>
                        <option value="others">Others </option>
                    </select>
                    <input type="text" id="box1" name="box1" style='display:none;'><hr></td></tr></div>
                   <div class="form-group"><tr>  
            <td><label>Stream :</label> </td><td><select id="stream" name="stream" onchange='return func_stream();'>
                        <option value="" selected disabled hidden>Choose here</option> 
                        <option value="BE"> BE </option>
                        <option value="BTech">BTech </option>
                        <option value="Bsc">Bsc </option>
                        <option value="BCOM">BCOM </option>
                        <option value="BA">BA </option>
                        <option value="BBA">BBA </option>
                        <option value="BCA">BCA </option>
                        <option value="others2">Others </option>
                    </select><input type="text" id="box2" name="box2" style='display:none;'><hr></td></tr></div>
                    <div class="form-group"><tr>
            <td><label>Events :</label> </td> <td><input type="checkbox" name="event" value="Cultural">Cultural
                      <input type="checkbox" name="event" value="Academics">Academics<br>
                      <input type="checkbox" name="event" value="IT">IT
                      <input type="checkbox" name="event" value="Sports">Sports<br>
                      <input type="checkbox" name="event" value="Academics">Academics
                      <input type="checkbox" name="event" value="Seminars">Seminars<br></td><tr></div>
            <tr>
            <td><input type="submit" value="Submit" class="bt btn-primary"></td></tr>
</table>



                        
                

        </form>
</div>
</center>

    </div>
</body>