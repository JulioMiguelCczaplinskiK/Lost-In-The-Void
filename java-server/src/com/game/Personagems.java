package com.game;

public class Personagems extends Grupo{

    private String nome;
    private int vida;
    private int dano;

    private Classes classe;
    private Status status;


    public Personagems(String nome, Classes classe, Status status){
        this.nome = nome;
        this.classe = classe;
        this.status = status;
    }


    public void BaterComPunhos(){

    }

    public void BaterComArma(){

    }

    /// bolqueio
    public void defenderComBracos(){

    }

    /// escudar
    public void defenderComArma(){

    }








    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }

    public int getDano() {
        return dano;
    }

    public void setDano(int dano) {
        this.dano = dano;
    }
}
