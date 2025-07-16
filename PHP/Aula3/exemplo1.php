<?php 
    # VARIÁVEIS
    $nome = "Jones";
    $sobrenome = "Fast";
    # CONSTANTES
    const PAIS = "Brasil"; // mesmo comportamento de variáveis que não tem set, e mesma forma de criação, pensar antes e pode ser alterado ou não

    $sobrenome = "S. Vlett"; // sobrescreve Fast
    # PAIS = "EUA"; não pode ser alterado, já que PAIS é uma constante
    echo "Muito prazer, $nome $sobrenome! Você mora no " . PAIS;

?>