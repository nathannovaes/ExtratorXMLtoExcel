from listaProdutos import *
pisconfins = ''
def tratamentoProdutos(listaB, data, nome, municipio, numNF, natureza,pisconfins, Venc):
    repeticao = []
    retiraRep = []
    excluir = []
    # Função que encontra os forncedores e os cfops iguais
    i = 0
    j = 0
    for i in range(len(listaB)):
        for j in range(len(listaB)):
            if j > i:
                if listaB[i][0] == listaB[j][0] and listaB[i][1] == listaB[j][1]:
                    repeticao.append((i,j))


    # Função que excluir as repetições na lista
    i = 0
    while i < len(excluir):
        repeticao.pop(excluir[i])
        i+=1

    # Faz a soma dos valores e substitui na casa onde apareceu a primeira vez o fornecedor
    i = 0
    j = 0
    print(repeticao)

    for i in range(len(repeticao)):
        # Calcula o valor do imposto
        vICMS = float(listaB[repeticao[i][0]][2]) + float(listaB[repeticao[i][1]][2])

        # Calcula o valor do produto
        vProd = float(listaB[repeticao[i][0]][3]) + float(listaB[repeticao[i][1]][3])

        # Monta o novo registro do fornecedor. Os valores já entram formatados ".2f"
        novoValor = (listaB[repeticao[i][0]][0], listaB[repeticao[i][0]][1], '{:0,.2f}'.format(vICMS), '{:0,.2f}'.format(vProd))

        # Remove o fornecedor do primeiro lugar onde aparecer na lista
        listaB.pop(repeticao[i][0])

        # Insere na lista o fornecedor novamente com os valores atualizados
        listaB.insert(repeticao[i][0], novoValor)

    # Exibe a lista
    print(listaB)



    # Retira número duplicados de uma lista
    i = 0
    for i in range(len(repeticao)):
        if repeticao[i][1] not in retiraRep:
            retiraRep.append(repeticao[i][1])


    # Cria uma lista com todas as posições do array
    i = 0
    j = 0
    resposta = []
    for i in range(len(listaB)):
        resposta.append(i)
    '''
    Faz uma comparação entre o que precisa ser retirado "retiraRep", pois está duplicado.
    Depois passa a comparar com a lista "resposta" e cria a lista respostaFinal, que contém
    somente as posições necessárias.
    '''
    respostaFinal = [posicao for posicao in resposta if posicao not in retiraRep]


    for i in range(len(respostaFinal)):
        listaProdutos(data, nome, municipio, numNF, 'Devolução' ,natureza, listaB[respostaFinal[i]][0], listaB[respostaFinal[i]][1], pisconfins, listaB[respostaFinal[i]][2], '0', listaB[respostaFinal[i]][3], Venc)