import flet as ft

def main(page: ft.page):
    ola = ft.Text(value="Ola, mundo!")
    page.controls.append(ola)
    page.update()

ft.app(target=main)