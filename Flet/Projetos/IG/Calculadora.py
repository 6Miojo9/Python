import flet as ft

class Display(ft.TextField):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.width = 350
        self.text_align = ft.TextAlign.RIGHT
        self.bgcolor = ft.colors.GREEN_100
        self.color = ft.colors.BLACK
        self.disabled = True
        self.var = None
        self.op = None
        
class Botao_Numero(ft.ElevatedButton):
    def __init__(self, numero, display, page):
        super().__init__()
        self.bgcolor = ft.colors.GREY
        self.color = ft.colors.BLACK
        self.text = numero
        self.on_click = self.num
        self.display = display
        self.page = page
        self.width = 80

    def num(self, e):
        if float(self.display.value) == 0:
            self.display.value = self.text
        else:
            self.display.value += self.text
        self.page.update()    
        
class Botao_Operacao(ft.ElevatedButton):
    def __init__(self, operacao, display, page):
        super().__init__()
        self.bgcolor = ft.colors.BLACK
        self.color = ft.colors.WHITE
        self.text = operacao
        self.on_click = self.opracao
        self.display = display
        self.page = page
        self.width = 80
        if self.text == "=":
            self.bgcolor = ft.colors.BLUE
            self.color = ft.colors.BLACK
    
    def final(self):
        if self.display.op == "+":
            self.display.var += float(self.display.value)
        elif self.display.op == "-":
            self.display.var -= float(self.display.value)
        elif self.display.op == "x":
            self.display.var *= float(self.display.value)
        elif self.display.op == "/":
            self.display.var /= float(self.display.value)
        self.display.op = self.text
        self.display.value = "0"
        
    def opracao(self, e):
        if self.text == "=":
            self.final()
            self.display.value = self.display.var
        else:
            if self.display.var == None:
                self.display.var = float(self.display.value)
                self.display.op = self.text
                self.display.value = "0"
            else:
                self.final()
        self.page.update()

class Botao_Clear(ft.ElevatedButton):
    def __init__(self, texto, display, page):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.BLACK
        self.text = texto
        self.display = display
        self.page = page
        self.on_click = self.clear
        self.width = 80
        
    def clear(self, e):
        self.display.var = None
        self.display.op = None
        self.display.value = "0"
        self.page.update()
        
def main(page: ft.Page):
    display = Display("0")
    page.window_width = 385
    page.window_height = 280
    page.add(
        ft.Column([
            ft.Row([
                display
            ]),
            ft.Row([
                Botao_Numero("1", display, page),
                Botao_Numero("2", display, page),
                Botao_Numero("3", display, page),
                Botao_Operacao("+", display, page)
            ]),
            ft.Row([
                Botao_Numero("4", display, page),
                Botao_Numero("5", display, page),
                Botao_Numero("6", display, page),
                Botao_Operacao("-", display, page)
            ]),
            ft.Row([
                Botao_Numero("7", display, page),
                Botao_Numero("8", display, page),
                Botao_Numero("9", display, page),
                Botao_Operacao("x", display, page)
            ]),
            ft.Row([
                Botao_Clear("A/C", display, page),
                Botao_Numero("0", display, page),
                Botao_Operacao("=", display, page),
                Botao_Operacao("/", display, page)
            ]),
        ])
    )

ft.app(main)