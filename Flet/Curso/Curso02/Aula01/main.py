import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value='Bem vindo ao Flet!'))
    pass

ft.app(target=main)