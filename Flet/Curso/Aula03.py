import flet as ft

def app(page: ft.Page):
    
    def tecla(e: ft.KeyboardEvent):
        page.add(
            ft.Text(f"Tecla pressionada: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}")
        )
        if e.key == "A":
            page.add(
                ft.Text("a")
            )
    page.on_keyboard_event = tecla
    
    page.add(
        ft.Text("Pressione qualquer tecla ou uma combinação de teclas")
    )
ft.app(target=app)