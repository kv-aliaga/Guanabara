<!-- SUPERGLOBAIS NO PHP -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../Desafios/style.css">
</head>
<body>
    <main>
        <pre> <!-- mantém quebras de linha e espaços exatamente como estão no HTML/PHP -->
            <?php
                // cookie: cria uma variável no sistema, no caso de dia-da-semana, ela só é valida por 3600 segundos (1 hora)
                setcookie("dia-da-semana","QUINTA", time() + 3600,"/");
                session_start();
                $_SESSION["teste"] = "FUNCIONOU!";

                echo "<h1>Superglobal GET</h1>";
                var_dump($_GET);

                echo "<h1>Superglobal POST</h1>";
                var_dump($_POST);

                echo "<h1>Superglobal REQUEST</h1>";
                var_dump($_REQUEST);

                echo "<h1>Superglobal COOKIE</h1>";
                var_dump($_COOKIE);

                echo "<h1>Superglobal SESSION</h1>";
                var_dump($_SESSION);

                echo "<h1>Superglobal ENV</h1>";
                foreach(getenv() as $k => $v){
                    echo "<br> $k -> $v";
                }

                echo "<h1>Superglobal SERVER</h1>";
                var_dump($_SERVER);

                echo "<h1>Superglobal GLOBALS</h1>";
                var_dump($GLOBALS);
            ?>
        </pre>
    </main>
</body>
</html>