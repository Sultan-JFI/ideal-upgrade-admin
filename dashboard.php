<?php
session_start();
if (!isset($_SESSION['admin'])) { header('Location: index.php'); exit; }
?>
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Dashboard</title></head>
<body>
<h2>Welcome, Admin</h2>
<ul>
  <li><a href="products.php">Manage Products</a></li>
  <li><a href="messages.php">View Contact Messages</a></li>
  <li><a href="edit-content.php">Edit Site Content</a></li>
  <li><a href="logout.php">Logout</a></li>
</ul>
</body>
</html>
