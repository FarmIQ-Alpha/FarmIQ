<?php 
session_start();
include("php/config.php");
if (!isset($_SESSION['valid'])) {
    header("Location: index2.php");
    exit();
}

$id = $_SESSION['id'];
$query = mysqli_query($con, "SELECT * FROM users WHERE Id = $id");
$user = mysqli_fetch_assoc($query);

$res_Uname = $user['Username'];
$res_Email = $user['Email'];
$res_Age = $user['Age'];
$res_id = $user['Id'];
$res_Subsidy = $user['Subsidy'];

$subsidyPerHectare = 100; // Fixed subsidy amount per hectare
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/style_home.css">
    <link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
    <title>Checkout Summary</title>
</head>
<body>
    <div class="nav">
        <div class="logo">
            <p><a href="home.php">FarmIQ</a></p>
        </div>
        <div class="right-links">
            <?php echo "<a href='edit.php?Id=$res_id'>Uredi profil</a>"; ?>
            <a href="php/logout.php"><button class="btn">Odjava</button></a>
        </div>
    </div>
    <main>
        <div class="main-box">
            <div class="bottom">
                <div class="box">
                    <h3>Zaključek</h3>
                    <?php
                    if ($_SERVER["REQUEST_METHOD"] == "POST") {
                        $products = $_POST['products'];
                        $hectares = $_POST['hectares'];
                        
                        echo "<table class='table'>";
                        echo "<tr><th>Izdelek</th><th>Hektarji</th><th>Subvencija (€)</th></tr>";
                        
                        $totalSubsidy = 0;
                        foreach ($products as $product) {
                            $hectar = isset($hectares[$product]) ? (int)$hectares[$product] : 0;
                            $productSubsidy = $hectar * $subsidyPerHectare;
                            $totalSubsidy += $productSubsidy;

                            echo "<tr>";
                            echo "<td>" . htmlspecialchars($product) . "</td>";
                            echo "<td>" . htmlspecialchars($hectar) . "</td>";
                            echo "<td>" . htmlspecialchars($productSubsidy) . "</td>";
                            echo "</tr>";
                        }
                        
                        echo "<tr><td colspan='2'><b>Skupaj Subvencija</b></td><td><b>" . htmlspecialchars($totalSubsidy) . " €</b></td></tr>";
                        echo "</table>";
                    } else {
                        echo "Podatki niso bili poslani.";
                    }
                    ?>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
