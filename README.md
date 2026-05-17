<<<<<<< HEAD


------------------------------------------------------------------------------------------

PARAR PROGRAMA
Se o programa travar use "Ctrl" + "C" para parar(para qualquer programa rodando no terminal)

------------------------------------------------------------------------------------------
VER SOCKETS POR PORTA - matar processo

Use "netstat -ano | findstr :5000" para ver seus sockets abertos na porta 5000(mude o nomero para o que voce preferir).

Você verá algo como: TCP    0.0.0.0:5000    0.0.0.0:0    LISTENING    12345 (O número no final, ex: 12345, é o PID - Process ID).

Mate o processo usando o PID encontrado (substitua 12345 pelo número real):
taskkill /PID 12345 /F



LINUX
Se você estiver no Linux ou macOS (Terminal)

Descubra o processo:
lsof -i :5000
# OU
netstat -tulpn | grep :5000

Procure pelo PID (Process ID) na coluna PID ou PROCESS.

Mate o processo (substitua 12345 pelo PID):
kill -9 12345

------------------------------------------------------------------------------------------

VER SOCKETS LISTENING
netstat -ano | findstr LISTENING

------------------------------------------------------------------------------------------
TIME_WAITING

O estado TIME_WAIT que você está vendo é comum e normal no Windows e em redes TCP/IP. Ele indica que conexões recentes foram encerradas corretamente, mas o sistema operacional está "esperando" um pouco para garantir que nenhum pacote antigo se perca antes de liberar completamente a porta.

------------------------------------------------------------------------------------------
=======
# Lost-In-The-Void
"Lost In The Void" é um jogo de RPG por turnos desenvolvido por mim. Além de ser um ótimo passatempo, ele me estimula a aprender assuntos cada vez mais difíceis e específicos.
>>>>>>> 4547e2d663b1c08bde8db99db985448185e78fd3
