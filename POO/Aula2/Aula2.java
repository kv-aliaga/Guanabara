package Aula2;

public class Aula2 {
    public static void main(String[] args) {
        // cria conexão, surgindo a primeira caneta (c1)
        Caneta c1 = new Caneta();

        // atribui valores a c1
        c1.cor = "Azul";
        c1.ponta = 0.5;
        c1.tampada = false;
        c1.modelo  = "Pilot Escriba Max";
        c1.carga = 90;

        c1.status(); // mostra status
        c1.tampar(); // tampa a caneta
        c1.rabiscar(); // tenta rabiscar (não consegue)
        c1.destampar(); // destampa a caneta
        c1.rabiscar(); // rabisca
        c1.tampar(); // tampa de novo


        // cria nova caneta c2
        Caneta c2 = new Caneta();
        c2.modelo = "Pilot Jones";
        c2.cor = "Preto";
        c2.destampar();

        // canetas diferentes tem comportamentos diferentes
        c1.rabiscar(); // não rabisca
        c2.rabiscar(); // rabisca
    }
}
