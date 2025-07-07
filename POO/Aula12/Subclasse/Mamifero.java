package Aula12.Subclasse;

import Aula12.Animal;

public class Mamifero extends Animal {
    // atributos
    private String corPelo;

    // métodos especiais
    public String getCorPelo() {
        return corPelo;
    }
    public void setCorPelo(String corPelo) {
        this.corPelo = corPelo;
    }

    // métodos
    @Override
    public void alimentar() {
        System.out.println("O " + getNome() + " come carne e vegetais!");
    }

    @Override
    public void emitirSom() {
        System.out.println("O " + getNome() + " emite um som!");
    }

    @Override
    public void locomover() {
        System.out.println("O " + getNome() + " caminha!");
    }
}
