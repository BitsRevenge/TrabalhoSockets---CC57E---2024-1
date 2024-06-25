import socket

def print_forca(erro, resultado):
    if erro == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        print(resultado)
    elif erro == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        print(resultado)
    elif erro == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
        print(resultado)
    elif erro == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
        print(resultado)
    elif erro == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|   / \\ ")
        print("_      ")
        print()
        print(resultado)
        print("Fim do jogo!!")
def main():
    # Configurar o socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    erro = 0
    com = []

    try:
        client_socket.sendall(' '.encode())
        result = client_socket.recv(1024).decode()
        print_forca(erro, result)
        while True:
            # Enviar dados para o servidor
            letra = str(input('Insira Uma Letra: '))
            print(f"Enviando: {letra}")
            client_socket.sendall(letra.encode())

            # Receber o resultado do servidor
            result = client_socket.recv(1024).decode()
            if set(com) == set(result):
                erro = erro + 1
            if result == '-2' or erro > 3:
                break
            print_forca(erro, result)
            com = result
        print("Fim do jogo!!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fechar a conexão com o servidor
        client_socket.close()


if __name__ == "__main__":
    main()