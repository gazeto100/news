<?php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['text'];
$formcontent=" From: $name \n Message: $message";
$recipient = "andrei_terziev@abv.bg";
$subject = "Contact Form";
$mailheader = "From: $email \r\n";
mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
echo "Thank You!" . " -" . "<a href='form.html' style='text-decoration:none;color:#ff0099;'> Return Home</a>";
?>
