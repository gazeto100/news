function myFunction() {
  var x = document.getElementsByTagName("H1")[0].getAttribute("class");
  document.getElementById("demo").innerHTML = x;
}