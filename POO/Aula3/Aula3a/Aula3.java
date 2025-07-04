package Aula3.Aula3a;

public class Aula3 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();

        c1.cor = "Azul";
        c1.modelo = "BIC Jones";
//      c1.ponta = 0,5;
        // ⬑ esse código dá erro, já que ponta é privada e só é permitida de ser usada em Caneta.java

        c1.rabiscar(); // não tem problemas em chamar rabiscar já que é public void rabiscar
    }
}
