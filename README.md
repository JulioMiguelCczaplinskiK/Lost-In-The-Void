# Lost In The Void — rpg de turno 

```text
    _,_
  /7/Y/^\
  vuVV|C)|                        __ _
    \|^ /                       .'  Y '>,
    )| \)                      / _   _   \
   //)|\\                      )(_) (_)(|}
  / ^| \ \                     {  4A   } /
 //^| || \\                     \uLuJJ/\l
>//||| |\\\|                    |3    p)/
| """""  7/>l__ _____ ____      /nnm_n//
L>_   _-< 7/|_-__,__-)\,__)(".  \_>-<_/D
)D" Y "c)  9)       //V     \_"-._.__G G_c__.-__<"/ ( \
 | | |  |(|               < "-._"> _.G_.___)\   \7\
  \"=" // |              (,"-.__.|\ \<.__.-" )   \ \
   '---'  |              |,"-.__"| \!"-.__.-".\   \ \
     |_;._/              (_"-.__"'\ \"-.__.-".|    \_\
     )(" V                \"-.__"'|\ \-.__.-".)     \ \
        (                  "-.__'"\_\ \.__.-"./      \ l
         )                  ".__"">>G\ \__.-">        V )
                                ""  G<\ \_.-"        ./7
                                     G<\ \          ///
                                ___  GD'
```

> RPG de turno com estética retrô e interface ASCII no terminal.

**Lost In The Void** é um projeto experimental que combina RPG por turnos, exploração em masmorras e ambientação dark fantasy. O objetivo é criar uma experiência de descoberta, dificuldade e imersão em um jogo de terminal.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Java](https://img.shields.io/badge/Java-17-orange?logo=java&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

---

## 📌 Índice

- [Visão Geral](#-visão-geral)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Arquitetura do Projeto](#-arquitetura-do-projeto)
- [Estrutura de Pastas](#-estrutura-de-pastas)
- [Como Executar](#-como-executar)
- [Status Atual](#-status-atual)
- [Próximos Passos](#-próximos-passos)
- [Como Contribuir](#-como-contribuir)
- [Autor](#-autor)

---

## 📖 Visão Geral

Lost In The Void é um RPG com foco em:

- direção de arte retrô em terminal,
- progressão por níveis de masmorra,
- combate por turnos,
- sensação de risco e descoberta.

O jogo é construído como um sistema cliente/servidor:

- o **cliente** em Python gerencia a entrada do jogador e a renderização em terminal usando `curses`;
- o **servidor** em Java recebe comandos via socket TCP, aplica a lógica do jogo e responde com resultados.

A experiência é pensada para ser simples no visual, mas cheia de possibilidades em mecânicas e estado de jogo.

---

## 🚀 Tecnologias Utilizadas

- **Java** (backend)
  - `java.net.ServerSocket`
  - classes de rede, leitura de streams e lógica de jogo
- **Python** (frontend)
  - `socket` para comunicação TCP
  - `curses` para interface de terminal
- **ASCII / terminal**
  - interface baseada em texto, com foco em ambientes de terminal/console

> Observação: A arquitetura é voltada para Java + Python.

---

## 🧱 Arquitetura do Projeto

O projeto está dividido em dois módulos principais:

- `java-server/`: código do servidor Java que aceita conexões TCP na porta `5000` e processa comandos.
- `python-client/`: código do cliente Python que se conecta ao servidor, envia comandos e exibe a interface no terminal.

Há também um diretório `protocol/` reservado para definições de comunicação futuras.

---

## 📂 Estrutura de Pastas

### Backend

```text
java-server/
├── src/
│   ├── com/
│   │   ├── game/
│   │   │   ├── Cavaleiro.java
│   │   │   ├── Classes.java
│   │   │   ├── Grupo.java
│   │   │   ├── Main.java
│   │   │   ├── Personagems.java
│   │   │   └── Status.java
│   │   └── network/
│   │       └── CriarServer.java
└── src.iml
```

### Frontend

```text
python-client/
├── input/
├── network/
│   └── EntrarServidor.py
├── render/
│   └── index.py
└── state/
```

---

## ▶️ Como Executar

### 1. Iniciar o servidor Java

1. Abra um terminal em `java-server/src`.
2. Compile o servidor Java com `javac`.

### 2. Iniciar o cliente Python

1. Abra outro terminal em `python-client`.
2. Execute `python python-client/render/index.py`.

O servidor abre na porta `5000` e aguarda a conexão do cliente.
O cliente tenta se conectar em `localhost:5000` e envia um comando de teste.

> Certifique-se de ter Python 3 instalado. O módulo `curses` é usado para a interface de terminal.

---

## 🚧 Status Atual

Atualmente o projeto está em desenvolvimento. O servidor Java já implementa uma conexão TCP básica e o cliente Python consegue enviar mensagens ao servidor.

O fluxo de rede está funcionando como protótipo, mas ainda faltam elementos importantes como:

- lógica completa de combate por turnos;
- gerenciamento de múltiplos estados de jogo;
- interface de jogo completa;
- persistência ou salvamento de progresso.

---

## 🔄 Fluxo da Aplicação

O ciclo de funcionamento segue, de forma geral, as etapas abaixo:

1. **Interação do jogador:** o jogador pressiona uma tecla ou executa uma ação no terminal (ex: mover, atacar, abrir inventário).
2. **Envio da ação:** o cliente em Python captura o input e envia uma mensagem JSON via socket TCP para o servidor Java.
3. **Processamento no servidor (Java):** o servidor recebe a mensagem, interpreta o tipo (MOVE, ATTACK, etc.), valida a ação de acordo com as regras do jogo e atualiza o estado interno (engine).
4. **Geração da resposta:** o servidor cria uma ou mais mensagens JSON com o novo estado do jogo ou eventos (ex: GAME_STATE, ENTITY_MOVED, DAMAGE).
5. **Retorno ao cliente::** essas mensagens são enviadas de volta ao cliente Python via socket.
6. **Atualização da interface:** o cliente processa as mensagens recebidas, atualiza o estado local e redesenha a interface usando curses, sem reiniciar o programa.

Esse fluxo permite uma separação clara de responsabilidades entre cliente, servidor e permite a interacao de mais de um jogador.

---

## 🤝 Como Contribuir

### Programacao
1. Faça um fork do projeto.
2. Crie uma branch com a sua melhoria.
3. Abra um pull request descrevendo o objetivo.

### Arte
> Atualmente, o projeto utiliza artes ASCII gratuitas, pois não há produção própria nessa área. Caso você tenha habilidades com desenho em ASCII, colaborações serão muito bem-vindas.

### Ideias
> Sugestões de conteúdo como: items, habilidades, poderes, magias, mecanicas... quanto mais customizacoes suas ideia tiver melhor.

#### Contribuições são bem-vindas, especialmente em:

- lógica de jogo;
- rede e protocolo;
- interface de terminal;
- documentação.

---

## ✍️ Autor
```text
                                             _______________________
   _______________________-------------------                       `\
 /:--__                                                              |
||< > |                                   ___________________________/
| \__/_________________-------------------                         |
|                                                                  |
 |                      Projeto desenvolvido por:                  |
 |                                                                  |
 |                          Julio Miguel C.K.                       |
  |                                                                  |
  |                                                                  |
  |                                                                  |
  |                                                                   |
   |                                                                  |
   |                                                                  |
   |                      Instagram: @theone_lio                     |
  |                                              ____________________|_
  |  ___________________-------------------------                      `\
  |/`--_                                                                 |
  ||[ ]||                                            ___________________/
   \===/___________________--------------------------
```
