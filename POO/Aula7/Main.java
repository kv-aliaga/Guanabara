package Aula7;

public class Main {
    public static void main(String[] args) {
        // instanciando lutadores
        Lutador[] lutadores = new Lutador[7];
        Lutador prettyBoy = lutadores[0] = new Lutador("Pretty Boy", "França", 31, 1.75, 68.9, 11,  2, 1);
        Lutador putscript = lutadores[1] = new Lutador("Putscript", "Brasil", 29, 1.68, 57.8, 14,  2, 3);
        Lutador snapsahdow = lutadores[2] = new Lutador("Snapshadow", "EUA", 35, 1.65, 80.9, 12,  2, 1);
        Lutador deadCode = lutadores[3] = new Lutador("Dead Code", "Austrália", 28, 1.93, 81.6, 13,  0, 2);
        Lutador ufocobol = lutadores[4] = new Lutador("Ufocobol", "Brasil", 37, 1.7, 119.3, 5,  4, 3);
        Lutador nerdaard = lutadores[5] = new Lutador("Nerdaard", "EUA", 30, 1.81, 105.7, 12,  2, 4);
        Lutador placeholder = lutadores[6] = new Lutador("0", "0", 0, 0, 0, 0, 0, 0);

        placeholder.definirLutaSemEmpate(putscript, prettyBoy);
        System.out.println("-=".repeat(30));
        placeholder.definirLutaSemEmpate(snapsahdow, deadCode);
        System.out.println("-=".repeat(30));
        placeholder.definirLutaSemEmpate(ufocobol, nerdaard);
    }
}
