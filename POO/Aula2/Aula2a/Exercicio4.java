package Aula2.Aula2a;
// Cria uma classe para algo imaterial
//  Tema: Ler um livro

public class Exercicio4 {
    String nomeLivro;
    int qtdPaginas;
    int paginasLidas; // de 0
    int qtdDias;

    public void lerLivro(int qtdLidas){
        paginasLidas += qtdLidas;
        if (paginasLidas > qtdPaginas){
            paginasLidas = qtdPaginas;
        }
    }
    public void passarDia(){
        qtdDias ++;
    }
}
