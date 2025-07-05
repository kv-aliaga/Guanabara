package Aula4.Aula4b;

public class Aula4 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta("Jones", 0.15);
        Caneta c2 = new Caneta("Quinto's Pen", 0.25);

        // fazem o mesmo
//      c1.modelo = "BIC";
//      c1.setPonta(0.5);

        c1.status();

        System.out.printf("Tenho uma caneta %s com a ponta %.2f\n", c1.getModelo(), c1.getPonta());

        c2.status();
    }
}
