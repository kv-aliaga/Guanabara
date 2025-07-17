<?php 
    $nome = 'Jones \u{1F596}'; // single quoted -> não interpreta
    $nome2 = "Jones \u{1F596}"; // double quoted -> interpreta

    echo "$nome";
    echo "<br>$nome2";
?>
