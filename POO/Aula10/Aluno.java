package Aula10;

import java.util.Random;

public class Aluno extends Pessoa{
    Random aleatorio = new Random();

//    atributos
    private int matricula;
    private String curso;

//    construtor
    public Aluno(String nome, int idade, String genero, String curso){
        super(nome, idade, genero);
        this.curso = curso;
        this.matricula = aleatorio.nextInt(10000, 99999);
    }

//    métodos getters e setters
    public int getMatricula(){
        return this.matricula;
    }
    public String getCurso(){
        return this.curso;
    }
    public void setCurso(String curso){
        this.curso = curso;
    }

//    métodos
    public void trancarCurso(){
        this.matricula = 0;
        this.curso = "Cancelado";
        System.out.println("Curso cancelado");
    }
}