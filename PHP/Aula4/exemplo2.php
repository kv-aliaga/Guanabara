<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Testes de Tipos Primitivos</h1>
    <?php 
        $exemploHex = 0x1A; // igual a 26 (hexadecimal)
        echo "A variável é $exemploHex";

        $exemploBin = 0b1010; // igual a 10 (binário)
        echo "<br>A variável é $exemploBin";

        $exemploOct = 010; // igual a 8 (octal)
        echo "<br>A variável é $exemploOct <br><br>";

        $var = "Joãozinho";
        echo"Mostrando todas as informações de var: ";
        var_dump($var)
    ?>
</body>
</html>