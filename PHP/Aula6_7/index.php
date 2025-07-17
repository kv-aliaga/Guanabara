<!-- Formulários em PHP -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Resultado do processamento</h1>
    </header>
    <main>
        <!-- var_dump($_REQUEST); -> junta $_GET, $_POST e $_COOKIES -->
        <?php 
        // o valor dentro de get precisa ser o mesmo do name de index.html
            $nome = $_GET["nome"] ?? "Desconhecido"; // coalesce -> se estiver nulo aparece Desconhecido na tela
            $sobrenome = $_GET["sobrenome"] ?? "Desconhecido";

            echo "Prazer <strong>$nome $sobrenome</strong> esse é meu site!"
        ?>
        <p><a href="javascript:history.go(-1)">Voltar para a página anterior</a></p>
    </main>
</body>
</html>