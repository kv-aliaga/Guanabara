package Aula6;
// Encapsulamento: Proteção e padrão do código
// Ocultar partes da implementação, construir partes invisíveis ao mundo exterior
// Vantagens: Tornar mudanças invisíveis, facilitar a reutilização do código, reduzir efeitos colaterais
// Como encapsular: Deixar o código fácil para um possível usuário exterior;
                 // Deixar todos os atributos privados; Criar os métodos getters e setters;

// MÉTODO ABSTRATO: nada é mostrado para o usuário, logo ele é void

public class ControleRemoto{
    // ATRIBUTOS
    private int volume;
    private boolean ligado;
    private boolean tocando;

    // CONSTRUTOR
    public ControleRemoto(int volume, boolean ligado, boolean tocando){
        this.volume = volume;
        this.ligado = ligado;
        this.tocando = tocando;
    }

    // MÉTODOS GETTERS E SETTERS
    public int getVolume(){
        return this.volume;
    }
    public void setVolume(int volume){
        this.volume = volume;
    }
    public boolean getLigado(){
        return this.ligado;
    }
    public void setLigado(boolean ligado){
        this.ligado = ligado;
    }
    public boolean getTocando(){
        return this.tocando;
    }
    public void setTocando(boolean tocando){
        this.tocando = tocando;
    }

    // SOBRESCREVENDO MÉTODOS
    public void ligar(){
        setLigado(true);
    }
    public void desligar(){
        setLigado(false);
    }
    public void abrirMenu(){
        System.out.println(getLigado());
        System.out.println(getVolume());
        for (int i = 0; i < getVolume(); i += 10){
            System.out.println("I");
        }
    }
    public void fecharMenu(){
        System.out.println("Fechando menu...");
    }
    public void aumentarVolume(){
        if (getVolume() < 100){
            setVolume(getVolume() + 1);
        } else{
            setVolume(100);
        }
    }
    public void abaixarVolume(){
        if (getVolume() > 0 && getVolume() < 100){
            setVolume(getVolume() - 1);
        } else{
            setVolume(0);
        }
    }
    public void ligarMudo(){
        if (getLigado() && getVolume() > 0){
            setVolume(0);
        }
    }
    public void desligarMudo(){
        if (getLigado() && getVolume() == 0){
            setVolume(50);
        }
    }
    public void play(){
        if (getLigado() && !getTocando()){
            setTocando(true);
        }
    }
    public void pause(){
        if (getLigado() && getTocando()){
            setTocando(false);
        }
    }

    public void informacoes(){
        System.out.println("CONTROLE REMOTO");
        System.out.println("VOLUME: " + this.volume);
        System.out.println("LIGADO: " + (this.ligado ? "Sim" : "Não"));
        System.out.println("TOCANDO: " + (this.tocando ? "Sim" : "Não"));
    }
}
