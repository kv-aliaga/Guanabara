package Aula8;

import java.util.Random;

public class Luta {
    Random rd = new Random();
//    atributos
    private Lutador desafiado; // tipo abstrato de dados, diz que um dos atributos vai ser uma instancia de outro método
    private Lutador desafiante;
    private int rounds;
    private boolean aprovada;

//    métodos especiais
    public Lutador getDesafiado(){
        return this.desafiado;
    }
    public void setDesafiado(Lutador desafiado){
        this.desafiado = desafiado;
    }
    public Lutador getDesafiante(){
        return this.desafiante;
    }
    public void setDesafiante(Lutador desafiante){
        this.desafiante = desafiante;
    }
    public int getRounds(){
        return this.rounds;
    }
    public void setRounds(int rounds){
        this.rounds = rounds;
    }
    public boolean getAprovada(){
        return this.aprovada;
    }
    public void setAprovada(boolean aprovada){
        this.aprovada = aprovada;
    }

//    métodos
    public void marcarLuta(Lutador l1, Lutador l2){
        if (l1.getCategoria() == l2.getCategoria() && l1 != l2){
            System.out.println("Luta marcada!");
            this.aprovada = true;
            desafiado = l1;
            desafiante = l2;

            lutar();
        } else{
            System.out.println("Luta não pode acontecer");
            this.aprovada = false;
            desafiado = null;
            desafiante = null;
        }
    }

    public void lutar(){
        if (aprovada){
            System.out.println(desafiado.apresentar());
            System.out.println(desafiante.apresentar());

            int vencedor = rd.nextInt(0,3);
            if (vencedor == 0){ // empate
                System.out.println("Empatou");
                desafiado.empatarLuta();
                desafiante.empatarLuta();

            } else if (vencedor == 1) { // ganhou desafiado
                System.out.println(desafiado.getNome() + " ganhou!");
                desafiado.ganharLuta();
                desafiante.perderLuta();

            } else{ // ganhou desafiante
                System.out.println(desafiante.getNome() + " ganhou!");
                desafiante.ganharLuta();
                desafiado.perderLuta();
            }
        } else{
            System.out.println("Luta não pode acontecer");
        }
    }
}
