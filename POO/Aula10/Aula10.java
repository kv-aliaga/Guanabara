package Aula10;

public class Aula10{
    public static void main(String[] args) {
//        instanciando
        Aluno aluno = new Aluno("Jones", 15, "M", "Programação");
        Funcionario funcionario = new Funcionario("Malaquias", 30, "M", "Limpeza", true);
        Professor professor = new Professor("Modolo", 40, "M", "POO", 2000);

        aluno.fazerAniversario(); // aluno faz aniversário
        aluno.trancarCurso();

        funcionario.fazerAniversario();
        funcionario.mudarTrabalho("Zeladoria");

        professor.fazerAniversario();
        professor.receberAumento(100);
    }
}