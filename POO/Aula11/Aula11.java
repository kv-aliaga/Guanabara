package Aula11;

public class Aula11 {
    public static void main(String[] args) {
        Visitante v1 = new Visitante();
        Aluno a1 = new Aluno();
        Bolsista b1 = new Bolsista();

//        instanciando
        a1.setCurso("Programação");
        a1.setMatricula(123456);
        a1.setNome("Jones");
        a1.setIdade(15);
        a1.setGenero("M");

        b1.setBolsa(2000);
        b1.setCurso("Programação");
        b1.setMatricula(147258);
        b1.setNome("Jones");
        b1.setIdade(15);
        b1.setGenero("M");

        v1.setGenero("M");
        v1.setIdade(16);
        v1.setNome("Francisco");


    }
}
