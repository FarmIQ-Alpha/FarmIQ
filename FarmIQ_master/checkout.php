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
$res_Subsidy = $user['Subsidy']; // Assuming there is a Subsidy field in the users table
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/style_home.css">
    <link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
    <title>Checkout</title>
    <style>
        .table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .table, .table th, .table td {
            border: 1px solid black;
        }

        .table th, .table td {
            padding: 8px;
            text-align: left;
        }

        .btn {
            height: 35px;
            background: #000000;
            border: none;
            border-radius: 5px;
            color: #fff;
            font-size: 15px;
            cursor: pointer;
            transition: all 0.3s;
            width: auto;
            padding: 5px 15px;
            margin: 20px;
        }

        .btn:hover {
            opacity: 0.85;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .hay-bale {
            width: 200px;
            height: 200px;
            background-image: url('pics/bala.jpg');
            background-size: cover;
            animation: rotate 2s linear infinite;
        }

        .container {
            position: absolute;
            top: 50%; 
            right: 50%;
            transform: translate(50%,-50%);
        }

        .error {
            color: red;
            font-weight: bold;
        }
    </style>
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
                    <p>Trenutno imate <b id="total-hectares"><?php echo $res_Age; ?></b> hektarjev obdelovalnih površin.</p>
                    <p>Preostale subvencije: <b><?php echo $res_Subsidy; ?> €</b></p>
                    <div class="cart-box">
                        <?php
                        if ($_SERVER["REQUEST_METHOD"] == "POST") {
                            $cartItems = json_decode($_POST['cartItems'], true);
                            $output = exec("python3 FarmIQ_master/web_predict1.py");
                            $variables = json_decode($output, true);

                            $x = $variables['hello'];
                            var_dump($x);
                        

                            if (!empty($cartItems)) {
                                echo "<h3>Izbrane poljščine:</h3>";
                                echo "<form id='checkoutForm' action='koncaj.html' method='POST' onsubmit='return validateForm()'>";
                                echo "<table class='table'>";
                                echo "<tr><th>Izdelek</th><th>Hektarji</th></tr>";
                                foreach ($cartItems as $item) {
                                    echo "<tr>";
                                    echo "<td>$item</td>";
                                    echo "<td><input class='hectar-input' type='number' name='hectares[$item]' min='0' onkeyup='handler()' required></td>";
                                    echo "</tr>";
                                }
                                echo "</table>";
                                echo "<button class='btn' type='submit'>Potrdi</button>";
                                echo "</form>";
                                echo "<p id='error-message' class='error'></p>";
                            } else {
                                echo "Košarica je prazna.";
                            }
                        } else {
                            echo "Podatki niso bili poslani.";
                        }
                        ?>
                    </div>
                </div>
            </div>
            <div class="container">
                <div class="hay-bale"></div>
            </div>
        </div>
    </main>
    <script>
        setTimeout(() => {
            document.getElementsByClassName('container')[0].remove();
        }, 2000);

        function validateForm() {
            return !checkHectaresExceeded();
        }

        function handler() {
            checkHectaresExceeded();
        }

        function checkHectaresExceeded() {
            let totalHectares = 0;
            const maxHectares = <?php echo $res_Age; ?>;
            const inputs = document.getElementsByClassName('hectar-input');
            const errorMessage = document.getElementById('error-message');
            const totalHectaresElement = document.getElementById('total-hectares');
            const initialHectares = <?php echo $res_Age; ?>;

            for (let i = 0; i < inputs.length; i++) {
                totalHectares += parseFloat(inputs[i].value) || 0;
            }

            const remainingHectares = initialHectares - totalHectares;

            if (totalHectares > maxHectares) {
                errorMessage.innerText = "Prekoračili ste vsote hektarjev.";
                totalHectaresElement.innerText = remainingHectares < 0 ? 0 : remainingHectares;
                return true;
            } else {
                errorMessage.innerText = "";
                totalHectaresElement.innerText = remainingHectares;
                return false;
            }
        }
    </script>
</body>
</html>
