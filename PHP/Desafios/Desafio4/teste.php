<?php 
    $inicio = date("m-d-Y", strtotime("-7 days"));
    $fim = date("m-d-Y");

    $url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' .'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' . '@dataInicial=\'' . $inicio . '\'' . '&@dataFinalCotacao=\'' . $fim . '\'' . '&$top=1&$orderby=dataHoraCotacao desc&$format=json&$select=cotacaoCompra,dataHoraCotacao';

    $dados = json_decode(file_get_contents($url), true);
    $cotacao = $dados["value"][0]["cotacaoCompra"];

    var_dump($cotacao);
?>
