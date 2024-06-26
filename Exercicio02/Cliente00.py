import socket


def main():
    # Configurar o socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    try:
        # Enviar dados para o servidor
        data = str(input("Insira a operação: "))
        print(f"Enviando: {data}")
        client_socket.sendall(data.encode())

        # Receber o resultado do servidor
        result = client_socket.recv(1024).decode()
        print(f"Resultado recebido: {result}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fechar a conexão com o servidor
        client_socket.close()


if __name__ == "__main__":
    main()