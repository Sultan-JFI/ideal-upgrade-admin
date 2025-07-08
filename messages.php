<?php
session_start();
if (!isset($_SESSION['admin'])) { header('Location: index.php'); exit; }

$data = json_decode(file_get_contents('data/messages.json'), true);
?>
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Messages</title></head>
<body>
<h2>Contact Messages</h2>
<ul>
<?php foreach ($data as $msg): ?>
  <li><strong><?php echo $msg['name']; ?>:</strong> <?php echo $msg['message']; ?></li>
<?php endforeach; ?>
</ul>
</body>
</html>
