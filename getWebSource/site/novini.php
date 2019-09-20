<style>
<?php
include ('box.css');
?>
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

<?php
include ('menu.html');
?>

<?php
$link = mysqli_connect("localhost", "root", "", "newsbg");

mysqli_set_charset($link,"utf8");
if ($link === false) {
    die("ERROR: Could not connect. "
                .mysqli_connect_error());
}

$sql = "SELECT * FROM dnesbg WHERE site='novini.bg' ORDER BY id DESC";
if ($res = mysqli_query($link, $sql)) {
    if (mysqli_num_rows($res) > 0) {
        while ($row = mysqli_fetch_array($res)) {

             echo "<div class='infobox-container'>";
             echo "<div class='infobox'>";
             echo "<h3><span>".$row['site']."</span></h3>";
             echo "<hr>";
             echo "<a target='_blank' href=".$row['link']."> <img src=".$row['img']." height='100' width='150'></a>";
             echo "<hr>";
             echo "<a target='_blank' id='title' href=".$row['link'].">";
             echo "<div class='title'><p>".$row['title']."</p></div>";
             echo "</a>";
             echo "<p style='color:black; vertical-align: text-bottom;'>От: ".$row['data']."<p>";
             echo "</div>";
             echo "<hr>";
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

<?php
include ('footer.html');
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
