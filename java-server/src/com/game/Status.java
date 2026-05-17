package com.game;

public class Status{

    private int vitalidade;
    private int forca;
    private int danoCritico;
    private float chanceCritica;
    private int resistencia;
    private int tolerancia;
    private int percepcao;
    private int agilidade;
    private int sorte;
    private int energia;
    private int mente;
    private int sabedoria;

    public Status(){
        vitalidade = 2;
        forca = 2;
        danoCritico = 2;
        chanceCritica = 2;
        resistencia = 2;
        tolerancia = 2;
        percepcao = 2;
        agilidade = 2;
        sorte = 2;
        energia = 2;
        mente = 2;
        sabedoria = 2;
    }

    public int getVida() {
        return vitalidade;
    }

    public void setVida(int vida) {
        this.vitalidade = vida;
    }

    public int getDano() {
        return forca;
    }

    public void setDano(int dano) {
        this.forca = dano;
    }

    public int getDanoCritico() {
        return danoCritico;
    }

    public void setDanoCritico(int danoCritico) {
        this.danoCritico = danoCritico;
    }

    public float getChanceCritica() {
        return chanceCritica;
    }

    public void setChanceCritica(float chanceCritica) {
        this.chanceCritica = chanceCritica;
    }

    public int getResistencia() {
        return resistencia;
    }

    public void setResistencia(int resistencia) {
        this.resistencia = resistencia;
    }

    public int getTolerancia() {
        return tolerancia;
    }

    public void setTolerancia(int tolerancia) {
        this.tolerancia = tolerancia;
    }

    public int getPercepcao() {
        return percepcao;
    }

    public void setPercepcao(int percepcao) {
        this.percepcao = percepcao;
    }

    public int getAgilidade() {
        return agilidade;
    }

    public void setAgilidade(int agilidade) {
        this.agilidade = agilidade;
    }

    public int getSorte() {
        return sorte;
    }

    public void setSorte(int sorte) {
        this.sorte = sorte;
    }

    public int getEnergia() {
        return energia;
    }

    public void setEnergia(int energia) {
        this.energia = energia;
    }

    public int getMente() {
        return mente;
    }

    public void setMente(int mente) {
        this.mente = mente;
    }

    public int getSabedoria() {
        return sabedoria;
    }

    public void setSabedoria(int sabedoria) {
        this.sabedoria = sabedoria;
    }





}
