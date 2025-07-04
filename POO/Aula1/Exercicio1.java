package Aula1;
// Cria uma classe para algo físico
//  Tema: Celular

public class Exercicio1 {
    // atributos
    int pctBateria;
    int pctBrilho;
    int qtdApps;
    boolean ligado;
    boolean temInternet;
    String modelo;

    // métodos
    public int carregar(int pctAumento){
        return pctBateria += pctAumento;
    }
    public int descarregar(int pctDiminui){
        return pctBateria -= pctDiminui;
    }
    public int aumentarBrilho(int pctAumento){
        return pctBrilho += pctAumento;
    }
    public int diminuirBrilho(int pctDiminui){
        return pctBrilho -= pctDiminui;
    }
    public int instalarApp(){
        return qtdApps++;
    }
    public int desinstlarApp(){
        return qtdApps --;
    }
    public boolean ligar(){
        return ligado = true;
    }
    public boolean desligar(){
        return ligado = false;
    }
    public boolean ligarInternet(){
        return temInternet = true;
    }
    public boolean desligarInternet(){
        return temInternet = false;
    }
}
