package Aula9.Aula9b;

import java.util.Scanner;

public class Aula9 {
    public static void main(String[] args) {
//        instanciando
        Pessoa p1 = new Pessoa("Jones", 15, "M");
        Livro l1 = new Livro("Mary Poppins", "P.L. Travers", 229, p1.getNome(), "Zahar");

//        mostrando informações

        l1.abrir(); // abre o livro
        l1.fechar(); // fecha o livro
        l1.abrir();

        l1.folhear(); // escolhe página aleatória
        l1.detalhes(); // mostra detalhes

        l1.avancarPag();
        l1.voltarPag();

        l1.detalhes();
    }
}
