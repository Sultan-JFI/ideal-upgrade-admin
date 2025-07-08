<?php
session_start();
if (!isset($_SESSION['admin'])) { header('Location: index.php'); exit; }
?>
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Edit Content</title></head>
<body>
<h2>Edit Site Content</h2>
<p>Feature under development</p>
</body>
</html>
