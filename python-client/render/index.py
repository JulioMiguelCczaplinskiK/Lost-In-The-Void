
# Projeto: Lost in the Void - Jogo de Aventura em Terminal
# Descrição: Cliente Python para renderização de interface em terminal usando curses.
# Autor: [Julio Miguel C.K.]


# Importações necessárias
import curses
from curses import wrapper
import sys
import os
from pathlib import Path
import subprocess
import time
import threading









def safe_addstr(win, y, x, text, attr=0):
    if text is None:
        text = ""
    try:
        max_y, max_x = win.getmaxyx()
        if y < 0 or y >= max_y or x < 0 or x >= max_x:
            return
        text = str(text)
        max_len = max_x - x
        if max_len <= 0:
            return
        win.addstr(y, x, text[:max_len], attr)
    except curses.error:
        pass

# -------------------------------------------





def DesenharLayout(stdscr):

    # limpa tela
    stdscr.clear()
    
    # Variaveis iniciais
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    global SCREEN_BORDER_COLOR
    SCREEN_BORDER_COLOR = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    global ENEMY_COLOR
    ENEMY_COLOR = curses.color_pair(2)

    # Configuracoes iniciais da tela

    global alturaTela
    global larguraTela  
    global tercoTela

    alturaTela = 0
    larguraTela = 0

    alturaTela, larguraTela = stdscr.getmaxyx()
    alturaTela -= 1
    larguraTela -= 2

    tercoTela = larguraTela // 3


    alturaMenu = tercoTela
    larguraMenu = tercoTela


    global opcoes
    opcoes = ["Conectar ao servidor", "Configurações", "Sair"]

    # CRIAR BACKGROUND 
    stdscr.addstr(0, 0, "┌", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, 0, "└", SCREEN_BORDER_COLOR)
    stdscr.addstr(0, larguraTela, "┐", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, larguraTela, "┘", SCREEN_BORDER_COLOR)

    
    i = 1
    while i < alturaTela:
        stdscr.addstr(i, 0, "│", SCREEN_BORDER_COLOR)
        stdscr.addstr(i, larguraTela, "│", SCREEN_BORDER_COLOR)
        i += 1
    
    
    i = 1
    while i < larguraTela:
        stdscr.addstr(0, i, "─", SCREEN_BORDER_COLOR)
        stdscr.addstr(alturaTela, i, "─", SCREEN_BORDER_COLOR)
        i += 1
    
    alturaTela -= 1
    larguraTela -= 2




    # adiciona os paineis

    # painel esquerda
    stdscr.addstr(1, 1, "┌", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, 1, "└", SCREEN_BORDER_COLOR)
    stdscr.addstr(1, tercoTela, "┐", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, tercoTela, "┘", SCREEN_BORDER_COLOR)

    i = 2
    while i < alturaTela:
        stdscr.addstr(i, 1, "│", SCREEN_BORDER_COLOR)
        stdscr.addstr(i, tercoTela, "│", SCREEN_BORDER_COLOR)
        i += 1
    


    i = 2
    while i < tercoTela:
        stdscr.addstr(1, i, "─", SCREEN_BORDER_COLOR)
        stdscr.addstr(alturaTela, i, "─", SCREEN_BORDER_COLOR)
        i += 1





    # painel direita

    stdscr.addstr(1, tercoTela * 2, "┌", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, tercoTela * 2, "└", SCREEN_BORDER_COLOR)
    stdscr.addstr(1, larguraTela, "┐", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, larguraTela, "┘", SCREEN_BORDER_COLOR)
            

    i = 2
    while i < alturaTela:
        stdscr.addstr(i, tercoTela * 2, "│", SCREEN_BORDER_COLOR)
        stdscr.addstr(i, larguraTela, "│", SCREEN_BORDER_COLOR)
        i += 1
    


    i = tercoTela * 2 +1
    while i < larguraTela:
        stdscr.addstr(1, i, "─", SCREEN_BORDER_COLOR)
        stdscr.addstr(alturaTela, i, "─", SCREEN_BORDER_COLOR)
        i += 1





    # painel meio-cima

    alturaTela = alturaTela // 2
    
    stdscr.addstr(1, tercoTela + 1, "┌", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, tercoTela + 1, "└", SCREEN_BORDER_COLOR)
    stdscr.addstr(1, tercoTela * 2 - 1, "┐", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela, tercoTela * 2 - 1, "┘", SCREEN_BORDER_COLOR)

    i = 2
    while i < alturaTela:
        stdscr.addstr(i, tercoTela + 1, "│", SCREEN_BORDER_COLOR)
        stdscr.addstr(i, tercoTela * 2 -1, "│", SCREEN_BORDER_COLOR)
        i += 1
    


    i = tercoTela + 2
    while i < tercoTela * 2 - 1:
        stdscr.addstr(1, i, "─", SCREEN_BORDER_COLOR)
        stdscr.addstr(alturaTela, i, "─", SCREEN_BORDER_COLOR)
        i += 1





    # painel meio-baixo
    
    stdscr.addstr(alturaTela + 1, tercoTela + 1, "┌", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela * 2 + 1, tercoTela + 1, "└", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela + 1, tercoTela * 2 - 1, "┐", SCREEN_BORDER_COLOR)
    stdscr.addstr(alturaTela * 2 + 1, tercoTela * 2 - 1, "┘", SCREEN_BORDER_COLOR)


    i = alturaTela + 2 
    while i < alturaTela * 2 + 1:
        stdscr.addstr(i, tercoTela + 1, "│", SCREEN_BORDER_COLOR)
        stdscr.addstr(i, tercoTela * 2 -1, "│", SCREEN_BORDER_COLOR)
        i += 1
    


    i = tercoTela + 2
    while i < tercoTela * 2 - 1:
        stdscr.addstr(alturaTela + 1, i, "─", SCREEN_BORDER_COLOR)
        stdscr.addstr(alturaTela *2 + 1, i, "─", SCREEN_BORDER_COLOR)
        i += 1

    # Cria as janelas para cada painel
    color = SCREEN_BORDER_COLOR


    global janelaEsquerda
    global janelaDireita
    global janelaMeioCima
    global janelaMeioBaixo

    global larguraTelaMeioCima
    global alturaTelaMeioCima
    
    

    janelaEsquerda = curses.newwin(alturaTela * 2 - 1, tercoTela - 3, 2, 3)
    alturaTelaEsquerda, larguraTelaEsquerda = janelaEsquerda.getmaxyx()


    janelaDireita = curses.newwin(alturaTela * 2 - 1, tercoTela - 2, 2, tercoTela * 2 + 2)
    alturaTelaDireita, larguraTelaDireita = janelaDireita.getmaxyx()


    janelaMeioCima = curses.newwin(alturaTela - 2, tercoTela - 4, 2, tercoTela + 3)
    alturaTelaMeioCima, larguraTelaMeioCima = janelaMeioCima.getmaxyx()


    janelaMeioBaixo = curses.newwin(alturaTela - 1, tercoTela - 4, alturaTela + 2, tercoTela + 3)
    alturaTelaMeioBaixo, larguraTelaMeioBaixo = janelaMeioBaixo.getmaxyx()

    
    


def MostrarEventos(stdscr):

    # Arte ASCII com espaços de indentação no início (comum ao copiar de IDEs)
    arte_bruta = r"""
    ⠀/\_/\
    ( o.o )
    ⠀> ^ <
    """

    pergaminho = r"""
    ⠀__________________________
    /⠀\⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\.
    |⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    \_⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|.
    ⠀⠀⠀⠀|⠀⠀⠀_____________________|___
    ⠀⠀⠀⠀|⠀⠀/⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀/.
    ⠀⠀⠀⠀\_/dc______________________/.
    """

    morte = r"""
                                         .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. \
                |    |:::||             //'///                    `.\
                |    |:::||            //  ||'                      `|
        jgs     /    |:::|/        _,-//\  ||
        hh     /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\` /`                    |             // 
     |`                     \            ||  
    /                        |           //  
  /`                          \         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`
"""



    
    # Remove apenas a indentação comum, mantendo os espaços relativos do desenho
    linhas_raw = morte.splitlines()
    
    # Encontra a indentação mínima (espaços no início)
    min_indent = float('inf')
    for linha in linhas_raw:
        if linha.strip():  # Se a linha não está vazia
            indent = len(linha) - len(linha.lstrip())
            min_indent = min(min_indent, indent)
    
    if min_indent == float('inf'):
        min_indent = 0
    
    # Remove apenas a indentação comum de todas as linhas
    linhas = [linha[min_indent:] if len(linha) > min_indent else linha for linha in linhas_raw]

    # Centraliza horizontalmente E verticalmente na janela (adapta a desenhos maiores)
    largura_disponivel = larguraTelaMeioCima
    altura_disponivel = alturaTelaMeioCima
    
    maior_linha = max(len(linha) for linha in linhas) if linhas else 0
    num_linhas = len(linhas)
    
    # Se o desenho for maior que a janela, posiciona do lado esquerdo/topo
    if maior_linha > largura_disponivel:
        x_start = 1
    else:
        x_start = max(1, (largura_disponivel - maior_linha) // 2)
    
    if num_linhas > altura_disponivel:
        y_start = 1
    else:
        y_start = max(1, (altura_disponivel - num_linhas) // 2)
    
    for i, linha in enumerate(linhas):
        try:
            # Trunca a linha se for maior que a janela (sem remover espaços importantes)
            linha_exibir = linha[:largura_disponivel - x_start]
            janelaMeioCima.addstr(y_start + i, x_start, linha_exibir, ENEMY_COLOR)
            stdscr.refresh()
            janelaMeioCima.refresh()
        except curses.error:
            # Ignora linhas que ultrapassam a altura da janela
            pass






def menu(stdscr, escolha):
    match escolha:
        case 0:

            iniciarServidorJava(stdscr)

            janelaDireita.addstr("Entrando no servidor... \n", SCREEN_BORDER_COLOR)
            janelaDireita.refresh()
            stdscr.refresh()

            #ajusta o caminho para importar o módulo de rede
            raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            sys.path.insert(0, os.path.join(raiz, 'network'))

            

            try:
                # importa o modulo de rede
                from EntrarServidor import ConectarComServidor
                teste = ConectarComServidor()

                if teste:
                    try:
                        #janelaDireita.erase()
                        janelaDireita.addstr(teste, SCREEN_BORDER_COLOR)
                        janelaDireita.refresh()
                        stdscr.refresh()
                    except Exception as e:
                        janelaDireita.addstr(f"Erro ao exibir: {e} \n", SCREEN_BORDER_COLOR)
                        janelaDireita.refresh()
                        stdscr.refresh()

            except ImportError as e:
                janelaDireita.addstr(f"Erro de importação: {e} \n", SCREEN_BORDER_COLOR)
                janelaDireita.refresh()
                stdscr.refresh()
            except Exception as e:
                janelaDireita.addstr(f"Erro: {e}", SCREEN_BORDER_COLOR)
                janelaDireita.refresh()
                stdscr.refresh()

            janelaEsquerda.refresh()    
        case 1: 
            return ""
        case 2:
            curses.endwin()
            sys.exit(0)




def liberar_porta(porta):
    """Mata qualquer processo usando a porta especificada."""
    print(f"Liberando porta {porta}...")
    try:
        if os.name == 'nt':  # Windows
            # netstat -ano | findstr :5000
            result = subprocess.run(f'netstat -ano | findstr :{porta}', shell=True, capture_output=True, text=True)
            if result.stdout:
                for line in result.stdout.splitlines():
                    parts = line.split()
                    if len(parts) > 4:
                        pid = parts[-1]
                        try:
                            subprocess.run(f'taskkill /PID {pid} /F', shell=True, capture_output=True)
                            print(f"Processo {pid} matado.")
                        except Exception as e:
                            print(f"Erro ao matar processo {pid}: {e}")
        else:  # Linux/Mac
            result = subprocess.run(f'lsof -ti :{porta}', shell=True, capture_output=True, text=True)
            if result.stdout.strip():
                pids = result.stdout.strip().split(',')
                for pid in pids:
                    try:
                        os.kill(int(pid), signal.SIGKILL)
                        print(f"Processo {pid} matado.")
                    except Exception as e:
                        print(f"Erro ao matar processo {pid}: {e}")
    except Exception as e:
        print(f"Erro ao liberar porta: {e}")

def iniciarServidorJava(stdscr):
    BASE_DIR = Path(__file__).resolve().parent
    JAVA_DIR = str(BASE_DIR / ".." / ".." / "java-server" / "out" / "production" / "src")
    PORTA = 5000

    # 1. LIBERA A PORTA ANTES DE TUDO
    liberar_porta(PORTA)
    time.sleep(1) # Pequena pausa para o SO liberar a porta

    try:
        janelaDireita.addstr(f"Iniciando servidor Java na porta {PORTA}... \n", SCREEN_BORDER_COLOR)
        janelaDireita.refresh()
        stdscr.refresh()

        # Inicia o processo
        process1 = subprocess.Popen(
            ["java", "com.network.CriarServer"],
            cwd=JAVA_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        server_started = False
        output_log = []

        def leer_saida(pipe, target_list):
            for line in iter(pipe.readline, ''):
                target_list.append(line)
                if "Servidor iniciado" in line:
                    target_list.append("START")
                if "Exception" in line or "BindException" in line:
                    target_list.append("ERROR")
            pipe.close()

        reader_thread = threading.Thread(target=leer_saida, args=(process1.stdout, output_log))
        reader_thread.daemon = True
        reader_thread.start()

        timeout_limit = 10
        start_time = time.time()
        
        while time.time() - start_time < timeout_limit:
            if process1.poll() is not None:
                # Processo morreu
                stderr_val = process1.stderr.read()
                if "BindException" in stderr_val:
                    janelaDireita.addstr(f"Erro: Porta {PORTA} ainda ocupada após tentar liberar. \n", SCREEN_BORDER_COLOR)
                else:
                    janelaDireita.addstr(f"Erro inesperado: {stderr_val[:200]} \n", SCREEN_BORDER_COLOR)
                return False
            
            if "START" in output_log:
                server_started = True
                break
            
            time.sleep(0.1)

        if not server_started:
            # Verifica se o processo está vivo mas não imprimiu nada
            if process1.poll() is None:
                 # Timeout
                 process1.terminate()
                 janelaDireita.addstr(f"Erro: Servidor Java não respondeu em {timeout_limit}s. \n", SCREEN_BORDER_COLOR)
                 return False
            else:
                 stderr_val = process1.stderr.read()
                 janelaDireita.addstr(f"Erro: {stderr_val[:200]} \n", SCREEN_BORDER_COLOR)
                 return False

        # Sucesso
        janelaDireita.addstr("Servidor Java iniciado com sucesso! \n", SCREEN_BORDER_COLOR)
        janelaDireita.refresh()
        stdscr.refresh()
        time.sleep(0.5) # Garante que o socket esteja pronto
        return True

    except Exception as e:
        janelaDireita.addstr(f"Erro ao iniciar servidor: {e} \n", SCREEN_BORDER_COLOR)
        return False

# Nota: Certifique-se de que o Java imprima EXATAMENTE "Servidor iniciado na porta 5000!"
# No seu código Java, o print é: System.out.println("Servidor iniciado na porta 5000!");
# O código Python procura por "Servidor iniciado", o que funciona.



def MeuInicial(stdscr):
    global alturaTela
    global larguraTela  
    global tercoTela

    alturaTela = 0
    larguraTela = 0

    alturaTela, larguraTela = stdscr.getmaxyx()
    alturaTela -= 1
    larguraTela -= 2

    tercoTela = larguraTela // 3


    # Configurações iniciais da tela
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    global SCREEN_BORDER_COLOR
    SCREEN_BORDER_COLOR = curses.color_pair(1)

    # Configurações do cursor
    cursorEsquerdo = "> "
    cursorDireito = " <"
    cursorY = 4
    cursorOpcao = 0

    # Configurações do menu
    alturaMenu = 15
    larguraMenu = 45

    y = int(alturaTela/2 - alturaMenu/2)
    x = int(larguraTela/2 - larguraMenu/2)



    # Variaveis do titulo do menu
    titulo = "Lost in the Void"
    yTitulo = 2
    xTitulo = int(larguraMenu - len(titulo)) // 2

    # Variaveis das opcoes do menu
    opcoes = ["Novo jogo", "Carregar jogo", "Configurações", "Sair"]
    yOpcoes = 4




    #Cria a janela do menu
    menuInicialWindow = curses.newwin(alturaMenu,larguraMenu, y,  x)

    menuInicialWindow.refresh()
    stdscr.refresh()



    # Configura a janela do menu
    menuInicialWindow.bkgd(' ', SCREEN_BORDER_COLOR)
    menuInicialWindow.border()



    # Adiciona os textos do menu
    menuInicialWindow.addstr(yTitulo, xTitulo, titulo, SCREEN_BORDER_COLOR)
    for i, opcao in enumerate(opcoes):
        menuInicialWindow.addstr(yOpcoes + i, (int(larguraMenu - len(opcoes[i])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, "  " + opcao + "  ", SCREEN_BORDER_COLOR)
    menuInicialWindow.refresh()
    stdscr.refresh()

    menuInicialWindow.addstr(cursorY, (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, cursorEsquerdo + opcoes[cursorOpcao] + cursorDireito, SCREEN_BORDER_COLOR)
    menuInicialWindow.refresh()
    stdscr.refresh()


    while True:
        
        menuInicialWindow.addstr(cursorY, (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, cursorEsquerdo + opcoes[cursorOpcao] + cursorDireito, SCREEN_BORDER_COLOR)
        menuInicialWindow.refresh()
        stdscr.refresh()

        key = stdscr.getkey()

        if key == "KEY_UP" and cursorY > 4:
            menuInicialWindow.addstr(cursorY,  (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, "  " + opcoes[cursorOpcao] + "  ", SCREEN_BORDER_COLOR)
            menuInicialWindow.refresh()
            stdscr.refresh()
            cursorOpcao -= 1
            cursorY -= 1
        elif key == "KEY_DOWN" and cursorY < 7:
            menuInicialWindow.addstr(cursorY, (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, "  " + opcoes[cursorOpcao] + "  ", SCREEN_BORDER_COLOR)
            menuInicialWindow.refresh()
            stdscr.refresh()
            cursorOpcao += 1
            cursorY += 1

        if key == "KEY_ENTER" or key == "\n":
            match cursorOpcao:
                case 0:
                    return
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    curses.endwin()
                    sys.exit(0)
    
    
    








def main(stdscr):
    
    MeuInicial(stdscr)

    DesenharLayout(stdscr)



    posicaoCursor = 0
    cursor = "> "

    for i, opcao in enumerate(opcoes):
        janelaEsquerda.addstr(i, 0, "  " + opcao, SCREEN_BORDER_COLOR)
        stdscr.refresh()
        janelaEsquerda.refresh()

    #janelaEsquerda.addstr(0, 0, "  " + opcoes[0] + "  ", SCREEN_BORDER_COLOR)
    #janelaEsquerda.addstr(1, 0, "  " + opcoes[1] + "  ", SCREEN_BORDER_COLOR)
    #janelaEsquerda.addstr(2, 0, "  " + opcoes[2] + "  ", SCREEN_BORDER_COLOR)

    while True:
        
        janelaEsquerda.addstr(posicaoCursor, 0, cursor, SCREEN_BORDER_COLOR)
        janelaEsquerda.refresh()
        stdscr.refresh()

        key = stdscr.getkey()

        if key == "KEY_UP" and posicaoCursor > 0:
            janelaEsquerda.addstr(posicaoCursor, 0, "  ")
            posicaoCursor -= 1
        elif key == "KEY_DOWN" and posicaoCursor < len(opcoes) - 1:
            janelaEsquerda.addstr(posicaoCursor, 0, "  ")
            posicaoCursor += 1

        if key == "KEY_ENTER" or key == "\n":
            menu(stdscr, posicaoCursor)
        





    # Preenche a janela esquerda com caracteres
    
    
            
  

    """
    for i in range(alturaTelaDireita):
        for j in range(larguraTelaDireita - 1):
            
            janelaDireita.addstr(i, j, "0", color)
            stdscr.refresh()
            janelaDireita.refresh()
    
    


    for i in range(alturaTelaMeioBaixo):
        for j in range(larguraTelaMeioBaixo - 1):
            
            janelaMeioBaixo.addstr(i, j, "0", color)
            stdscr.refresh()
            janelaMeioBaixo.refresh()
            
        time.sleep(0.0001)
    """

    

    











    # Espera um input do usuario
    

    






    

#wrapper(variaveis)
#wrapper(telainicial)
wrapper(main)