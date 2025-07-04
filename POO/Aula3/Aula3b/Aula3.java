package Aula3.Aula3b;

public class Aula3 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();

        c1.cor = "Azul";
        c1.modelo = "BIC Jones";
//      c1.ponta = 0,5; → não pode acessar porque é private
        c1.carga = 80; // pode acessar porque é protected e está na mesma package

//      c1.tampada = false; → tampada é private mas destampar() e tampar() podem ser utilizados para modificar ela, já que estes métodos são públicos

        c1.rabiscar();
        c1.status();
    }
}