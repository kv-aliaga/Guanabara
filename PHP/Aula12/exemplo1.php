<!-- FORMULÁRIOS RETROALIMENTADOS -->
<!-- não é necessário mais ter uma página HTML e uma página PHP -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../Desafios/style.css">
</head>
<body>
    <!-- Quando for usar um formulário retroalimentado, por padrão fazer isso: -->
    <?php 
        // Capturando os valores do formulário
        $num1 = $_GET["idnum1"] ?? 0;
        $num2 = $_GET["idnum2"] ?? 0;
    ?>

    <main>
        <h1>Somador de Valores</h1>
        <!-- action se direciona para si mesmo -->
        <form action="<?= $_SERVER['PHP_SELF']?> " method="get">
            <label for="idnum1">Valor 1</label>
            <!-- quando usar form. retro. usar value depois do input para pegar as informações  -->
            <input type="number" name="idnum1" id="idnum1" value="<?=$num1?>">

            <label for="idnum2">Valor 2</label>
            <input type="number" name="idnum2" id="idnum2" value="<?=$num2?>">

            <input type="submit" value="Somar">

            
        </form>
    </main>

    <section>
        <h2>Resultado da Soma</h2>
        <?php
            $soma = $num1 + $num2;
            echo "<p>A soma entre $num1 e $num2 é <strong>$soma</strong></p>";
        ?>
    </section>
</body>
</html>