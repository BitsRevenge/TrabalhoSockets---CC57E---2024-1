import threading
import socket
from random import randint
from time import sleep


def main():
    filial = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        filial.connect(('localhost', 7777))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário> ')
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[filial])
    thread2 = threading.Thread(target=sendMessages, args=[filial, username])

    thread1.start()
    thread2.start()


def receiveMessages(filial):
    while True:
        try:
            msg = filial.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            filial.close()
            break


def sendMessages(filial, username):
    while True:
        try:
            for i in range(15):
                vendas = randint(0, 1000)
                msg = f"Venda total: {vendas}"
                filial.send(f'<{username}> {msg}'.encode('utf-8'))
                sleep(2)
            filial.close()
        except:
            return False


main()