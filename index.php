<?php
session_start();
if (isset($_POST['username']) && isset($_POST['password'])) {
    if ($_POST['username'] === 'admin' && $_POST['password'] === '1234') {
        $_SESSION['admin'] = true;
        header('Location: dashboard.php');
        exit;
    } else {
        $error = "Wrong credentials.";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Admin Login</title></head>
<body>
<h2>Login to Admin Panel</h2>
<?php if (!empty($error)) echo "<p style='color:red;'>$error</p>"; ?>
<form method="POST">
    <input type="text" name="username" placeholder="Username" required/><br/>
    <input type="password" name="password" placeholder="Password" required/><br/>
    <button type="submit">Login</button>
</form>
</body>
</html>
