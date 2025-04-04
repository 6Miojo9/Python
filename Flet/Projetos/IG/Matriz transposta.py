import flet as ft

class Celula(ft.TextField):
    def __init__(self, coluna, linha):
        super().__init__()
        self.height = 50
        self.width = 50
        self.color = ft.colors.WHITE
        self.bgcolor = ft.colors.BLACK
        self.text_align = ft.TextAlign.CENTER
        self.coluna = coluna
        self.linha = linha
        
    def corpo(self):
        self.bgcolor = ft.colors.GREY
        self.content = ft.Text("")

class Linha(ft.Row):
    def __init__(self, y, x):
        super().__init__()
        self.y = y
        self.x = x
        for i in range(0, self.x):
            self.controls += [Celula(i, self.y)]

class Tabuleiro(ft.Column):
    def __init__(self, x, y):
        super().__init__()
        self.y = y
        self.x = x
        for i in range(0, self.y):
            self.controls += [Linha(i, self.x)]

class Botao(ft.ElevatedButton):
    def __init__(self, text, x, y, page):
        super().__init__()
        self.text = text
        self.page = page
        self.x = x
        self.y = y
        self.on_click = self.criar_matriz
        self.tab
        
    def criar_matriz(self):
       self.tab = Tabuleiro(self.x, self.y)
       self.page.add(self.tab)
       self.update()
    
def main(page: ft.Page):
    x = ft.TextField(label="X", value=0)
    y = ft.TextField(label="Y", value=0)
    bot = Botao("Executar", x, y, page)
    page.add(
        ft.Column([
            ft.Row([
                x,
                y,
                bot
            ]),
        ])
    )

ft.app(main)