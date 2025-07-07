package Aula12.Subclasse;

import Aula12.Animal;

public class Reptil extends Animal {
    // atributos
    private String corEscama;

    // métodos especiais
    public String getCorEscama() {
        return corEscama;
    }
    public void setCorEscama(String corEscama) {
        this.corEscama = corEscama;
    }

    // métodos
    @Override
    public void alimentar() {
        System.out.println("O " + getNome() + " come vegetais!");
    }

    @Override
    public void emitirSom() {
        System.out.println("O " + getNome() + " sibila!");
    }

    @Override
    public void locomover() {
        System.out.println("O " + getNome() + " rasteja!");
    }
}
