package Aula9.Aula9b;

import java.util.Random;

public class Livro implements Publicacao{
    Random rd = new Random();

//    atributos
    private String titulo; // sem set
    private String autor; // sem set
    private int qtdPaginas; // sem set
    private int paginaAtual; // com set
    private boolean aberto; // sem set
    private String leitor; // com set
    private int codigo; // sem set
    private String editora;

//    construtor
    public Livro(String titulo, String autor, int qtdPaginas, String leitor, String editora){
        this.titulo = titulo;
        this.autor = autor;
        this.qtdPaginas = qtdPaginas;
        this.paginaAtual = 1;
        this.aberto = false;
        this.leitor = leitor;
        this.codigo = rd.nextInt(10000, 999999);
        this.editora = editora;
    }

//    métodos getters e setters
    public String getTitulo(){
        return this.titulo;
    }
    public String getAutor(){
        return this.autor;
    }
    public int getQtdPaginas() {
        return this.qtdPaginas;
    }
    public int getPaginaAtual(){
        return this.paginaAtual;
    }
    public void setPaginaAtual(int paginaAtual){
        this.paginaAtual = paginaAtual;
    }
    public boolean getAberto(){
        return this.aberto;
    }
    public String getLeitor(){
        return this.leitor;
    }
    public void setLeitor(String leitor){
        this.leitor = leitor;
    }
    public int getCodigo(){
        return this.codigo;
    }
    public String getEditora(){
        return this.editora;
    }

//    métodos especiais
    public void abrir(){
        this.aberto = true;
    }
    public void fechar(){
        this.aberto = false;
    }
    public void folhear(){
        int paginaAleatoria = rd.nextInt(1, getQtdPaginas() + 1);

        System.out.println("Você folheou o livro e abriu na página " + paginaAleatoria);

        setPaginaAtual(paginaAleatoria);
    }
    public void avancarPag(){
        if (this.paginaAtual >= this.qtdPaginas){
            System.out.println("Você não pode passar a página");
        } else if (!this.aberto) {
            System.out.println("Você só pode pasar a página se abrir o livro");
        } else{
            this.paginaAtual += 1;
            System.out.println("\nVocê passou para a página: " + this.paginaAtual);
        }
    }
    public void voltarPag(){
        if (this.paginaAtual <= 1){
            System.out.println("Você vê a capa do livro");
            System.out.println(this.titulo.toUpperCase());
            System.out.println(this.autor);
        } else if (!this.aberto) {
            System.out.println("Você só pode pasar a página se abrir o livro");
        } else{
            this.paginaAtual -= 1;
            System.out.println("\nVocê voltou para a página: " + this.paginaAtual);
        }
    }
    public void detalhes(){
        System.out.println("\n === SISTEMA DA BIBLIOTECA === ");
        System.out.println("Título: " + this.titulo);
        System.out.println("Autor: " + this.autor);
        System.out.println("Editora: " + this.editora);
        System.out.println("Quantidade de Páginas: " + this.qtdPaginas);
        System.out.println("Página Atual do Leitor: " + this.paginaAtual);
        System.out.println("Aberto: " + (this.aberto ? "Sim" : "Não"));
        System.out.println("Leitor Atual: " + this.leitor);
        System.out.println("Código: " + this.codigo);
    }
}