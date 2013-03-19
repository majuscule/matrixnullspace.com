<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>matrixnullspace</title>
  <link rel="stylesheet" href="/style.css">
  <script type='text/javascript' src='/jquery.js'></script>
  <script type='text/javascript' src='/validate.js'></script>
</head>
<body>

<pre>
usage: matrix.py

Find the kernel, determinant and eigenvalues of the given matrix.

example:

2 3 5
-4 2 3
0 0 0
</pre>

<br>

<form id="calulator" action="calculate" method="post" > 
  <textarea id="matrix" name="matrix" rows="15" cols="40"></textarea>
  <br><br>
  <input type="submit" value="./calculate" id="submit" />
</form> 

</body>

<br>
<h2>written by dylan@<a href="http://dylansserver.com">dylansserver.com</a>
</h2>

</html>
