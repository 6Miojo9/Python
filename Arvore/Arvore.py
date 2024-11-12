import flet as ft

class Arvore(): # Classes que cria da arvore e da raiz.
    def __init__(self, raiz):
        self.raiz = No(raiz) # Define a raiz com um novo Nó.
    
class No: # Classe que cria e adiciona novos Nós.
    def __init__(self, valor):
        self.valor = valor # Valor do Nó
        self.esquerda = None # Ponteiro para a esquerda.
        self.direita = None # Ponteiro para a direita.
        self.nivel = 1 # Nivel do Nó (inicial: 1).
    
    def direito(self, valor): # Cria e adiciona o novo Nó para o ponteiro direito.
        self.direita = No(valor) # Define o novo no com o valor para a direito.
        self.nivel += self.direita.nivel # Adiciona o novo nivel para o Nó pai.
        
    def esquerdo(self, valor): # Cria e adiciona o novo Nó para o ponteiro esquerdo.
        self.esquerda = No(valor) # Define o novo no com o valor para a esquerda.
        self.nivel += self.esquerda.nivel # Adiciona o novo nivel para o Nó pai.
    
    def novo_no(self, valor): # Função que decide a criação e direção de um novo Nó.
        if valor >= self.valor and self.direita == None:
            self.direito(valor) # Chama a função para o ponteiro direito.
        elif valor >= self.valor:
            self.direita.novo_no(valor) # Re-chama a função para adicionar o Nó para o no filho já apontado para a direita.
        elif valor <= self.valor and self.esquerda == None:
            self.esquerdo(valor) # Chama a função para o ponteiro esquerdo.
        elif valor <= self.valor:
            self.esquerda.novo_no(valor) # Re-chama a função para adicionar o Nó para o no filho já apontado para a esquerda.
        
        if self.direita.nivel > (self.esquerda.nivel + 1) or (self.direita.nivel >= 2 and self.esquerda.nivel == None):
            print(f"O direito é maior {self.direita.nivel}.")
        elif self.esquerda.nivel > (self.direita.nivel + 1) or (self.esquerda.nivel >= 2 and self.direita.nivel == None):
            print(f"O esquerdo é maior {self.esquerda.nivel}.")
        else:
            print(f"Os dos são iguais: direita {self.direita.nivel}, esquerda: {self.esquerda.nivel}.")

arvore = Arvore(int(input("Digite o primeiro no"))) #Variavel que guarda a arvore

for i in range(6):
    arvore.raiz.novo_no(int(input("Digite:"))) # Recebe o valor para o novo Nó e insere a partir da raiz até a posição correta na arvore.


# def main(page: ft.Page):
#     entrada_no = ft.TextField(label="Digite o valor:")
#     page.add(
#         entrada_no
#     )

# ft.app(target=main)