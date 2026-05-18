package com.network;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class CriarServer {

    public static void main(String[] args) {

        // Define o numero da porta
        int port = 5000;

        System.out.println("Iniciando servidor...");
        // "ServerSocket server = new ServerSocket(port)" - Cria um servidor na porta "port"
        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("Servidor iniciado na porta " + port + "!");
            System.out.println("Aguardando 1 cliente...");

            // Aceita APENAS UM cliente
            // "Socket client = server.accept();" - para tudo e espera um cliente se conectar
            // para aceitar mais de um e preciso um loop, repetindo o numero de vezes igual ao numero de clientes
            Socket client = server.accept();
            System.out.println("Cliente conectado: " + client.getInetAddress().getHostAddress());

            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            String message;

            try {
                // Lê a mensagem
                if ((message = in.readLine()) != null) {
                    System.out.println("Recebido: " + message);

                    // Processa e envia resposta
                    if (message.contains("\"type\":\"MOVE\"")) {
                        System.out.println("-> MOVE processado.");

                        // Envia resposta
                        String resposta = "OK\n";
                        client.getOutputStream().write(resposta.getBytes());
                        client.getOutputStream().flush();
                        System.out.println("-> Resposta enviada.");
                    }
                }
            } finally {
                // Fecha o socket do cliente
                if (client != null && !client.isClosed()) {
                    client.close();
                    System.out.println("Cliente desconectado.");
                }
            }

            // --- MATAR O SERVIDOR AQUI ---
            System.out.println("Tarefa concluída. Fechando servidor...");
            // O try-with-resources fecha o 'server' automaticamente ao sair deste bloco
            // Mas se quiser encerrar o processo Java imediatamente:
            // System.exit(0);

        } catch (IOException e) {
            System.err.println("Erro: " + e.getMessage());
            e.printStackTrace();
        }

        System.out.println("Servidor encerrado.");
    }
}