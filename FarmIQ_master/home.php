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
    <link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
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
            <!-- Ikona za košarico -->
            <div class="cart-icon" id="cart-icon">
                <i class="fa fa-shopping-basket" aria-hidden="true"></i>
                <span id="cart-count">0</span>
            </div>
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
                <!-- Grozdje -->
                <div class="card">
                    <img src="pics/grozdje.jpg">
                    <div class="card-content">
                        <h3>Grozdje</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Grozdje">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Ječmen -->
                <div class="card">
                    <img src="pics/jecmen.jpg">
                    <div class="card-content">
                        <h3>Ječmen</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Ječmen">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Pšenica -->
                <div class="card">
                    <img src="pics/psenica.jpg">
                    <div class="card-content">
                        <h3>Pšenica</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Pšenica">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Solata -->
                <div class="card">
                    <img src="pics/solata.jpg">
                    <div class="card-content">
                        <h3>Solata</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Solata">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Krompir -->
                <div class="card">
                    <img src="pics/krompir.jpg">
                    <div class="card-content">
                        <h3>Krompir</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Krompir">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Koruza -->
                <div class="card">
                    <img src="pics/koruza.jpg">
                    <div class="card-content">
                        <h3>Koruza</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Koruza">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Čebula -->
                <div class="card">
                    <img src="pics/cebula.jpg">
                    <div class="card-content">
                        <h3>Čebula</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Čebula">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Pesa -->
                <div class="card">
                    <img src="pics/pesa.jpg">
                    <div class="card-content">
                        <h3>Pesa</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Pesa">Izberi poljščino</button>
                    </div>
                </div>
                <!-- Por -->
                <div class="card">
                    <img src="pics/por.jpg">
                    <div class="card-content">
                        <h3>Por</h3>
                        <p class="txt">Višina subvencij: 3000 eur <br>
                            Regija: Štajerska<br>
                            Zahtevan % lokalne prodaje: 30%<br>
                            Število subvencij še na voljo: 79
                        </p>
                        <button class="btn add-to-cart" data-name="Por">Izberi poljščino</button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Dodamo div za prikaz sporočila -->
    <div id="cart-message" class="hidden">Izdelek dodan v košarico</div>

    <!-- Dodamo div za prikaz košarice -->
    <div id="cart-overlay" class="hidden">
        <div id="cart-items"></div>
        <button id="close-cart">Zapri</button>
        <form id="checkout-form" action="checkout.php" method="POST">
            <input type="hidden" name="cartItems" id="cartItemsInput">
            <button type="submit" class="btn">Zaključi</button>
        </form>
    </div>

    <script>
        // Seznam za shranjevanje izdelkov v košarici
        let cartItems = [];

        // Funkcija za posodobitev prikaza števila izdelkov v košarici
        function updateCartCount() {
            document.getElementById('cart-count').innerText = cartItems.length;
        }

        // Funkcija za posodobitev prikaza izdelkov v košarici
        function updateCartDisplay() {
            const cartItemsDiv = document.getElementById('cart-items');
            cartItemsDiv.innerHTML = ''; // Počisti prejšnji prikaz
            cartItems.forEach(item => {
                const itemDiv = document.createElement('div');
                itemDiv.innerText = item;
                cartItemsDiv.appendChild(itemDiv);
            });
        }

        // JavaScript za dodajanje v košarico
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', event => {
                const itemName = event.target.getAttribute('data-name');
                
                // Preveri, ali je izdelek že v košarici
                if (!cartItems.includes(itemName)) {
                    cartItems.push(itemName);
                    updateCartCount();
                    updateCartDisplay();

                    const messageDiv = document.getElementById('cart-message');
                    messageDiv.innerText = `${itemName} dodana v izbor`;
                    messageDiv.classList.remove('hidden');
                    messageDiv.classList.add('visible');
                    setTimeout(() => {
                        messageDiv.classList.remove('visible');
                        messageDiv.classList.add('hidden');
                    }, 2000); // Sporočilo izgine po 2 sekundah
                } else {
                    const messageDiv = document.getElementById('cart-message');
                    messageDiv.innerText = `${itemName} je že v izboru`;
                    messageDiv.classList.remove('hidden');
                    messageDiv.classList.add('visible');
                    setTimeout(() => {
                        messageDiv.classList.remove('visible');
                        messageDiv.classList.add('hidden');
                    }, 2000); // Sporočilo izgine po 2 sekundah
                }
            });
        });

        // JavaScript za prikaz in skrivanje košarice
        document.getElementById('cart-icon').addEventListener('click', () => {
            document.getElementById('cart-overlay').classList.remove('hidden');
        });

        document.getElementById('close-cart').addEventListener('click', () => {
            document.getElementById('cart-overlay').classList.add('hidden');
        });

        // JavaScript za pošiljanje podatkov košarice na checkout.php
        document.getElementById('checkout-form').addEventListener('submit', () => {
            const cartItemsInput = document.getElementById('cartItemsInput');
            cartItemsInput.value = JSON.stringify(cartItems);
        });
    </script>
</body>
</html>
