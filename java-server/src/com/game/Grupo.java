package com.game;

import java.util.ArrayList;
import java.util.List;


public class Grupo {

    List<Personagems> grupo = new ArrayList<>(5);



    public void adicionarMembro(Personagems personagem){
        grupo.add(personagem);
    }

    public void retirarMembro(Personagems personagem){
        grupo.remove(personagem);
    }



}
