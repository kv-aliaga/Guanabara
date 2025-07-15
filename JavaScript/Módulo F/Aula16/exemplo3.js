var v = function(x){
    return x * 2
}

console.log(v(10)) // v = func(10) -> 10*2

// recursividade
function fatorial(n){
    if (n == 1){
        return 1
    } else{
        return n * fatorial(n-1)
    }
}

console.log(fatorial(5))