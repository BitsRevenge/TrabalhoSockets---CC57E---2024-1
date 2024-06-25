import socket

def process_data(data):
    # Separar os números e a operação
    parts = data.strip().split()
    numbers = list(map(int, parts[:-1]))
    operation = parts[-1]

    # Executar a operação
    if operation == 'sum':
        result = sum(numbers)
    elif operation == 'prod':
        result = 1
        for num in numbers:
            result *= num
    elif operation == 'max':
        result = max(numbers)
    elif operation == 'min':
        result = min(numbers)
    else:
        result = "Operação desconhecida"

    return result

def main():
    # Configurar o socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Servidor pronto para aceitar conexões...")

    while True:
        # Aceitar uma nova conexão
        client_socket, client_address = server_socket.accept()
        print(f"Conexão aceita de {client_address}")

        try:
            # Receber dados do cliente
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Dados recebidos: {data}")

            # Processar os dados recebidos
            result = process_data(data)
            print(f"Resultado da operação: {result}")

            # Enviar o resultado de volta ao cliente
            client_socket.sendall(str(result).encode())
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            # Fechar a conexão com o cliente
            client_socket.close()
            print(f"Conexão com {client_address} encerrada")

if __name__ == "__main__":
    main()