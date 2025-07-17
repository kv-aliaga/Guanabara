<?php 
    // número absoluto
    $r = abs(-200);
    echo"$r";

    // converter bases
    //                numero    base decimal   base octal
    $r = base_convert(254, 10, 8);
    echo"<br>$r";

    // arredondar, para cima, baixo
    $r = ceil(456.174588); // 457 <- arr. para cima
    $r = floor(456.174588); // 456 <- arr. para baixo
    $r = round(456.174588); // 456 <- arredonda
    echo "<br>$r";

    // hipotenusa
    $r = hypot(4, 3); // retorna a hipotenusa dos catetos (5)
    echo "<br>$r";

    // intdiv (divisão inteira)
    $r = intdiv(5,2); // 5/2 = 2.5, na intdiv é só 2
    echo "<br>$r";

    // min e max
    $r = min(5, -1459); // mostra qual o menor
    $r = max(123, 856, 123, -5, 4840); // mostra qual o maior
    echo "<br>$r";

    // pi
    $r = M_PI;
    $r = pi(); // M_PI e pi() retornam o mesmo
    echo "<br>$r";

    // raiz quadrada
    $r = 81 ** 0.5;
    $r = sqrt(81); // os dois retornam 9
    echo "<br>$r";

    // raiz cubica
    $r = 27 * (1/3); // não tem operador pra raiz cúbica, preciso fazer na mão
    echo "<br>$r";
?>