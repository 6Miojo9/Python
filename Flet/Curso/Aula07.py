import flet as ft

def main(page: ft.Page):
    page.title = "Apicação teste"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.update()
    
ft.app(target=main)