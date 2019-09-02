<style>
    .infobox-container {
    display: inline-block;
    margin: 0;
    padding: 0;
    width: 300px;
}
.infobox {
    width: 250px;
    background: #FFFFFF;
    padding: 10px 5px 5px 5px;
    margin:10px;
    color: #fff;
    font-size: 90%;
    height: 300px;

}

.infobox:hover{
  box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
}
.infobox h3 {
    background: #3198dd;
    width: 270px;
    color: #fff;
    padding: 10px 5px;
    margin: 0;
    font-size: 140%;
    text-align: center;
    font-weight: bold;
    position: relative;
    left: -15px;
}

a { color: #000000; }
a:hover { color: #FFFO00; }

.title{
    width:auto;
    height:200px;
}

</style>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml" xml:lang="bg" lang="bg">

<head>

<meta charset="windows-1251" />
 <meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="box.css">
</head>
<body>

<div class="topnav" id="myTopnav">
  <a href="#home" class="active">Home</a>
  <a href="#news">Nova.bg</a>
  <a href="#contact">Dnes.bg</a>
  <a href="#about">24chasa.bg</a>
  <a href="#about">Novini.bg</a>
  <a href="#about">Dir.bg</a>
  <a href="#about">Blitz.bg</a>
  <a href="#about">Vesti.bg</a>
  <a href="#about">Actualno.bg</a>
  <a href="#about">Dariknews.bg</a>
  <a href="#about">Btv.bg</a>
  <a href="javascript:void(0);" class="icon" onclick="myFunction()">
    <i class="fa fa-bars"></i>
  </a>
</div>

<?php
$link = mysqli_connect("localhost", "root", "", "newsbg");

mysqli_set_charset($link,"utf8");
if ($link === false) {
    die("ERROR: Could not connect. "
                .mysqli_connect_error());
}

$sql = "SELECT * FROM dnesbg WHERE site='blitz.bg' ORDER BY id DESC";
if ($res = mysqli_query($link, $sql)) {
    if (mysqli_num_rows($res) > 0) {
        while ($row = mysqli_fetch_array($res)) {

             echo "<div class='infobox-container'>";
             echo "<div class='infobox'>";
             echo "<h3><span>".$row['site']."</span></h3>";
             echo "<hr>";
             echo "<a target='_blank' href=".$row['link']."> <img src=".$row['img']." height='100' width='150'></a>";
             echo "<hr>";
             echo "<a target='_blank' href=".$row['link'].">";
             echo "<div class='title'><p>".$row['title']."</p></div>";
             echo "</a>";
             echo "</div>";
             echo "</div>";

        }
    }
    else {
        echo "No matching records are found.";
    }
}
else {
    echo "ERROR: Could not able to execute $sql. "
                                .mysqli_error($link);
}
mysqli_close($link);
?>

<script>
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
</script>
</body>
</html>
