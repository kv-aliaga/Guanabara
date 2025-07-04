package Aula3.Aula3b;

public class Caneta {
    // atributos
    public String modelo;
    public String cor;
    private double ponta;
    protected int carga;
    private boolean tampada;

    // métodos
    public void rabiscar(){
        if (this.tampada){
            System.out.println("Destampe a caneta para rabiscar");
        } else{
            System.out.println("Rabiscando");
        }
    }
    public void tampar(){
        this.tampada = true;
    }
    public void destampar(){
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

