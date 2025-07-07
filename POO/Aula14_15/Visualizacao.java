package Aula14_15;

public class Visualizacao {
    // atributos
    private Gafanhoto espectador;
    private Video filme;

    // métodos
    public Gafanhoto getEspectador() {
        return espectador;
    }

    public void setEspectador(Gafanhoto espectador) {
        this.espectador = espectador;
    }

    public Video getFilme() {
        return filme;
    }

    public void setFilme(Video filme) {
        this.filme = filme;
    }

    // métodos
    public void avaliar(){
        this.filme.like();
    }

    public void avaliar(int nota){
        this.filme.setAvaliacao(nota);
    }

    public void avaliar(int nota10, int porcentagem){
        porcentagem = nota10 / porcentagem;
        this.filme.setAvaliacao(porcentagem);
    }
}
