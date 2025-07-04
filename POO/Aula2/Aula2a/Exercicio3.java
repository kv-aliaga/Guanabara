package Aula2.Aula2a;
// Cria uma classe para algo não material
//  Tema: Corrida

public class Exercicio3 {
    int kmTemp;
    int kmTotal;
    double caloriasPerdidas;
    String modalidade;

    public int perderCalorias(){
        for (int i = 0; i < kmTemp; i ++){
            if (modalidade == "Corrida"){
                caloriasPerdidas += 90;
            } else if (modalidade == "Caminhada"){
                caloriasPerdidas += 50;
            } else{
                caloriasPerdidas += 70;
            }
        }
        return kmTemp;
    }
    public int andarMais(int km) {
        kmTemp += km;
        perderCalorias();
        return kmTotal = kmTemp;
    }
}
