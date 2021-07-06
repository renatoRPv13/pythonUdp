from socket import *


def main():
    host = "127.0.0.1"
    port = 12000
    server = (host, port)
    conexao = socket(AF_INET, SOCK_DGRAM)
    conexao.bind((host, port))

    msg = input("#$: ")
    while msg == 'renato':
        conexao.sendto(msg.encode(), server)

        data, endereco = conexao.recvfrom(1024)

        print("Recebida ->", str(data))

        msg = input("-> ")

    conexao.close()


if __name__ == '__main__':
    main()
