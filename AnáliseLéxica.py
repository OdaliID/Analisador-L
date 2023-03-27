import json

reservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminador = [';']
identificadores = ['i', 'j']

def procura(item):
    if item in reservadas:
        return 'Palavra reservada'
    elif item in operadores:
        return 'Operador'
    elif item in terminador:
        return 'Terminador'
    elif item in identificadores:
        return 'Identificador'
    else:
        return 'Constante'

def pesquisa(token, lista):
    for item in lista:
        if token in item:
            return True
    return False

def traduz(linha):
    itens = linha.replace(';', ' ;').split(' ')

    tabela = {
        'tokens': [],
        'identificacoes': [],
    }

    listaIdent = []
    listaAtual = []
    for i in range(len(itens)):
        token = itens[i]
        identificacao = procura(itens[i])
        if identificacao == 'Constante' or identificacao == 'Identificador':
            if not pesquisa(token, listaIdent):
                listaIdent.append([token, identificacao])
                identificacao = [identificacao, len(listaIdent)]
            else:
                for i, item in enumerate(listaIdent):
                    if item[1] == identificacao and item[0] == token:
                        identificacao = [item[1], i+1]
        tamanho = len(itens[i])
        posicao = 0
        if listaAtual:
            if len(listaAtual) == 1:
                posicao = linha.find(token, len(listaAtual[0])+1)
            else:
                posicao = linha.find(token, listaAtual[-1][1]+1)
        listaAtual.append([token, posicao])
        if token == ';':
            tabela['tokens'].append({
                'token': token,
                'identificacao': 'Terminador',
                'tamanho': tamanho,
                'posicao': '(0,{})'.format(posicao)
            })
        else:
            tabela['tokens'].append({
                'token': token,
                'identificacao': identificacao,
                'tamanho': tamanho,
                'posicao': '(0,{})'.format(posicao)
            })

    for item in listaIdent:
        tabela['identificacoes'].append({
            'indice': listaIdent.index(item)+1,
            'simbolo': item[0]
        })

    with open('tabelas.json', 'w') as f:
        json.dump(tabela, f, indent=4)



with open('codigo.txt', 'r') as arquivo:

    linha = arquivo.read()


traduz(linha)