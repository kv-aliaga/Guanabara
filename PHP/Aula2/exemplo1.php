<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            font-family: Arial, Helvetica, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Usar <script lenguage="php"> não funciona mais -->
    <?php 
        // cria a variável nome
        $nome = "Jones S Vlett";
        // mostra a variável nome em um parágrafo
        echo "<p>O meu nome é $nome</p>";

        // INFORMAÇÕES SOBRE O PHP: se for só um comando no <?php? > não é necessário usar ;
        // Se for só um comando é possível simplificar para somente <?? >, que se chama shorttag php
        // se só tiver um <?php e echo é possível simplificar para <?= e sem usar ; (por mais que usá-las sejam boas práticas)

        // se um erro acontecer em php, vai ser mostrado no HTML
        // Fatal error: Uncaught Error: Undefined constant "phpfp" in C:\xampp\htdocs\cursophp\Guanabara\PHP\Aula2\exemplo1.php:25 Stack trace: #0 {main} thrown in C:\xampp\htdocs\cursophp\Guanabara\PHP\Aula2\exemplo1.php on line 25
    ?>
</body>
</html>