'''
Faça um programa que:
a.	Solicite ao usuário que digite o nome de um arquivo texto (caminho completo);
b.	Solicite ao usuário que digite uma palavra;
c.	Verifique em todo arquivo quais as linhas contêm a palavra. Todas as linhas localizadas devem ser salvas em um novo arquivo texto com o nome FIND_<nome_arquivo_original>, contendo o seguinte:
'''

def escreverArquivo(path, palavraChave):
    arquivo = open(path, 'r')
    newFile = open('FIND_' + path, 'w')
    for l_num, line in enumerate(arquivo, 1):
        if(palavraChave in line):
            newFile.writelines("[" + str(l_num) + "] " + line)
    newFile.close()
    arquivo.close()


path = input('Digite o caminho completo do arquivo: ')
palavraChave = input('Digite uma palavra: ')