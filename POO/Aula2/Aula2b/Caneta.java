package Aula2.Aula2b;
// como definir classe, instanciar objetos, mexer nos atributos e métodos, mostrando o estado atual de cada objeto

public class Caneta {
    // atributos
    String modelo;
    String cor;
    double ponta;
    int carga;
    boolean tampada;

    // métodos
    void rabiscar(){
        if (this.tampada){
            System.out.println("Destampe a caneta para rabiscar");
        } else{
            System.out.println("Rabiscando");
        }
    }
    void tampar(){
        this.tampada = true;
    }
    void destampar(){
        this.tampada = false;
    }
    void status(){
                                                // this se refere ao nome do objeto que o chamou, referência ao próprio objeto.
        System.out.printf("Caneta %s, %s caneta\n", this.cor, this.cor);
        System.out.println("Está tampada? " + this.tampada);
        System.out.println("O modelo é:  " + this.modelo);
        System.out.println("A ponta é: " + this.ponta);
        System.out.println("A carga esta: " + this.carga + "% cheia");
    }
}
