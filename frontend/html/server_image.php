<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

require('../../../DBconnection.php');

if (!isset($_GET['access_code']) || !isset($_GET['file'])) {
    http_response_code(400);
    exit('Invalid request');
}

$access_code = $_GET['access_code'];
$file = basename($_GET['file']); 

$stmt = $conn->prepare("SELECT id FROM user WHERE access_code = ?");
$stmt->bind_param("s", $access_code);
$stmt->execute();
$result = $stmt->get_result();

if ($row = $result->fetch_assoc()) {
    $user_id = $row['id'];
    $image_path = "../../uploads/user_$user_id/$file";

    if (file_exists($image_path)) {
        $mime = mime_content_type($image_path);
        header("Content-Type: $mime");
        readfile($image_path);
        exit;
    } else {
        http_response_code(404);
        exit("Image not found");
    }
} else {
    http_response_code(403);
    exit("Invalid access code");
}
