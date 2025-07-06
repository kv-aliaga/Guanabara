package Aula11;
// CLASSE ABSTRATA: Não pode ser instanciada. Só pode servir como progenitora.

// MÉTODO ABSTRATO: Declarado, mas não implementado na progenitora.

// CLASSE FINAL: Não pode ser herdada por outra classe. Obrigatoriamente folha.

// MÉTODO FINAL: Não pode ser sobrescrito pelas sub-classes. Obrigatoriamente herdado.

public abstract class Pessoa { // classe abstrata (não tem métodos especiais)
    private String nome;
    private int idade;
    private String genero;

//    método
    public String getNome(){
        return this.nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public int getIdade(){
        return this.idade;
    }
    public void setIdade(int idade){
        this.idade = idade;
    }
    public String getGenero(){
        return this.genero;
    }
    public void setGenero(String genero){
        this.genero = genero;
    }

    // método final
    public final void fazerAniversario(){
        this.idade ++;
    }
}
