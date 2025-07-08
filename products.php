<?php
session_start();
if (!isset($_SESSION['admin'])) { header('Location: index.php'); exit; }

$data = json_decode(file_get_contents('data/products.json'), true);
?>
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Products</title></head>
<body>
<h2>Product List</h2>
<ul>
<?php foreach ($data as $product): ?>
  <li><?php echo $product['name']; ?> - <?php echo $product['price']; ?> Toman</li>
<?php endforeach; ?>
</ul>
</body>
</html>
