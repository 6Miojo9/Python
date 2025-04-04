import flet as ft
import time as tm
import random as rd
import copy as cp
from concurrent.futures import ThreadPoolExecutor

class Processo():
    def __init__(self, tempo):
        self.tempo = tempo
    
class Titulo(ft.Text):
    def __init__(self, valor):
        super().__init__()
        self.size = 20
        self.font_family = ft.FontWeight.W_900
        self.value = valor
        
class Local(ft.Container):
    def __init__(self, tempo):
        super().__init__()
        self.width = 50
        self.height = 50
        self.border = ft.border.all(5,ft.colors.WHITE)
        self.content = ft.Text(value=tempo, size=20)
        self.alignment = ft.alignment.center
        self.tempo = tempo 
              
fila = list()
fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4)
fila.append(5)

def get(index):
        try:
            return fila[index]
        except IndexError:
            return ""
        
pb = ft.ProgressBar(width=50,height=5)
processamento = Local("")
barbeiro = Local("")
entrada = Local("")
saida = Local("")
cad01 = Local(get(0))
cad02 = Local(get(1))
cad03 = Local(get(2))
cad04 = Local(get(3))
cad05 = Local(get(4))


    
def main(page: ft.Page):
    barbeiro.bgcolor = ft.colors.GREEN_600
    processamento.bgcolor = ft.colors.GREEN_600
    
    def executar_tarefas():
        for func in [novo_processo, verificar, processo]:
            executor.submit(func)
            
    page.add(
        ft.Row(
            [
                ft.Container(
                    bgcolor=ft.colors.BLACK87,
                    alignment=ft.alignment.center,
                    expand=True,
                    border=ft.border.all(2, ft.colors.WHITE),
                    border_radius=10,
                ),
                ft.VerticalDivider(width=9, thickness=3),
                ft.Container(
                    bgcolor=ft.colors.BLACK87,
                    alignment=ft.alignment.center,
                    expand=True,
                    border=ft.border.all(2, ft.colors.WHITE),
                    border_radius=10,
                    content=ft.Container(
                        width=500,
                        height=600,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Container( 
                                    alignment=ft.alignment.center,
                                    expand=True,
                                    border=ft.border.only(left=ft.BorderSide(5, ft.colors.WHITE), top=ft.BorderSide(5, ft.colors.WHITE), right=ft.BorderSide(5, ft.colors.WHITE), bottom=None),
                                    content=ft.Column(
                                        width=500,
                                        height=250,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                width=500,
                                                height=50,
                                                alignment=ft.alignment.center,
                                                content=Titulo("Fila de espera")
                                            ),
                                            ft.Container(
                                                width=400,
                                                height=195,
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                                    controls=[
                                                        cad05,
                                                        cad04,
                                                        cad03,
                                                        cad02,
                                                        cad01
                                                    ] 
                                                ),
                                            ),
                                        ]
                                    )
                                    
                                ),
                                ft.Container(
                                    width=500,
                                    height=100,
                                    content=ft.Row(
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                width=150,
                                                height=100,
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        Titulo("Entrada"),
                                                        entrada
                                                    ]
                                                )
                                                
                                            ),
                                            ft.Container(
                                                width=200,
                                                height=100,
                                            ),
                                            ft.Container(
                                                width=150,
                                                height=100,
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        Titulo("Saida"),
                                                        saida
                                                    ]
                                                )
                                            ) 
                                        ]
                                    )
                                ),
                                ft.Container(
                                    width=500,
                                    height=250,
                                    border=ft.border.only(left=ft.BorderSide(5, ft.colors.WHITE), top=None, right=ft.BorderSide(5,ft.colors.WHITE), bottom=ft.BorderSide(5, ft.colors.WHITE)),
                                    content=ft.Row(
                                        vertical_alignment=ft.CrossAxisAlignment.END,
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                width=150,
                                                height=250,
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        Titulo("Barbeiro"),
                                                        barbeiro
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                width=195,
                                                height=160,
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        pb,
                                                        processamento,
                                                        Titulo("Processamento"),
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                width=100,
                                                height=250,
                                            )
                                        ]
                                    ),
                                ),
                            ]
                        )
                    )
                ),
            ],
            spacing=0,
            expand=True,
        )
    )
    
    def sair():
        tm.sleep(1)
        saida.bgcolor = ft.colors.GREEN_600
        page.update()
        tm.sleep(0.5)
        saida.bgcolor = ft.colors.BLACK87
        saida.ocupacao = None
        saida.livre = True
        page.update()
    
    def barra():
        espaco = 1 / processamento.ocupacao.tempo
        for i in range(0,(processamento.ocupacao.tempo+1)):
            pb.value = i * espaco
            processamento.content.value = i
            tm.sleep(1)
            page.update()
        pb.value = 0
        processamento.bgcolor = ft.colors.GREEN_600
        processamento.content.value = ""
        page.update()
        troca(processamento, saida)
        sair()
    
    def processo():
        while True:
            if processamento.livre == False:
                barbeiro.bgcolor = ft.colors.RED_800
                barra()
                barbeiro.bgcolor = ft.colors.GREEN_600
                page.update()
    
    def troca(atual, proximo):
            if atual.livre == False and proximo.livre == True:
                proximo.livre = False
                proximo.ocupacao = cp.deepcopy(atual.ocupacao)
                proximo.bgcolor = ft.colors.BLUE_800
                proximo.content.value = proximo.ocupacao.tempo
                if proximo == saida:
                    saida.content.value = ""
                atual.content.value = ""
                atual.bgcolor = ft.colors.BLACK87
                atual.ocupacao = None
                atual.livre = True
                page.update()
                tm.sleep(0.5)
        
    def verificar():
        while True:
            troca(cad05, cad04)
            troca(cad04, cad03)
            troca(cad03, cad02)
            troca(cad02, cad01)
            troca(cad01, processamento)
            
    def novo_processo():
        while True:
            tm.sleep(rd.randrange(1, 3))
            entrada.bgcolor = ft.colors.BLUE_800
            page.update()
            tm.sleep(0.5)
            
            if len(fila) < 5:
                entrada.bgcolor = ft.colors.GREEN_600
                page.update()
                tm.sleep(0.5)
                fila.append(rd.randrange(4, 9))
                page.update()
            else:
                entrada.bgcolor = ft.colors.RED_800
                page.update()
                tm.sleep(0.5)
                
            entrada.bgcolor = ft.colors.BLACK87
            page.update()
            tm.sleep(0.5)
    
    executor = ThreadPoolExecutor(max_workers=3)
    executar_tarefas()
    
ft.app(main)