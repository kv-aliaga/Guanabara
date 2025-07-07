package Aula13;

public class Cachorro extends Lobo{
    @Override
    public void emitirSom() {
        System.out.println("Au! Au! Au!");
    }

    public void reagir(String frase){
        if (frase.equals("Toma comida") || frase.equals(getNome())){
            System.out.println("Abanar e latir");
        } else{
            System.out.println("Rosnar");
        }
    }
    public void reagir(int hora){
        if (hora < 12){
            System.out.println("Latir");
        } else if (hora < 18) {
            System.out.println("Abanar rabo");
        } else{
            System.out.println("Rosna");
        }
    }
    public void reagir(boolean dono){
        if (dono){
            System.out.println("Late e abana o rabo");
        } else{
            System.out.println("Rosna");
        }
    }
    public void reagir(int idade, double peso){
        if (idade < 5){
            if (peso < 25){
                System.out.println("Abanar");
            } else{
                System.out.println("Latir");
            }
        } else{
            if (peso < 50){
                System.out.println("Abanar");
            } else{
                System.out.println("Latir");
            }
        }
    }
}
