import socket


def checkFileExistance(arquivo):
    try:
        with open("D:/" + arquivo + '.txt', 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False


def lerArquivo(arquivo):
    f = open("D:/" + arquivo + '.txt', 'r')
    return f.read()


def main():
    ip = ''
    porta = 7000
    endereco = (ip, porta)
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind(endereco)
    serv_socket.listen(5)
    print('aguardando conexao')
    con, cliente = serv_socket.accept()
    print('conectado')
    print('aguardando mensagem')
    recebe = con.recv(1024)
    arquivo = checkFileExistance(recebe.decode('utf-8'))
    if(arquivo):
        print('Arquivo existe')
        lista = lerArquivo(recebe.decode('utf-8'))
        con.send(lista.encode())

    else:
        print('Arquivo não existe')

    serv_socket.close()


main()
