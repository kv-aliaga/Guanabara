package Aula5;
// exemplos práticos com objetos

import java.util.Scanner;

public class Aula5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ContaBanco c1 = new ContaBanco("Jones");

        // entrada de dados
        System.out.print("Digite o tipo da sua conta (CC para Conta Corrente e CP para Conta Poupança): ");
        c1.abrirConta(input.nextLine()); // abre a conta

        // saída de dados
        c1.informacoes(); // mostra as informações
        c1.depositar(500);
        c1.sacar(10000); // saque impossível
        c1.sacar(100);
        c1.pagarMensalidade(); // paga mensalidade
        c1.sacar(448);
        c1.fecharConta();
        c1.depositar(10); // depósito impossível
        c1.informacoes();
    }
}
