package Aula13;

public class Mamifero extends Animal {
    // atributos
    protected String corPelo;

    // métodos

    @Override
    public void emitirSom() {
        System.out.println("Som de mamífero");
    }
}
