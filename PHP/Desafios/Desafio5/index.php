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
        <h1>Analisador de Número Real</h1>

        <?php 
            $numero = $_GET["numero"];
            $parteInteira = intdiv($numero,1);
            $parteDecimal = $numero - $parteInteira;

            echo "Analisando o número <strong>" . $numero . "</strong> informado pelo usuário: ";
            echo "
            <nav>
                <ul>
                    <li>
                        A parte inteira do número é <strong>". $parteInteira ."</strong>
                    </li>
                    <li>
                        A parte fracionária do número é <strong>".$parteDecimal ."</strong>
                    </li>
                </ul>
            </nav>";
        ?>
    </section>
</body>
</html>