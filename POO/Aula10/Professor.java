package Aula10;

public class Professor extends Pessoa{
//    atributos
    private String especialidade;
    private double salario;

//     construtor
    public Professor(String nome, int idade, String genero, String especialidade, double salario){
        super(nome, idade, genero);
        this.especialidade = especialidade;
        this.salario = salario;
    }

//    métodos especiais
    public String getEspecialidade(){
        return this.especialidade;
    }
    public void setEspecialidade(String especialidade){
        this.especialidade = especialidade;
    }
    public double getSalario(){
        return this.salario;
    }

//    métodos
    public double receberAumento(double porcentagem){
        System.out.println("Antigo salário: R$" + this.salario);
        this.salario += this.salario * (porcentagem / 100);
        System.out.println("Novo salário: R$" + this.salario);
        return this.salario;
    }
}