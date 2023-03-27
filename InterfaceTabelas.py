import json
import tkinter as tk
from tkinter import ttk

class TabelaTokens(tk.Frame):
    def __init__(self, master, tabela):
        super().__init__(master)
        self.tabela = tabela


        self.tree = ttk.Treeview(self, columns=('identificacao', 'tamanho', 'posicao'))
        self.tree.heading('#0', text='Token')
        self.tree.heading('identificacao', text='Identificação')
        self.tree.heading('tamanho', text='Tamanho')
        self.tree.heading('posicao', text='Posição')


        for item in self.tabela['tokens']:
            self.tree.insert('', 'end', text=item['token'], values=(item['identificacao'], item['tamanho'], item['posicao']))

        self.tree.pack(fill='both', expand=True)

class TabelaIdentificacoes(tk.Frame):
    def __init__(self, master, tabela):
        super().__init__(master)
        self.tabela = tabela


        self.tree = ttk.Treeview(self, columns=('simbolo',))
        self.tree.heading('#0', text='Índice')
        self.tree.heading('simbolo', text='Símbolo')


        for item in self.tabela['identificacoes']:
            self.tree.insert('', 'end', text=item['indice'], values=(item['simbolo'],))

        self.tree.pack(fill='both', expand=True)

class InterfaceTabelas(tk.Tk):
    def __init__(self, tabela):
        super().__init__()
        self.tabela = tabela
        self.title('Tabelas')
        self.geometry('900x400')


        self.notebook = ttk.Notebook(self)
        self.tab_tokens = TabelaTokens(self.notebook, self.tabela)
        self.tab_identificacoes = TabelaIdentificacoes(self.notebook, self.tabela)
        self.notebook.add(self.tab_tokens, text='Tokens')
        self.notebook.add(self.tab_identificacoes, text='Identificações')
        self.notebook.pack(fill='both', expand=True)
        


with open('tabelas.json') as f:
    tabela = json.load(f)


app = InterfaceTabelas(tabela)
app.mainloop()
