
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



# Inicializa as cores da aplicacao
def inicializarCores(stdscr):
    curses.start_color()
    curses.use_default_colors()

    # Define a cor padrao(foreground - verde | background - preto)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    global COR_PADRAO
    COR_PADRAO = curses.color_pair(1)

    # Define a cor padrao(foreground - verde | background - preto)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    global COR_INIMIGO
    COR_INIMIGO = curses.color_pair(2)



def inicializarVariaveisDeTela(stdscr):
    global alturaTela
    global larguraTela  
    global tercoTela
    
    alturaTela, larguraTela = stdscr.getmaxyx()
    alturaTela -= 1
    larguraTela -= 2

    tercoTela = larguraTela // 3




def DesenharLayout(stdscr):
    global alturaTela
    global larguraTela  
    global tercoTela

    # Inicialiva variaveis para a posicao do layout(bordas)
    yLayout = 0
    xLayout = 0


    global opcoes
    opcoes = ["Conectar ao servidor", "Configurações", "Sair"]

    # Desenha as bordas do layout
    stdscr.addstr(yLayout, xLayout, "┌", COR_PADRAO)
    stdscr.addstr(alturaTela, xLayout, "└", COR_PADRAO)
    stdscr.addstr(yLayout, larguraTela, "┐", COR_PADRAO)
    stdscr.addstr(alturaTela, larguraTela, "┘", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas verticais do layout
    for i in range(1, alturaTela):
        stdscr.addstr(i, xLayout, "│", COR_PADRAO)
        stdscr.addstr(i, larguraTela, "│", COR_PADRAO)
    stdscr.refresh()
    
    # Desenha as linhas horizontais do layout
    for i in range(1, larguraTela):
        stdscr.addstr(yLayout, i, "─", COR_PADRAO)
        stdscr.addstr(alturaTela, i, "─", COR_PADRAO)
    stdscr.refresh()
    


def DesenharPainelEsquerdo(stdscr):
    global alturaTela
    global larguraTela
    global tercoTela

    # Inicialiva variaveis para a posicao do painel esquerdo
    ypainelEsquerdo = 1
    xpainelEsquerdo = 1

    alturaPainelEsquerdo = alturaTela - 1
    larguraPainelEsquerdo = tercoTela
    

    # Desenha as bordas do painel esquerdo
    stdscr.addstr(ypainelEsquerdo, xpainelEsquerdo, "┌", COR_PADRAO)
    stdscr.addstr(alturaPainelEsquerdo, xpainelEsquerdo, "└", COR_PADRAO)
    stdscr.addstr(ypainelEsquerdo, larguraPainelEsquerdo, "┐", COR_PADRAO)
    stdscr.addstr(alturaPainelEsquerdo, larguraPainelEsquerdo, "┘", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas verticais do painel esquerdo
    for i in range(2, alturaPainelEsquerdo):
        stdscr.addstr(i, xpainelEsquerdo, "│", COR_PADRAO)
        stdscr.addstr(i, larguraPainelEsquerdo, "│", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas horizontais do painel esquerdo
    for i in range(2, tercoTela):
        stdscr.addstr(ypainelEsquerdo, i, "─", COR_PADRAO)
        stdscr.addstr(alturaPainelEsquerdo, i, "─", COR_PADRAO)
    stdscr.refresh()


    # Inicialiva variaveis para a posicao da Janela do painel esquerdo
    global janelaEsquerda
    global alturaJanelaEsquerda
    global larguraJanelaEsquerda

    yjanelaEsquerda = 2
    xjanelaEsquerda = 3

    alturaJanelaEsquerda = alturaTela - 3
    larguraJanelaEsquerda = tercoTela - 3

    # Cria as janelas para cada painel
    janelaEsquerda = curses.newwin(alturaJanelaEsquerda,larguraJanelaEsquerda,yjanelaEsquerda,xjanelaEsquerda)



def DesenharPainelDireito(stdscr):
    global alturaTela
    global larguraTela
    global tercoTela

    # Inicialiva variaveis para a posicao do painel direito
    ypainelDireito = 1
    xpainelDireito = tercoTela * 2

    alturaPainelDireito = alturaTela - 1
    larguraPainelDireito = larguraTela - 2

    
    # Desenha as bordas do painel direito
    stdscr.addstr(ypainelDireito, xpainelDireito, "┌", COR_PADRAO)
    stdscr.addstr(alturaPainelDireito, xpainelDireito, "└", COR_PADRAO)
    stdscr.addstr(ypainelDireito, larguraPainelDireito, "┐", COR_PADRAO)
    stdscr.addstr(alturaPainelDireito, larguraPainelDireito, "┘", COR_PADRAO)
    stdscr.refresh()
            
    # Desenha as linhas verticais do painel direito
    for i in range(2, alturaPainelDireito):
        stdscr.addstr(i, xpainelDireito, "│", COR_PADRAO)
        stdscr.addstr(i, larguraPainelDireito, "│", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas horizontais do painel direito
    for i in range(xpainelDireito + 1, larguraPainelDireito):
        stdscr.addstr(ypainelDireito, i, "─", COR_PADRAO)
        stdscr.addstr(alturaPainelDireito, i, "─", COR_PADRAO)
    stdscr.refresh()


    # Inicialiva variaveis para a posicao da Janela do painel direito
    global janelaDireita
    global alturaJanelaDireita
    global larguraJanelaDireita

    yjanelaDireita = 2
    xjanelaDireita = tercoTela * 2 + 2

    alturaJanelaDireita = alturaTela - 3
    larguraJanelaDireita = tercoTela - 2

    # Cria as janelas para cada painel
    janelaDireita = curses.newwin(alturaJanelaDireita,larguraJanelaDireita,yjanelaDireita,xjanelaDireita)



def DesenharPainelMeioCima(stdscr):
    global alturaTela
    global larguraTela
    global tercoTela

    # Inicialiva variaveis para a posicao do painel do meio-cima
    ypainelMeioCima = 1
    xpainelMeioCima = tercoTela + 1

    alturaPainelMeioCima = (alturaTela // 2) - 1
    larguraPainelMeioCima = (tercoTela * 2) - 1


    # Desenha as bordas do painel do meio-cima
    stdscr.addstr(ypainelMeioCima, xpainelMeioCima, "┌", COR_PADRAO)
    stdscr.addstr(alturaPainelMeioCima, xpainelMeioCima, "└", COR_PADRAO)
    stdscr.addstr(ypainelMeioCima, larguraPainelMeioCima, "┐", COR_PADRAO)
    stdscr.addstr(alturaPainelMeioCima, larguraPainelMeioCima, "┘", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas verticais do painel do meio-cima
    for i in range(2, alturaPainelMeioCima):
        stdscr.addstr(i, xpainelMeioCima, "│", COR_PADRAO)
        stdscr.addstr(i, larguraPainelMeioCima, "│", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas horizontais do painel do meio-cima
    for i in range(xpainelMeioCima + 1, larguraPainelMeioCima):
        stdscr.addstr(ypainelMeioCima, i, "─", COR_PADRAO)
        stdscr.addstr(alturaPainelMeioCima, i, "─", COR_PADRAO)
    stdscr.refresh()


    # Inicialiva variaveis para a posicao da Janela do painel do meio-cima
    global janelaMeioCima
    global alturaJanelaMeioCima
    global larguraJanelaMeioCima

    yjanelaMeioCima = 2
    xjanelaMeioCima = tercoTela + 3

    alturaJanelaMeioCima = alturaTela // 2 - 3
    larguraJanelaMeioCima = tercoTela - 4

    # Cria as janelas para cada painel
    janelaMeioCima = curses.newwin(alturaJanelaMeioCima,larguraJanelaMeioCima,yjanelaMeioCima,xjanelaMeioCima)



def DesenharPainelMeioBaixo(stdscr):
    global alturaTela
    global larguraTela
    global tercoTela

    # Inicialiva variaveis para a posicao do painel do meio-bai
    ypainelMeioCima = (alturaTela // 2) 
    xpainelMeioCima = tercoTela + 1

    alturaPainelMeioCima = alturaTela - 1
    larguraPainelMeioCima = tercoTela * 2 - 1

   
    # Desenha as bordas do painel do meio-baixo
    stdscr.addstr(ypainelMeioCima, xpainelMeioCima, "┌", COR_PADRAO)
    stdscr.addstr(alturaPainelMeioCima, xpainelMeioCima, "└", COR_PADRAO)
    stdscr.addstr(ypainelMeioCima, larguraPainelMeioCima, "┐", COR_PADRAO)
    stdscr.addstr(alturaPainelMeioCima, larguraPainelMeioCima, "┘", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas verticais do painel do meio-baixo
    for i in range(ypainelMeioCima + 1, alturaPainelMeioCima):
        stdscr.addstr(i, xpainelMeioCima, "│", COR_PADRAO)
        stdscr.addstr(i, larguraPainelMeioCima, "│", COR_PADRAO)
    stdscr.refresh()

    # Desenha as linhas horizontais do painel do meio-baixo
    for i in range(xpainelMeioCima + 1, larguraPainelMeioCima):
        stdscr.addstr(ypainelMeioCima, i, "─", COR_PADRAO)
        stdscr.addstr(alturaPainelMeioCima, i, "─", COR_PADRAO)
    stdscr.refresh()


    # Inicialiva variaveis para a posicao da Janela do painel do meio-baixo
    global janelaMeioBaixo
    global alturaJanelaMeioBaixo
    global larguraJanelaMeioBaixo

    yjanelaMeioBaixo = (alturaTela // 2) + 1
    xjanelaMeioBaixo = tercoTela + 3

    alturaJanelaMeioBaixo = alturaTela // 2 - 2
    larguraJanelaMeioBaixo = tercoTela - 4

    # Cria as janelas para cada painel
    janelaMeioBaixo = curses.newwin(alturaJanelaMeioBaixo,larguraJanelaMeioBaixo,yjanelaMeioBaixo,xjanelaMeioBaixo)



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
            janelaMeioCima.addstr(y_start + i, x_start, linha_exibir, COR_INIMIGO)
            stdscr.refresh()
            janelaMeioCima.refresh()
        except curses.error:
            # Ignora linhas que ultrapassam a altura da janela
            pass






def menu(stdscr, escolha):
    match escolha:
        case 0:

            iniciarServidorJava(stdscr)

            janelaDireita.addstr("Entrando no servidor... \n", COR_PADRAO)
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
                        janelaDireita.addstr(teste, COR_PADRAO)
                        janelaDireita.refresh()
                        stdscr.refresh()
                    except Exception as e:
                        janelaDireita.addstr(f"Erro ao exibir: {e} \n", COR_PADRAO)
                        janelaDireita.refresh()
                        stdscr.refresh()

            except ImportError as e:
                janelaDireita.addstr(f"Erro de importação: {e} \n", COR_PADRAO)
                janelaDireita.refresh()
                stdscr.refresh()
            except Exception as e:
                janelaDireita.addstr(f"Erro: {e}", COR_PADRAO)
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
        janelaDireita.addstr(f"Iniciando servidor Java na porta {PORTA}... \n", COR_PADRAO)
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
                    janelaDireita.addstr(f"Erro: Porta {PORTA} ainda ocupada após tentar liberar. \n", COR_PADRAO)
                else:
                    janelaDireita.addstr(f"Erro inesperado: {stderr_val[:200]} \n", COR_PADRAO)
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
                 janelaDireita.addstr(f"Erro: Servidor Java não respondeu em {timeout_limit}s. \n", COR_PADRAO)
                 return False
            else:
                 stderr_val = process1.stderr.read()
                 janelaDireita.addstr(f"Erro: {stderr_val[:200]} \n", COR_PADRAO)
                 return False

        # Sucesso
        janelaDireita.addstr("Servidor Java iniciado com sucesso! \n", COR_PADRAO)
        janelaDireita.refresh()
        stdscr.refresh()
        time.sleep(0.5) # Garante que o socket esteja pronto
        return True

    except Exception as e:
        janelaDireita.addstr(f"Erro ao iniciar servidor: {e} \n", COR_PADRAO)
        return False

# Nota: Certifique-se de que o Java imprima EXATAMENTE "Servidor iniciado na porta 5000!"
# No seu código Java, o print é: System.out.println("Servidor iniciado na porta 5000!");
# O código Python procura por "Servidor iniciado", o que funciona.



def MeuInicial(stdscr):
    global alturaTela
    global larguraTela  
    global tercoTela

    alturaMenu = tercoTela
    larguraMenu = tercoTela

    alturaTela = 0
    larguraTela = 0

    alturaTela, larguraTela = stdscr.getmaxyx()
    alturaTela -= 1
    larguraTela -= 2

    tercoTela = larguraTela // 3


    # Configurações iniciais da tela
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    global COR_PADRAO
    COR_PADRAO = curses.color_pair(1)

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
    menuInicialWindow.bkgd(' ', COR_PADRAO)
    menuInicialWindow.border()



    # Adiciona os textos do menu
    menuInicialWindow.addstr(yTitulo, xTitulo, titulo, COR_PADRAO)
    for i, opcao in enumerate(opcoes):
        menuInicialWindow.addstr(yOpcoes + i, (int(larguraMenu - len(opcoes[i])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, "  " + opcao + "  ", COR_PADRAO)
    menuInicialWindow.refresh()
    stdscr.refresh()

    menuInicialWindow.addstr(cursorY, (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, cursorEsquerdo + opcoes[cursorOpcao] + cursorDireito, COR_PADRAO)
    menuInicialWindow.refresh()
    stdscr.refresh()


    while True:
        
        menuInicialWindow.addstr(cursorY, (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, cursorEsquerdo + opcoes[cursorOpcao] + cursorDireito, COR_PADRAO)
        menuInicialWindow.refresh()
        stdscr.refresh()

        key = stdscr.getkey()

        if key == "KEY_UP" and cursorY > 4:
            menuInicialWindow.addstr(cursorY,  (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, "  " + opcoes[cursorOpcao] + "  ", COR_PADRAO)
            menuInicialWindow.refresh()
            stdscr.refresh()
            cursorOpcao -= 1
            cursorY -= 1
        elif key == "KEY_DOWN" and cursorY < 7:
            menuInicialWindow.addstr(cursorY, (int(larguraMenu - len(opcoes[cursorOpcao])) - (len(cursorEsquerdo) + len(cursorDireito)))// 2, "  " + opcoes[cursorOpcao] + "  ", COR_PADRAO)
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

    # Inicializa variaveis globais
    inicializarCores(stdscr)
    inicializarVariaveisDeTela(stdscr)

    MeuInicial(stdscr)

    stdscr.clear()
    DesenharLayout(stdscr)
    DesenharPainelEsquerdo(stdscr)
    DesenharPainelDireito(stdscr)
    DesenharPainelMeioCima(stdscr)
    DesenharPainelMeioBaixo(stdscr)



    
    
    
            


    posicaoCursor = 0
    cursor = "> "

    for i, opcao in enumerate(opcoes):
        janelaEsquerda.addstr(i, 0, "  " + opcao, COR_PADRAO)
        stdscr.refresh()
        janelaEsquerda.refresh()

    #janelaEsquerda.addstr(0, 0, "  " + opcoes[0] + "  ", COR_PADRAO)
    #janelaEsquerda.addstr(1, 0, "  " + opcoes[1] + "  ", COR_PADRAO)
    #janelaEsquerda.addstr(2, 0, "  " + opcoes[2] + "  ", COR_PADRAO)

    while True:
        
        janelaEsquerda.addstr(posicaoCursor, 0, cursor, COR_PADRAO)
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
        





    
    
            
  

    

    

    





    


"""
for i in range(alturaJanelaEsquerda):
    for j in range(larguraJanelaEsquerda - 1):
        
        janelaEsquerda.addstr(i, j, "0", COR_PADRAO)
        stdscr.refresh()
        janelaEsquerda.refresh()





for i in range(alturaJanelaMeioCima):
    for j in range(larguraJanelaMeioCima - 1):
        
        janelaMeioCima.addstr(i, j, "0", COR_PADRAO)
        stdscr.refresh()
        janelaMeioCima.refresh()
    time.sleep(0.1)
"""



    

#wrapper(variaveis)
#wrapper(telainicial)
wrapper(main)