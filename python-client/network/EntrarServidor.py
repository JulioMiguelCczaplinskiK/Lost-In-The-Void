
import curses
from curses import wrapper
import socket
import os
import sys


def ConectarComServidor():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Conectar-se
        client.connect(("localhost", 5000))
        # enviar dados
        client.sendall(b'{"type":"MOVE"}\n')
    
        # 3. ESPERAR RESPOSTA DO SERVIDOR (Crucial!)
        # O servidor deve enviar algo de volta
        # O timeout evita que o programa trave se o servidor ficar calado
        client.settimeout(5.0)  # Espera no máximo 5 segundos

        # Recebe a resposta do servidor
        resposta = client.recv(1024) # Recebe até 1024 bytes

        if not resposta:
            return "ERRO - Conexão fechada, servidor nao respondeu. \n"
        
        # 4. Verificar se a resposta indica sucesso
        resposta_str = resposta.decode('utf-8').strip()
        

        if "OK" in resposta_str or "success" in resposta_str:
            return f"Conexão estabelecida e resposta recebida: {resposta_str} \n"
        else:
            return f"Conexão estabelecida, mas servidor retornou erro/aviso: {resposta_str} \n"




        #return "Conexão com o servidor estabelecida e dado enviado com sucesso."
    except socket.timeout:
        client.close()
        return "ERRO - Servidor não respondeu dentro do tempo limite (timeout). \n"
    except ConnectionRefusedError:
        client.close()
        return "ERRO - Servidor recusou a conexão (está desligado ou porta errada). \n"
    except Exception as e:
        client.close()
        return f"ERRO - Erro inesperado: {str(e)} \n"
    finally:
        client.close()

    


if __name__ == "__main__":

    # "client = socket.socket()"   - abre a rede/inicia o cliente.
    # "socket.AF_INET"      - define o protocolo IPv4.
    # "socket.SOCK_STREAM"  - define o tipo de conexao(usa TCP (Transmission Control Protocol)).
    print("Iniciando cliente...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # "client.connect()" - O método connect é usado para estabelecer uma conexão com um servidor. Ele recebe como argumento uma tupla contendo o endereço IP do servidor e a porta na qual o servidor está ouvindo.
    # "localhost" - Refere-se ao próprio computador onde o cliente está sendo executado. É um nome de host que resolve para o endereço IP
    # "5000" - É a porta numérica onde o servidor está aguardando conexões.
    print("Conectando ao servidor...")
    client.connect(("localhost", 5000))

    # "client.sendall()" - É um método que garante que todos os dados passados sejam realmente enviados.
    # "b'{"type":"MOVE"}\n'" - Envia uma string JSON como bytes para o servidor, indicando que o cliente está se movendo.
    # "b''" - nao interpreta a string como texto, mas sim como bytes, caracteres especiais podem dar erro. Converte "café" em "caf\xc3\xa9", por exemplo.
    print("Enviando comando de movimento...")
    client.sendall(b'{"info":"Conectado e funcionando em tempo real"}\n')

    # "client.close()" - Fecha a conexão com o servidor, liberando os recursos associados a essa conexão.
    client.close()




