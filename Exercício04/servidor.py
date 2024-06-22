import socket
import threading
from time import sleep
from random import randint

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def depositar(self, valor):
        with self.lock:
            self.saldo += valor
            return f"Depósito de {valor}. Novo saldo: {self.saldo}"

    def sacar(self, valor):
        with self.lock:
            if valor > self.saldo:
                return "Saldo insuficiente."
            else:
                self.saldo -= valor
                return f"Saque de {valor}. Novo saldo: {self.saldo}"

    def obter_saldo(self):
        with self.lock:
            return f"Saldo atual: {self.saldo}"

clients = []
def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conta = ContaBancaria(0)
    try:
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=(client, conta))
        thread.start()

def messagesTreatment(*args):
        client = args[0]
        conta = args[1]
        while True:
            try:
                client.send(("*** Sistema Bancário ***\n[1] - Depositar\n[2] - Sacar\n[3] - Consultar\n[-1] - Sair").encode())
                msg = client.recv(2048).decode()
                if msg[-2:] == '-1':
                    client.send((f"Saindo do app.").encode())
                    print(f"{client} saiu do app.")
                    return False
                elif msg[-1] == '1':
                    for clientItem in clients:
                        if clientItem == client:
                            try:
                                clientItem.send(("Digite a quantia: ").encode())
                                quantia = clientItem.recv(2048).decode()
                                valor = int(quantia.split("> ")[1])
                                # valor = randint(1, 1000)
                                print("Deposito de ", valor)
                                clientItem.send(conta.depositar(valor).encode())
                                sleep(2)
                            except:
                                deleteClient(clientItem)
                                break
                elif msg[-1] == '2':
                    for clientItem in clients:
                        if clientItem == client:
                            try:
                                clientItem.send(("Digite a quantia: ").encode())
                                quantia = clientItem.recv(2048).decode()
                                valor = int(quantia.split("> ")[1])
                                # valor = randint(1, 1000)
                                print("Saque de ", valor)
                                clientItem.send(conta.sacar(valor).encode())
                                sleep(2)
                            except:
                                deleteClient(clientItem)
                                break
                elif msg[-1] == '3':
                    for clientItem in clients:
                        if clientItem == client:
                            clientItem.send(conta.obter_saldo().encode())
                else:
                    print("Operação desconhecida.")
            except:
                break
def deleteClient(client):
    clients.remove(client)


main()
