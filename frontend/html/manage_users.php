<?php
require('../../../DBconnection.php');

$query = "SELECT id, firstname, middlename, lastname, email, access_code FROM user";
$result = mysqli_query($conn, $query);

if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Manage Users</title>
    <style>
        :root {
            --accent: #fcd860;
            --accent-dark: #c5a334;
        }

        body {
            background-color: #1a1a1a;
            color: #fff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 2rem;
            margin: 0;
        }

        .top-bar {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 2rem;
        }

        .back-link {
            background-color: var(--accent);
            color: #000;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            box-shadow: 0 0 10px var(--accent-dark);
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .back-link:hover {
            background-color: var(--accent-dark);
            transform: scale(1.05);
        }

        h2 {
            color: var(--accent);
            text-align: center;
            margin-bottom: 1.5rem;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background-color: #111;
            color: #fff;
            box-shadow: 0 0 10px var(--accent);
        }

        th, td {
            border: 1px solid var(--accent-dark);
            padding: 1rem;
            text-align: center;
        }

        th {
            background-color: #222;
            color: var(--accent);
        }

        a.button {
            background-color: var(--accent-dark);
            color: #000;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }

        a.button:hover {
            background-color: var(--accent);
        }
    </style>
</head>
<body>

<div class="top-bar">
    <a class="back-link" href="../../../admin_dashboard.php"> Back to Admin Dashboard</a>
</div>

<h2>User Management Panel</h2>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Full Name</th>
            <th>Email</th>
            <th>Access Code</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <?php while ($user = mysqli_fetch_assoc($result)): ?>
            <tr>
                <td><?= htmlspecialchars($user['id']) ?></td>
                <td><?= htmlspecialchars($user['firstname'] . ' ' . $user['middlename'] . ' ' . $user['lastname']) ?></td>
                <td><?= htmlspecialchars($user['email']) ?></td>
                <td><?= htmlspecialchars($user['access_code']) ?></td>
                <td>
                    <a class="button" href="admin_upload.html?user_id=<?= $user['id'] ?>">Add Photo</a>
                </td>
            </tr>
        <?php endwhile; ?>
    </tbody>
</table>

</body>
</html>
