import flet as ft

def main(page: ft.page):
    for i in range(100):
        page.controls.append(ft.Text(f"Estamos na linha {i}"))
    page.scroll = "always"
    page.update()

ft.app(target=main)