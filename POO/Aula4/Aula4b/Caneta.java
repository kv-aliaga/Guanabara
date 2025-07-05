package Aula4.Aula4b;

public class Caneta {
    // atributos
    public String modelo;
    public double ponta;

    // construtor
    public Caneta(String modelo, double ponta){
        this.modelo  = modelo;
        this.ponta = ponta;
    }

    // getters e setters
    public String getModelo(){
        return this.modelo;
    }
    public void setModelo(String modelo){
        this.modelo = modelo;
    }
    public double getPonta(){
        return this.ponta;
    }
    public void setPonta(double ponta){
        this.ponta = ponta;
    }

    // outros métodos
    public void status(){
        System.out.println("SOBRE A CANETA");
        System.out.println("MODELO: " + this.modelo);
        System.out.println("PONTA: " + this.ponta);
    }
}
