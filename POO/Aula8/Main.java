package Aula8;

public class Main {
    public static void main(String[] args) {
        // instanciando lutadores
        Lutador[] lutadores = new Lutador[6];
        Luta uec1 = new Luta();

        // Pena
        Lutador prettyBoy = lutadores[0] = new Lutador("Pretty Boy", "França", 31, 1.75, 68.9, 11,  2, 1);

        // Mosca
        Lutador putscript = lutadores[1] = new Lutador("Putscript", "Brasil", 29, 1.68, 57.8, 14,  2, 3);

        // Meio-Médio
        Lutador snapsahdow = lutadores[2] = new Lutador("Snapshadow", "EUA", 35, 1.65, 80.9, 12,  2, 1);

        // Meio-Médio
        Lutador deadCode = lutadores[3] = new Lutador("Dead Code", "Austrália", 28, 1.93, 81.6, 13,  0, 2);

        // Meio-Pesado
        Lutador ufocobol = lutadores[4] = new Lutador("UFOcobol", "Brasil", 37, 1.7, 119.3, 5,  4, 3);

        // Meio-Pesado
        Lutador nerdaard = lutadores[5] = new Lutador("Nerdaard", "EUA", 30, 1.81, 105.7, 12,  2, 4);


//        LUTAS
        uec1.marcarLuta(ufocobol, nerdaard);

    }
}
