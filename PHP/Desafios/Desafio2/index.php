<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta name="autor" content="kv-aliaga">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../style.css">
    <title>Jones</title>
</head>
<body>
    <section>
        <h1>Trabalhando com números aleatórios</h1>
        <?php 
            $valor = mt_rand(1, 100);
            echo "<p>Gerando um número aleatório entre 0 e 100...</p>";
            echo "<p>O valor gerado foi <strong>" . $valor . "</strong></p>";
        ?>
        <input type="submit" value="Gerar outro" onclick="location.reload(); return false;"> 
    </section>
</body>
</html>