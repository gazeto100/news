 
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
<link rel="stylesheet" href="style.css" type="text/css" media="all" />
</head>
<body>

<?php
include ('menu.html');
?>

	<h2>Contact Form</h2>

	<form class="form" action="mail.php" method="POST">

		<p class="name">
		<label for="name">Name</label><br>
			<input type="text" name="name" id="name" placeholder="John Doe" />

		</p>

		<p class="email">
		<label for="email">Email</label><br>
			<input type="text" name="email" id="email" placeholder="mail@example.com" />

		</p>

		<p class="text">
			<textarea name="text" placeholder="Write something to us" width="300"/></textarea>
		</p>

		<p class="submit">
			<input type="submit" value="Send" />
		</p>
	</form>

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
