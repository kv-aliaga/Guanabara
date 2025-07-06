package Aula9.Aula9a;

import java.util.Scanner;

// passei as questões da Aula 9a pra java :)

public class Exercicios {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

//        Atribuindo valor as variáveis
        String[] respostas = new String[15];
        String jForm;
        double nota = 0;

//        inicializando gabarito
        String[] gabarito = {"C", "A", "A", "B", "C", "C", "C", "D", "B", "B", "B", "D", "D", "D", "D"};
        String[] perguntas = {
//                questão 1
                "Uma casa está para uma planta arquitetônica assim como um objeto está para...",

//                questão 2
                "A programação orientada a objetos se preocupa em produzir software que tenha as seguintes características",

//                questão 3
                "Assinale a alternativa incorreta com relação ao conceito de classe e objeto em Programação Orientada a Objetos.",

//                questão 4
                "Correlacione a coluna da esquerda com a da direita e assinale a alternativa que contém a sequência correta.\n" +
                        "(1) Atributo         ( ) ação executada por um objeto\n" +
                        "(2) Classe           ( ) define os atributos e comportamentos comuns\n" +
                        "(3) Comportamento    ( ) característica de uma classe que é visível\n" +
                        "(4) Domínio          ( ) construção de software que encapsula estado e comportamento\n" +
                        "(5) Objeto           ( ) espaço onde o problema reside\n",

//                questão 5
                "Assinale a alternativa incorreta sobre a definição de termos usados em POO:",

//                questão 6
                "Associe as colunas e a seguir marque a opção que contém a sequência correta:\n" +
                        "(1) construtor       ( ) métodos que dão acesso aos dados internos\n" +
                        "(2) acessor          ( ) define as diferentes espécies de valores que podem ser usados\n" +
                        "(3) mutante          ( ) métodos que permitem que se altere o estado de um objeto\n" +
                        "(4) tipos            ( ) métodos usados para inicializar objetos durante a instanciação\n",

//                questão 7
                "Quais são os três pilares da Programação Orientada a Objetos?",

//                questão 8
                "Correlacione a coluna da esquerda com a da direita e assinale a alternativa que contém a sequência correta\n" +
                        "(1) Classe           ( ) define o que uma entidade pode fazer com o objeto\n" +
                        "(2) Interface        ( ) instanciação de uma classe\n" +
                        "(3) Construtor       ( ) Define os atributos e comportamentos compartilhados\n" +
                        "(4) Objeto           ( ) utilizado para inicializar objetos\n",

//                questão 9
                "A maioria das linguagens orientadas a objetos suporta quais níveis de acesso?",

//                questão 10
                "No contexto dos níveis de acesso, selecione a alternativa que contém o nível que apenas garante o acesso para aquele objeto e suas subclasses.",

//                questão 11
                "A proteção de atributos e operações das classes, fazendo com que estas se comuniquem com o meio externo por meio de suas interfaces, define o conceito de:",

//                questão 12
                "Quando se utiliza o conceito de encapsulamento da POO, enquanto a ______ define os detalhes internos do componente, a ______ lista os serviços fornecidos por ele.",

//                questão 13
                "______ é a característica da POO que permite separar o programa em várias partes menores e independentes. Cada parte possui sua implementação isolada e realiza seu trabalho de forma autônoma. Com essa característica é possível ocultar os detalhes internos de cada parte através de uma interface.",

//                questão 14
                "Qual é o conceito de POO que significa representar uma entidade, incluindo apenas seus atributos mais relevantes?",

//                questão 15
                "Com relação aos conceitos de POO, assinale a opção incorreta."
        };
        String[][] questoes = {
                // Alternativas da Questão 1
                {"um método", "uma propriedade", "uma classe", "um atributo"},

                // Alternativas da Questão 2
                {"natural, confiável, reutilizável, manutenível, extensível e oportuno",
                        "natural, mensurável, manutenível, instantâneo, acessível e confiável",
                        "confiável, reutilizável, extensível, mensurável, acessível e fácil de usar",
                        "extensível, natural, mensurável, reutilizável, instantâneo e simples"},

                // Alternativas da Questão 3
                {"Uma classe é instância de um objeto",
                        "Um objeto é uma construção de software que encapsula estado e comportamento",
                        "Uma classe define os atributos e comportamentos compartilhados por um tipo de objeto",
                        "Em uma Linguagem POO pura, tudo é um objeto, desde os tipos mais básicos"},

                // Alternativas da Questão 4
                {"3, 2, 4, 5, 1",
                        "3, 2, 1, 5, 4",
                        "2, 3, 1, 5, 4",
                        "2, 4, 3, 1, 5"},

                // Alternativas da Questão 5
                {"Uma variável interna é um valor mantido dentro do objeto",
                        "Atributos são as características de uma classe visíveis externamente",
                        "Comportamento são as características de uma classe invisíveis externamente",
                        "O estado de um objeto é o significado combinado das variáveis internas do objeto"},

                // Alternativas da Questão 6
                {"1, 2, 3, 4",
                        "2, 4, 1, 3",
                        "2, 4, 3, 1",
                        "4, 2, 3, 1"},

                // Alternativas da Questão 7
                {"herança, polimorfismo e instância",
                        "herança, polimorfismo e metodologia",
                        "encapsulamento, herança e polimorfismo",
                        "encapsulamento, polimorfismo e metodologia"},

                // Alternativas da Questão 8
                {"1, 2, 4, 3",
                        "1, 4, 2, 3",
                        "2, 3, 1, 4",
                        "2, 4, 1, 3"},

                // Alternativas da Questão 9
                {"secreto, público e primário",
                        "público, protegido e privado",
                        "público, protegido e primário",
                        "público, privado e secundário"},

                // Alternativas da Questão 10
                {"público", "protegido", "privado", "oculto"},

                // Alternativas da Questão 11
                {"polimorfismo", "encapsulamento", "herança", "agregação"},

                // Alternativas da Questão 12
                {"interface - implementação", "classe - implementação", "interface - classe", "implementação - interface"},

                // Alternativas da Questão 13
                {"herança", "hierarquia", "polimorfismo", "encapsulamento"},

                // Alternativas da Questão 14
                {"encapsulamento", "polimorfismo", "abstração", "herança"},

                // Alternativas da Questão 15
                {"classes são tipos abstratos de dados", "objetos são instâncias de uma classe", "subclasse é uma classe definida por meio de outra classe", "atributos são subprogramas que definem as operações em objetos de uma classe"}
        };


        for (int i = 0; i < questoes.length; i ++){
            System.out.println("\nPERGUNTA " + (i + 1) + ": " + perguntas[i]);
            for (int j = 0; j < questoes[i].length; j ++){

                if (j == 0){
                    jForm = "A";
                } else if (j == 1) {
                    jForm = "B";
                } else if (j == 2) {
                    jForm = "C";
                } else {
                    jForm = "D";
                }

                System.out.println(jForm + ": " + questoes[i][j]);
            }
            System.out.print("\n(" + (i + 1) + ") Digite sua resposta: ");
            respostas[i] = input.nextLine().toUpperCase().strip();
            if (respostas[i].equals(gabarito[i])){
                System.out.println("Acertou!\n");
                nota += 0.66;
            } else{
                System.out.println("Errou, Reposta certa: " + gabarito[i] + "\n");
            }
        }
        System.out.printf("\nSua final nota foi: %.2f/10", nota);
    }
}
