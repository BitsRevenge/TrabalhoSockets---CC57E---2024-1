import signal
import socket
import random

def esconder_palavra(palavra):
    palavraE = []
    for i in palavra:
        palavraE.append('_')
    return palavraE

def process_data(letra, palavra):
    posicoes = []
    posicao = 0
    for i in palavra:
        if letra == i:
            posicoes.append(posicao)
        posicao = posicao + 1
    return posicoes


def main():
    # Configurar o socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    palavras = ['paralelepipedo', 'otorrinolaringologista', 'pneumoultramicroscopicossilicovulcanoconiose',
                'piperidinoetoxicarbometoxibenzofenona']
    palavra = palavras[random.randint(0, 3)]
    palavraE = esconder_palavra(palavra)
    print("Servidor pronto para aceitar conexões...")

    while True:
        # Aceitar uma nova conexão
        client_socket, client_address = server_socket.accept()
        print(f"Conexão aceita de {client_address}")

        try:
            while True:
                # Receber dados do cliente
                letra = client_socket.recv(1024).decode()
                if not letra:
                    break
                print(f"Recebido letra: {letra}")
                # Processar os dados recebidos
                result = process_data(letra, palavra)
                if result:
                    for i in result:
                        palavraE[i] = palavra[i]
                print(f"Resultado da operação: {' '.join(palavraE)}")

                # Enviar o resultado de volta ao cliente
                client_socket.sendall(str(' '.join(palavraE)).encode())
                if set(palavra) == set(palavraE):
                    break
            client_socket.recv(1024).decode()
            print("Jogo Finalizado")
            client_socket.sendall(str(-2).encode())
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            # Fechar a conexão com o cliente
            client_socket.close()
            print(f"Conexão com {client_address} encerrada")
            palavra = palavras[random.randint(0, 3)]
            palavraE = esconder_palavra(palavra)


if __name__ == "__main__":
    main()
