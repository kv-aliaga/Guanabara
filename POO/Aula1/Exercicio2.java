package Aula1;
// Cria uma classe para algo físico
//  Tema: Ventilador

public class Exercicio2 {
    // atributos
    boolean ligado;
    boolean movimento;
    String modelo;
    int watts;
    int potencia;

    // métodos
    public boolean ligar(){
        return ligado;
    }
    public boolean desligar(){
        return !ligado;
    }
    public boolean ativarMovimento(){
        return movimento;
    }
    public boolean desativarMovimento(){
        return !movimento;
    }
    public int mudarPotencia(int escolha){
        if (escolha == 0){
            desligar();
        } else{
            potencia = escolha;
        }
        return potencia;
    }
}
