package Aula6;

public class Main {
    public static void main(String[] args) {
        // instanciando
        ControleRemoto c1 = new ControleRemoto(50, true, true);

        c1.informacoes(); // mostra as informações
        c1.desligar();
        c1.ligar();
        c1.aumentarVolume();
        c1.abaixarVolume();
        c1.ligarMudo();
        c1.abrirMenu();
        c1.informacoes();

        // odeio fazer main em poo rs
    }
}
