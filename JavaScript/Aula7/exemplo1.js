// OPERADORES ARITMÉTICOS
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 % 2 == 1
5 ** 2 == 25

// PRECEDÊNCIA
//      ()
//      **
//      /, % e *
//      + e -

// exemplos com ordem de precedencia
var a = 5 + 3 // = 8
var b = a % 5 // 8 % 5 = 3
var c = 5 * (b ** 2) // 5 * 9 = 45
var d = 10 - (a / 2) // 10 - 4 = 6
var e = (6 * 2) / d // 12 / 6 = 2
var f = b % e + 4 / e // 1 + 2 = 3