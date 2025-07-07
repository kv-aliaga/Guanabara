package Aula14_15;

public class Video implements AcoesVideo {
    // atributos
    private String titulo;
    private int avaliacao;
    private int qtdCurtidas;
    private boolean reproduzindo;

    // construtor
    public Video(String titulo, int qtdCurtidas, int avaliacao) {
        this.titulo = titulo;
        this.reproduzindo = false;
        this.qtdCurtidas = qtdCurtidas;
        this.avaliacao = avaliacao;
    }

    // métodos especiais
    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    public int getQtdCurtidas() {
        return qtdCurtidas;
    }
    public void setQtdCurtidas(int qtdCurtidas) {
        this.qtdCurtidas = qtdCurtidas;
    }
    public int getAvaliacao() {
        return avaliacao;
    }
    public void setAvaliacao(int avaliacao) {
        this.avaliacao = avaliacao;
    }
    public boolean isReproduzindo() {
        return reproduzindo;
    }
    public void setReproduzindo(boolean reproduzindo) {
        this.reproduzindo = reproduzindo;
    }

    // métodos
    @Override
    public void play(){
        this.reproduzindo = true;
        System.out.println("Reproduzindo\n");
    }

    @Override
    public void pause() {
        this.reproduzindo = false;
        System.out.println("Pause\n");
    }

    public void like() {
        this.qtdCurtidas ++;
        this.avaliacao += (qtdCurtidas / 100);
        System.out.println("Like!");
        System.out.println(getAvaliacao());
        System.out.println();
    }
}
