package Aula5;
// REQUISITOS:
// tipo = CC (corrente) e CP poupança)
// qnd abrir conta perguntar tipo, se cc + R$50, se cp + R$150
// se conta aberta: status, senão !status
// se fechar, saldo precisa = 0
// sacar (precisa ser <= saldo) e depositar só se conta estiver aberta
// mensalidade (cc = 12) (cp = 20)
// construtor: status = false, saldo = 0

import java.util.Random;

public class ContaBanco {
    Random rd = new Random();

    // atributos
    public int numConta;
    protected String tipo;
    private String dono;
    private double saldo;
    private boolean status;

    //construtor
    public ContaBanco(String dono){
        this.numConta = rd.nextInt(100000, 999999);
        this.saldo = 0;
        this.status = false;
        this.dono = dono;
    }

    // métodos getters e setters
    public int getNumConta(){
        return this.numConta;
    }
    public void setNumConta(int numConta){
        this.numConta = numConta;
    }
    public String getTipo(){
        return this.tipo;
    }
    public void setTipo(String tipo){
        this.tipo = tipo;
    }
    public String getDono(){
        return this.dono;
    }
    public void setDono(String dono){
        this.dono = dono;
    }
    public double getSaldo(){
        return this.saldo;
    }
    public void setSaldo(double saldo){
        this.saldo = saldo;
    }
    public boolean getStatus(){
        return this.status;
    }
    public void setStatus(boolean status){
        this.status = status;
    }

    // métodos
    public void abrirConta(String tipo){
        this.status = true;
        this.tipo = tipo;

        if (this.tipo.equals("CC")){
            saldo += 50;
        } else{
            saldo += 150;
        }
    }

    public void fecharConta(){
        if (saldo == 0){
            status = false;
            System.out.println("Conta fechada com sucesso!");
        } else{
            System.out.println("\nA conta não pode ser fechada até o saldo da conta ser igual a R$0.00");
        }
    }

    public double depositar(double quantia){
        if (this.status){
            return this.saldo += quantia;
        } else{
            return 0;
        }
    }

    public void sacar(double quantia){
        if (this.saldo < quantia){
            System.out.printf("O saque de R$%.2f não pode ser feito\n", quantia);
            System.out.printf("\nSeu saldo é de R$%.2f", this.saldo);
        } else{
            saldo -= quantia;
        }
    }

    public void pagarMensalidade(){
        if (this.tipo.equals("CC")){
            saldo -= 12;
        } else{
            saldo -= 20;
        }
    }

    public void informacoes(){
        System.out.println("\nCONTA");
        System.out.println("Número da conta: " + this.numConta);
        System.out.println("Tipo da conta: " + (this.tipo.equals("CC") ? "Conta Corrente" : "Conta Poupança"));
        System.out.println("Dono: " + this.dono);
        System.out.println("Saldo: R$" + saldo);
        System.out.println("Status da conta: " + (this.status ? "Aberta" : "Fechada"));
        System.out.println();
    }
}
