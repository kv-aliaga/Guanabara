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
        <h1>Resultado Final</h1>

        <?php 
            $num = $_GET["numero"];

            echo "<p>O número escolhido foi <strong>$num</strong></p>";
            echo "<p>O seu antecessor é <strong>" . ($num - 1) . "</strong></p>";
            echo "<p>O seu sucessor é <strong>" . ($num + 1) . "</strong></p>"
        ?>
        <p><a href="javascript:history.go(-1)"><- Voltar</a></p>
    </section>
</body>
</html>