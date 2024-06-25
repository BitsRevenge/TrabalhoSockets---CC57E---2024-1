import socket

HOST = '127.0.0.1'  
PORT = 65432        

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        response = s.recv(1024)
        print(f"Resposta: {response.decode()}")

def main():
    print("Tentando conectar ao servidor...")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Conectado ao servidor.")
    except ConnectionRefusedError:
        print("Não foi possível se conectar ao servidor.")
        return

    print("Digite um comando para enviar ao servidor (GET-FORTUNE, ADD-FORTUNE <frase>, UPD-FORTUNE <pos> <nova frase>, LST-FORTUNE).")
    print("Digite 'EXIT' para sair.")

    while True:
        command = input("Comando: ")
        if command.strip().upper() == "EXIT":
            print("Encerrando o cliente.")
            break
        send_command(command)

if __name__ == "__main__":
    main()