import time as tm
import flet as ft

class Display(ft.TextField):
    def __init__(self, value, page):
        super().__init__()
        self.bgcolor = ft.colors.PINK_100
        self.color = ft.colors.BLACK
        self.__text_align = ft.TextAlign.CENTER
        self.text_size = 20
        self.width = 150
        self.value = value
        self.disabled = True
        self.milisegundos = 0
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.page = page
    
    def iniciar(self):
        self.milisegundos += 1
        if self.milisegundos == 1000:
            self.segundos += 1
            if self.segundos == 60:
                self.minutos += 1
                if self.minutos == 60:
                    self.horas += 1
                    self.minutos = 0
                self.segundos = 0
            self.milisegundos = 0
        
        self.value = str(self.horas).zfill(2) + ":" + str(self.minutos).zfill(2) + ":" + str(self.segundos).zfill(2) + ":" + str(self.milisegundos).zfill(3)
    
def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 200
    page.window.height = 200
    
    display = Display("", page)
    
    page.add(
        ft.Column([
            display
        ])
    )
    page.update()
    
    while True:
        tm.sleep(0.0001)
        display.iniciar()
        page.update()

ft.app(main)