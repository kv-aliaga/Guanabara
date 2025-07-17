<!-- Quatro formatos de String em PHP -->
<?php 
    $nome = "Jones";
    // double quoted (existe a interpretação do conteudo)
    echo "<h2>DOUBLE QUOTED</h2>";
    echo "Jones" . " PHP"; // <- Neste caso, o . serve como um concatenador de Strings (não é usado o + como em outras linguagens de programação)

    echo "<br>PHP \u{1F418}"; // \u{1F418} é interpretado e mostra 🐘
    echo "<br>Olá $nome!";

    // single quoted
    echo "<h2>SINGLE QUOTED</h2>";
    echo '<br>PHP \u{1F418}'; // \u{1F418} não é interpretado, mostrado literalmente
    echo '<br>Olá $nome!'; // também nãoo é interpretado
?>