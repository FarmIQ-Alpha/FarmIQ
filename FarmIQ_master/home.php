<?php 
session_start();
include("php/config.php");
if(!isset($_SESSION['valid'])){
    header("Location: index2.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/style_home.css">
    <title>Home</title>
</head>
<body>
    <div class="nav">
        <div class="logo">
            <p><a href="home.php">FarmIQ</a></p>
        </div>

        <div class="right-links">
            <?php 
            $id = $_SESSION['id'];
            $query = mysqli_query($con, "SELECT * FROM users WHERE Id = $id");

            while($result = mysqli_fetch_assoc($query)){
                $res_Uname = $result['Username'];
                $res_Email = $result['Email'];
                $res_Age = $result['Age'];
                $res_id = $result['Id'];
            }
            
            echo "<a href='edit.php?Id=$res_id'>Uredi profil</a>";
            ?>
            <a href="php/logout.php"><button class="btn">Odjava</button></a>
        </div>
    </div>
    <main>
        <div class="main-box">
            <div class="top">
                <div class="box">
                    <p>Pozdravljeni <b><?php echo $res_Uname ?></b></p>
                </div>
                <div class="box">
                    <p>Vaše uporabniško ime je <b><?php echo $res_Email ?></b></p>
                </div>
            </div>
            <div class="bottom">
                <div class="box">
                    <p>Trenutno imate <b><?php echo $res_Age ?> hektarjev obdelovalnih površin.</b></p> 
                </div>
            </div>
            <div class="card-container">
                <div class="card">
                    <img src="pics/grozdje.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/jecmen.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/psenica.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/solata.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/krompir.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/krompir.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/krompir.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/krompir.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
                <div class="card">
                    <img src="pics/krompir.jpg">
                    <div class="card-content">
                        <h3>Izdelek</h3>
                        <p>Neki random text je trenutno</p>
                        <a href="" class="btn">Izberi poljščino</a>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
