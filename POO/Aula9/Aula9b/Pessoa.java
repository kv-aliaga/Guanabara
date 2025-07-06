package Aula9.Aula9b;

public class Pessoa {
//    atributos
    private String nome;
    private int idade;
    private String genero;

//    construtor
    public Pessoa(String nome, int idade, String genero){
        this.nome = nome;
        this.idade = idade;
        this.genero = genero;
    }

//    métodos especiais
    public String getNome(){
        return this.nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public int getIdade(){
        return this.idade;
    }
    public String getGenero(){
        return this.genero;
    }
    public void setGenero(String genero){
        this.genero = genero;
    }

//    métodos
    public int fazerAniversario(){
        return this.idade ++;
    }
}
