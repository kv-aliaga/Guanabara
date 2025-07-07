package Aula14_15;

public class Pessoa {
    // atributos
    protected String nome;
    protected int idade;
    protected String genero;
    protected int experiencia;

    // métodos especiais

    public int getExperiencia() {
        return experiencia;
    }

    public void setExperiencia(int experiencia) {
        this.experiencia = experiencia;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    // métodos
    public void ganharExp(){
        this.experiencia ++;
    }
}
