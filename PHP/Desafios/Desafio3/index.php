<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <section>
        <h1>Conversor de Moedas</h1>

        <?php 
            $conversaoUS = 5.57;
            $valorBRL = $_GET["numero"];
            $valorUS = ceil($valorBRL / $conversaoUS);

            echo "<p>Seus R$" . $valorBRL . " equivalem a <strong>US$ " . $valorUS . "</strong></p>"
        ?>
    </section>
</body>
</html>