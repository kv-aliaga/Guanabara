<?php 
    // CONCATENAÇÃO (para constantes e funções)

    const ESTADO = "SP"; // const não tem $, mas como declará-lo no echo?
    echo "Moro em " . ESTADO ; // usando .

    echo "<br>Estadmos no ano de " . date('Y');

    // SEQUÊNCIAS DE ESCAPE
    $nome = "Rodrigo";
    $sobrenome = "Nogueira";

    echo "<br>$nome \"Minotauro\" $sobrenome"; // Sequência de escape, pede para o interpretador não ver "" como fechamento de strings
    echo "<br>Nova linha\n";
    echo "Tabulação horizontal\t";
    echo "Barra Invertida\\";
    echo "Cifrão\$";
    echo "Codepoint Unicode\u{148F3}";
?>