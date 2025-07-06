package Aula11;

import java.util.Random;

public class Aluno extends Pessoa{
    Random rd = new Random();

//    atributos
    private int matricula;
    private String curso;

//    métodos getters e setters
    public int getMatricula(){
        return this.matricula;
    }
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    public String getCurso(){
        return this.curso;
    }
    public void setCurso(String curso){
        this.curso = curso;
    }

//    métodos
    public void pagarMensalidade(){
        double mensalidade = 2000;
        System.out.println("Mensalidade de R$" + mensalidade + " paga");
    }
}
