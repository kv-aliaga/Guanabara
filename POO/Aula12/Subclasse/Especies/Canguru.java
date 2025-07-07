package Aula12.Subclasse.Especies;

import Aula12.Subclasse.Mamifero;

public class Canguru extends Mamifero {
    // métodos
    public void usarBolsa(){
        System.out.println("O canguru usa sua bolsa para carregar seu filho");
    }

    // sobrescrição
    @Override
    public void locomover() {
        System.out.println("O canguru salta");
    }
}
