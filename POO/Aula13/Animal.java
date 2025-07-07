package Aula13;
// Assinatura do mét.odo: Quantidade de atributos e Tipos de atributos
// Sobreposição: Mesma assinatura em classes diferentes
// Sobrecarga: Assinatura diferentes em mesmas classes

public abstract class Animal {
    // atributos (mesmo se forem protected fazem parte do encapsulamento)
    protected double peso;
    protected int idade;
    protected int qtdMembros;
    protected String nome;

    // métodos especiais
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

    // métodos
    public abstract void emitirSom();
}

