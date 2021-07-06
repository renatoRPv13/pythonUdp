from socket import *


def main():
    port = 12000
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(('', port))

    print("Servidor iniciado")

    while True:
        data, endereco = server.recvfrom(1024)

        print("Menssagem recebida de", str(endereco))
        print("Recebemos do cliente:", str(data))

        resposta = "Ecoo=>" + str(data)
        server.sendto(data, endereco)

    server.close()


if __name__ == '__main__':
    main()
