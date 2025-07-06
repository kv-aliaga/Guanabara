package Aula10;

public class Funcionario extends Pessoa{
//    atributos
    private String setor;
    private boolean trabalhando;

//    construtor
    public Funcionario(String nome, int idade, String genero, String setor, boolean trabalhando){
        super(nome, idade, genero);
        this.setor = setor;
        this.trabalhando = trabalhando;
    }

//    métodos especiais
    public String getSetor(){
        return this.setor;
    }
    public void setSetor(String setor){
        this.setor = setor;
    }
    public boolean getTrabalhando(){
        return this.trabalhando;
    }
    public void setTrabalhando(boolean trabalhando){
        this.trabalhando = trabalhando;
    }

//    métodos
    public void mudarTrabalho(String novoSetor){
        setSetor(novoSetor);
    }
}