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
            $inicio = date("m-d-Y", strtotime("-7 days"));
            $fim = date("m-d-Y");

            $url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' .'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' . '@dataInicial=\'' . $inicio . '\'' . '&@dataFinalCotacao=\'' . $fim . '\'' . '&$top=1&$orderby=dataHoraCotacao desc&$format=json&$select=cotacaoCompra,dataHoraCotacao';

            $dados = json_decode(file_get_contents($url), true);
            $cotacao = $dados["value"][0]["cotacaoCompra"];
            $valorBRL = $_GET["numero"];
            $valorUS = ceil($valorBRL / $cotacao);

            echo "<p>Seus R$" . $valorBRL . " equivalem a <strong>US$ " . $valorUS . "</strong></p>";
        ?>
    </section>
</body>
</html>