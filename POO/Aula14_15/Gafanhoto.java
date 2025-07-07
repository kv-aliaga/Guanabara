package Aula14_15;

public class Gafanhoto extends Pessoa{
    // atributos
    private String login;
    private int totalAssistido;

    // métodos especiais

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public int getTotalAssistido() {
        return totalAssistido;
    }

    public void setTotalAssistido(int totalAssistido) {
        this.totalAssistido = totalAssistido;
    }

    // métodos
    public void viuMaisUm(){
        this.totalAssistido ++;
    }
}
