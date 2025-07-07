package Aula12;

public abstract class Animal {
//    Tipos de Polimorfismo: SOBRECARGA E SOBREPOSIÇÃO
    private double peso;
    private int idade;
    private int qtdMembros;
    private String nome;

//    métodos especiais
    public double getPeso() {
        return peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public int getQtdMembros() {
        return qtdMembros;
    }

    public void setQtdMembros(int qtdMembros) {
        this.qtdMembros = qtdMembros;
    }

    //    métodos
    public abstract void locomover(); // métodos abstratos não podem ter {}
    public abstract void alimentar();
    public abstract void emitirSom();

}
