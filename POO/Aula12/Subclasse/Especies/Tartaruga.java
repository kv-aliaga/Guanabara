package Aula12.Subclasse.Especies;

import Aula12.Subclasse.Reptil;

public class Tartaruga extends Reptil {
    // métodos
    public void locomover() {
        for (int i = 0; i < 11; i++) {
            // Limpa a linha anterior e imprime a nova
            System.out.print("\rA tartaruga demora " + i + " segundos para caminhar");

            try {
                Thread.sleep(1000); // Pausa de 1 segundo entre as iterações
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }


    @Override
    public void emitirSom() {
        System.out.println("A tartaruga não emite sons");
    }
}
