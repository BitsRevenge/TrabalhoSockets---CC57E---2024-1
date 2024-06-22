import socket
import threading
from time import sleep

filiais = []
def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        filial, addr = server.accept()
        filiais.append(filial)

        thread = threading.Thread(target=messagesTreatment, args=[filial])
        thread.start()

def messagesTreatment(filial):
        while True:
            try:
                sleep(2)
                msg = filial.recv(2048).decode('utf-8')
                print(msg, " (registrado).")
                filial.send(("Dados confirmados pelo servidor.").encode())

            except:
                deletefilial(filial)
                break

def deletefilial(filial):
    filiais.remove(filial)


main()
