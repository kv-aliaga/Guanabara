// OPERADORES LÓGICOS

// ! = negação, tudo o que é diferente do primeiro termo
// && = conjunção, se os dois valores forem verdadeiros, retorna verdadeiro
// || = disjunção, se um dos valores forem verdadeiros, retorna verdadeiro

// ORDEM DE PRECEDÊNCIA
// aritméticos > relacionais > ! > && > ||

var a = 5
var b = 2

a > b && b % 2 == 0
// 2 % 2 == 0 (true)
// 5 > 2 (true)
// true e true (true)

a < b || b % 2 == 0
// 2 % 2 == 0 (true)
// 5 < 2 (false)
// false e true (true)