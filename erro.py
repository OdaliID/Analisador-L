import re
import tkinter as tk

def analisador_lexico(linha):
    itens = re.findall(r'\S+|\s+', linha.replace(';', ' ;'))
    for token in itens:
        if '  ' in token:
            return 'Erro léxico: espaço vazio encontrado entre tokens'
    return 'Análise léxica concluída com sucesso'

def analisar():
    linha = entrada.get()
    mensagem = analisador_lexico(linha)
    resultado.config(text=mensagem)

janela = tk.Tk()
janela.title('Analisador Léxico')

titulo = tk.Label(janela, text='Digite a linha a ser analisada:')
titulo.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text='Analisar', command=analisar)
botao.pack()

resultado = tk.Label(janela, text='')
resultado.pack()

janela.mainloop()
