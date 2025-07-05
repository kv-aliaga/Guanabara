package Aula8;

public class Lutador extends Luta {
    // atributos
    private String nome;
    private String nacionalidade;
    private int idade;
    private double altura;
    private double peso;
    private String categoria;
    private int vitorias;
    private int derrotas;
    private int empates;

    // construtor
    public Lutador(String nome, String nacionalidade, int idade, double altura, double peso, int vitorias, int derrotas, int empates){
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.idade = idade;
        this.altura = altura;
        this.peso = peso;
        this.categoria = categorizar(this.peso);
        this.vitorias = vitorias;
        this.derrotas = derrotas;
        this.empates = empates;
    }

    // métodos getters e setters
    public String getNome(){
        return this.nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNacionalidade(){
        return this.nacionalidade;
    }
    public void setNacionalidade(String nacionalidade){
        this.nacionalidade = nacionalidade;
    }
    public int getIdade(){
        return this.idade;
    }
    public void setIdade(int idade){
        this.idade = idade;
    }
    public double getAltura(){
        return this.altura;
    }
    public void setAltura(double altura){
        this.altura = altura;
    }
    public double getPeso(){
        return this.peso;
    }
    public void setPeso(double peso){
        this.peso = peso;
    }
    public int getVitorias(){
        return this.vitorias;
    }
    public int getDerrotas(){
        return this.derrotas;
    }
    public int getEmpates(){
        return this.empates;
    }
    public String getCategoria(){
        return this.categoria;
    }

    // métodos
    public String categorizar(double peso){
        if (peso >= 120.2 || peso <= 50) {
            return "Não permitido";
        } else if (peso >= 93) {
            return "Meio-Pesado";
        } else if (peso >= 83.9) {
            return "Médio";
        } else if (peso >= 77.1) {
            return "Meio-Médio";
        } else if (peso >= 70.3) {
            return "Leve";
        } else if (peso >= 65.8) {
            return "Pena";
        } else if (peso >= 61.2) {
            return "Galo";
        } else if (peso >= 56.7) {
            return "Mosca";
        } else{
            return "Não permitido";
        }
    }
    public String apresentar(){
        return this.nome + "! Com " + this.peso + "kg, peso " + this.categoria + ", " + this.vitorias + " vitórias! " + this.derrotas + " derrotas! e " + this.empates + " empates!";
    }
    public void ganharLuta(){
        this.vitorias += 1;
    }
    public void perderLuta(){
        this.derrotas += 1;
    }
    public void empatarLuta(){
        this.empates += 1;
    }

    public void status(){
        System.out.printf("\n\n==== LUTADOR %s ====\n", this.nome.toUpperCase());
        System.out.println("Nome: " + this.nome);
        System.out.println("Nacionalidade: " + this.nacionalidade);
        System.out.println("Idade: " + this.idade);
        System.out.println("Altura: " + this.altura);
        System.out.println("Peso: " + this.peso);
        System.out.println("Categoria: " + this.categoria);
        System.out.println("Vitórias: " + this.vitorias);
        System.out.println("Derrotas: " + this.derrotas);
        System.out.println("Empates: " + this.empates);
    }

    public void definirLutaSemEmpate(Lutador vencedor, Lutador perdedor){
//        iniciando apresentações
        System.out.println(vencedor.apresentar());
        System.out.println(perdedor.apresentar());
        System.out.println();

//        fim da luta
        vencedor.ganharLuta();
        perdedor.perderLuta();

        vencedor.status();
        perdedor.status();
    }
}
