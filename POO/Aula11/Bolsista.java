package Aula11;

public class Bolsista extends Aluno{
//    atributos
    private double bolsa;

//    método
    public double getBolsa() {
        return bolsa;
    }
    public void setBolsa(double bolsa) {
        this.bolsa = bolsa;
    }

    public void pagarMensalidade(double bolsa){
        double mensalidade = 2000;
        mensalidade -= bolsa;
        System.out.println("Mensalidade de R$" + mensalidade + " paga");
    }

    public void renovarBolsa(){
        System.out.println("Bolsa renovada!");
    }
}
