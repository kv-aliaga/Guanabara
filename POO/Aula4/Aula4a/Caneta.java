package Aula4.Aula4a;

public class Caneta {
    // ========== Atributos ==========
    public String modelo;
    public String cor;
    private double ponta;
    protected int carga;
    private boolean tampada;

    // ========== Construtor ==========
    public Caneta(String modelo, String cor, double ponta){
        this.modelo = modelo; // deixa que modelo, cor e ponta seja escolhido pelo usuário
        this.cor = cor;
        setPonta(ponta); // faz o mesmo de outra forma
        this.carga = 100; // deixa que carga seja sempre 100%
        tampar(); // deixa que a caneta comece tampada
    }

    // ========== Métodos ==========
    public void rabiscar() {
        if (this.tampada) {
            System.out.println("Destampe a caneta para rabiscar");
        } else {
            System.out.println("Rabiscando");
        }
    }

    public void tampar() {
        this.tampada = true;
    }

    public void destampar() {
        this.tampada = false;
    }

    public void status() {
        System.out.println("\n=== Status da Caneta ===");
        System.out.printf("Modelo: %s\n", this.modelo);
        System.out.printf("Cor: %s\n", this.cor);
        System.out.printf("Ponta: %.2f\n", this.ponta);
        System.out.printf("Carga: %d%%\n", this.carga);
        System.out.println("Tampada: " + (this.tampada ? "Sim" : "Não"));
    }

    // ========== Getters e Setters ==========
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
}