import socket
import random
import threading

# Lista de frases (base de dados de frases)
fortunes = [
    "A vida trará coisas boas se tiveres paciência.",
    "Demonstre amor e alegria em todas as oportunidades e verás que a paz nasce dentro de você.",
    "Não compense na ira o que lhe falta na razão.",
    "Defeitos e virtudes são apenas dois lados da mesma moeda.",
    "A maior de todas as torres começa no solo.",
]

# Função para tratar as conexões dos clientes
def handle_client(conn, addr):
    print(f"Nova conexão: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            command = data.decode().strip().split(maxsplit=1)
            if command[0] == "GET-FORTUNE":
                response = random.choice(fortunes)
            elif command[0] == "ADD-FORTUNE":
                if len(command) > 1:
                    fortunes.append(command[1])
                    response = "Frase adicionada com sucesso."
                else:
                    response = "Erro: Nenhuma frase fornecida."
            elif command[0] == "UPD-FORTUNE":
                if len(command) > 1:
                    try:
                        args = command[1].split(maxsplit=1)
                        index = int(args[0])
                        new_fortune = args[1]
                        fortunes[index] = new_fortune
                        response = "Frase atualizada com sucesso."
                    except (ValueError, IndexError):
                        response = "Erro: Índice inválido ou frase não fornecida."
                else:
                    response = "Erro: Nenhuma frase fornecida."
            elif command[0] == "LST-FORTUNE":
                response = "\n".join(f"{i}: {fortune}" for i, fortune in enumerate(fortunes))
            else:
                response = "Comando desconhecido."
            conn.sendall(response.encode())
    print(f"Conexão encerrada: {addr}")

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor escuta

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor iniciado em {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()