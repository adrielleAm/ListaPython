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

