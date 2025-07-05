package Aula4.Aula4a;

public class Aula4 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta("BIC Jones", "Azul", 0.02);

        // sobrepõe o construtor de caneta
        c1.setModelo("BIC Jones"); // instancia da mesma forma, dessa vez de forma mais segura
        c1.setPonta(0.2);

        c1.status();
    }
}
