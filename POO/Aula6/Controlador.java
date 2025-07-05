package Aula6;

public interface Controlador {
    // MÉTODOS
    public abstract void ligar(); // public abstract é redundante, mas serve para fixar. Também, o abstract é muito necessário para uma interface
    public abstract void desligar();
    public abstract void abrirMenu();
    public abstract void fecharMenu();
    public abstract void aumentarVolume();
    public abstract void abaixarVolume();
    public abstract void ligarMudo();
    public abstract void desligarMudo();
    public abstract void play();
    public abstract void pause();
}
