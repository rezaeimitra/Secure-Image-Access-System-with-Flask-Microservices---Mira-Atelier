<?php
require('../../../DBconnection.php');


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user_id = intval($_POST['user_id']);

    if (isset($_FILES['image']) && $_FILES['image']['error'] === 0) {
        $uploadDir = "uploads/user_$user_id/";
        if (!is_dir($uploadDir)) {
            mkdir($uploadDir, 0755, true);
        }

        $filename = basename($_FILES['image']['name']);
        $targetPath = $uploadDir . $filename;

        if (move_uploaded_file($_FILES['image']['tmp_name'], $targetPath)) {
            echo "✅ Upload successful!";
        } else {
            echo "❌ Upload failed.";
        }
    } else {
        echo "❌ No file uploaded.";
    }
}
?>
