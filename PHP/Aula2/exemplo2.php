<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>
        Exemplo de PHP
    </h1>

    <?php 
        // mostrando o dia
        echo"Hoje é dia ", date("d/m/Y");// 16/07/2025
        echo"<br>Hoje é dia ", date("D/M/Y"); // Wed/Jul/2025
        echo"<br>Hoje é dia ", date("d/m/y"); // 16/07/25

        // mostrando as horas (mostra o horário do servidor (Berlim) )
        echo "<br><br>e a hora atual é: ", date("G:i:s"); // 9:32:31

        date_default_timezone_set("America/Sao_Paulo"); // transforma horário do servidor para São Paulo
        echo "<br>e a hora atual é: ", date("G:i:s") // 4:32:31
    ?>
</body>
</html>