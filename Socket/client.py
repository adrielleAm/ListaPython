import socket


def escreverArquivo(texto):
    arquivo = open('D:/textoClient.txt', 'w')
    arquivo.write(texto.decode('utf-8'))
    arquivo.close()


def solicitarConexao(msg):
    ip = '127.0.0.1'
    porta = 7000
    endereco = (ip, porta)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(endereco)
    client_socket.send(msg.encode())
    print('mensagem enviada')
    recv = client_socket.recv(1024)
    escreverArquivo(recv)
    print('mensagem recebida')
    client_socket.close()


def main():
    arquivo = input("Digite o nome do arquivo:")
    solicitarConexao(arquivo)


main()
