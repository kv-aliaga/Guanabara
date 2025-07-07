package Aula12.Subclasse;

import Aula12.Animal;

public class Ave extends Animal {
    // atributos
    private String corPena;

    // métodos especiais
    public String getCorPena() {
        return corPena;
    }

    public void setCorPena(String corPena) {
        this.corPena = corPena;
    }

    // métodos
    @Override
    public void alimentar() {
        System.out.println("O " + getNome() + " come alpiste!");
    }

    @Override
    public void emitirSom() {
        System.out.println("O " + getNome() + " pia!");
    }

    @Override
    public void locomover() {
        System.out.println("O " + getNome() + " voa!");
    }

    public void fazerNinho(){
        System.out.println("O " + getNome() + " faz um ninho!");
        System.out.println("Ele está se preparando para se acasalar...");
    }
}
