package Aula12;

import Aula12.Subclasse.Especies.*;

public class Aula12 {
    public static void main(String[] args) {
        // objetos
        Arara a1 = new Arara();
        Cachorro ch1 = new Cachorro();
        Canguru cg1 = new Canguru();
        Cobra co1 = new Cobra();
        PeixeDourado p1 = new PeixeDourado();
        Tartaruga t1 = new Tartaruga();

        // atribuindo valores
        a1.setNome("Arara");
        a1.setQtdMembros(2);
        a1.setCorPena("Verde");
        a1.fazerNinho();

        System.out.println();

        ch1.setNome("Cachorro");
        ch1.setQtdMembros(4);
        ch1.setCorPelo("Marrom");
        ch1.abanarRabo();
        ch1.emitirSom();

        System.out.println();

        cg1.setNome("Canguru");
        cg1.setQtdMembros(4);
        cg1.setCorPelo("Marrom");
        cg1.locomover();

        System.out.println();

        co1.setNome("Cobra");
        co1.setCorEscama("Verde");
        co1.setQtdMembros(1);
        co1.emitirSom();

        System.out.println();

        p1.setNome("Peixe Dourado");
        p1.setQtdMembros(1);
        p1.setCorEscama("Dourado");
        p1.soltarBolha();

        System.out.println();

        t1.setNome("Tartaruga");
        t1.setCorEscama("Verde");
        t1.emitirSom();
        t1.locomover();
    }
}
