import flet as ft
import random as rd
import time as tm

RANGE = 16

class Celula(ft.Container):
    def __init__(self, coluna, linha):
        super().__init__()
        self.height = 30
        self.width = 30
        self.color = ft.colors.BLACK
        self.bgcolor = ft.colors.GREY
        self.content = ft.Text(text_align=ft.TextAlign.CENTER)
        self.tamanho = 0
        self.coluna = coluna
        self.linha = linha
        
    def corpo(self):
        self.bgcolor = ft.colors.GREY
        self.content = ft.Text("")

class Linha(ft.Row):
    def __init__(self, linha):
        super().__init__()
        self.linha = linha
        for i in range(0, RANGE):
            self.controls += [Celula(i, linha)]

class Tabuleiro(ft.Column):
    def __init__(self):
        super().__init__()
        for i in range(0, RANGE):
            self.controls += [Linha(i)]

class Cobra():
    def __init__(self, tab, page, troca, fruta):
        super().__init__()
        self.tab = tab
        self.page = page
        self.troca = troca
        self.ant = troca
        self.posx = 0
        self.posy = 2
        self.posit = self.tab.controls[self.posy].controls[self.posx]
        self.fruta = fruta
        self.tamanho = 1
        self.aux = 0
        self.corpo = list()
        self.propriedades_posicao()

    def direcao(self):
        while True:
            match self.ant:
                case "d":
                    if self.troca == "e":
                        self.troca = "d"
                case "e":
                    if self.troca == "d":
                        self.troca = "e"
                case "b":
                    if self.troca == "c":
                        self.troca = "b"
                case "c":
                    if self.troca == "b":
                        self.troca = "c"
                                           
            match self.troca:
                case "d":
                    self.posx += 1
                case "e":
                    self.posx -= 1
                case "b":
                    self.posy += 1
                case "c":
                    self.posy -= 1
            self.ant = self.troca
            self.move()

    def move(self):
        tm.sleep(0.5)
        self.corpo.append(self.posit)
        self.posit.tamanho = self.tamanho
        self.posit = self.tab.controls[self.posy].controls[self.posx]
        self.propriedades_posicao()
        self.page.update()
        
    def comp(self):
        print("corpo")
        for i in self.corpo:
            print("linha: " + str(i.linha) + "; Coluna: " + str(i.coluna) + ": " + str(i.tamanho))
            i.tamanho -= 1
            if i.tamanho == 0:
                i.corpo()
                del(self.corpo[0])

    def propriedades_posicao(self):
        if self.posit.bgcolor == ft.colors.RED:
            self.tamanho += 1
            self.fruta.trocar()
            
        self.posit.bgcolor = ft.colors.GREEN
        self.comp()
            
class Fruta():
    def __init__(self, tab, page):
        super().__init__()
        self.tab = tab
        self.page = page
        self.celula = self.tab.controls[rd.randrange(0, RANGE)].controls[rd.randrange(0, RANGE)]
        self.trocar()
    
    def trocar(self):
        match self.celula.bgcolor:
            case ft.colors.RED:
                self.celula = self.tab.controls[rd.randrange(0, RANGE)].controls[rd.randrange(0, RANGE)]
                self.trocar()
            case ft.colors.GREEN:
                self.celula = self.tab.controls[rd.randrange(0, RANGE)].controls[rd.randrange(0, RANGE)]
                self.trocar()
            case ft.colors.GREY:
                self.celula.bgcolor = ft.colors.RED
        self.page.update()
    
def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    troca = "d"
    tab = Tabuleiro()
    fruta = Fruta(tab, page)
    cobra = Cobra(tab, page, troca, fruta)
    def teclado_evento(evento: ft.KeyboardEvent):
        match evento.key:
            case "W":
                cobra.troca = "c"
            case "A":
                cobra.troca = "e"
            case "S":
                cobra.troca = "b"
            case "D":
                cobra.troca = "d"
        page.update()
    page.on_keyboard_event = teclado_evento
    page.add(
        tab
    )
    cobra.direcao()
    
ft.app(main)