package Aula12.Subclasse.Especies;

import Aula12.Subclasse.Mamifero;

public class Cachorro extends Mamifero {

   // métodos
    public void enterrarOsso(){
        System.out.println("O cachorro enterra seu osso!");
    }
    public void abanarRabo(){
        System.out.println("O cachorro abana seu rabo!");
    }

    @Override
    public void emitirSom() {
        System.out.println("O cachorro late!");
    }
}
