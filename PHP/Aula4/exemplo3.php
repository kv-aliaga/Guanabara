<!-- Coerção em php -->

<?php 
    $numString = "2602";
    var_dump($numString);

    echo"<br>";

    $numString = (int) $numString; // transforma em número inteiro
    var_dump( $numString );
?>