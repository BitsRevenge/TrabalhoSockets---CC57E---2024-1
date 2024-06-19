import socket

# Configuração do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor escuta

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        response = s.recv(1024)
        print(f"Resposta: {response.decode()}")

# Loop para ler comandos do usuário e enviar para o servidor
print("Digite um comando para enviar ao servidor (GET-FORTUNE, ADD-FORTUNE <frase>, UPD-FORTUNE <pos> <nova frase>, LST-FORTUNE).")
print("Digite 'EXIT' para sair.")

while True:
    command = input("Comando: ")
    if command.strip().upper() == "EXIT":
        print("Encerrando o cliente.")
        break
    send_command(command)