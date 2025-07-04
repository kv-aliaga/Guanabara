package Aula3.Aula3a;
// visibilidade de objetos
/*
    + > público, classe atual e todas as outras classes podem ter acesso a elas (exemplo, orelhão)
    - > privado, somente a classe atual pode usar ela (exemplo, celular pessoal)
    # > protegido, somente a classe atual e suas subclasses podem usar (exemplo, celular de casa)
*/

public class Caneta {

    // atributos
    public String modelo; // qualquer classe pode mexer
    public String cor;
    private double ponta; // só Caneta pode mexer
    protected int carga;
    protected boolean tampada; // só Caneta e suas subclasses podem mexer (isso não inclui Aula3)

    // métodos
    public void rabiscar(){
        if (this.tampada){
            System.out.println("Destampe a caneta para rabiscar");
        } else{
            System.out.println("Rabiscando");
        }
    }
}
