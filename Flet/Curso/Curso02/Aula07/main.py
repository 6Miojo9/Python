import flet as ft
import custom_checkbox as cc

def main(page: ft.Page):
    page.title = 'Minhas Tarefas'
    page.window.width = 400
    page.window.height = 650
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)
    
    def add_task(e):
        task_list.controls.append(cc.Checkbox(new_task.value))
        new_task.value = ''
        page.update()
        new_task.focus()
        
    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True, autofocus=True)
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)
    task_list = ft.Column()

    card = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    new_button
                ]
            ),
            task_list
        ]
    )

    page.add(card)


ft.app(target=main)