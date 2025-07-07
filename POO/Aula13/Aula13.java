package Aula13;

public class Aula13 {
    public static void main(String[] args) {
        Cachorro c1 = new Cachorro();

        c1.setIdade(10);
        c1.setNome("Jones");
        c1.setPeso(10);
        c1.setQtdMembros(4);

        c1.reagir(15);
        c1.reagir(true);
        c1.reagir(c1.getNome());
        c1.reagir(15, 60);
    }
}
