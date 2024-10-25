from flet import *

def main(page: Page):
    table = Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            Tab(
                text = "Contatos",
                content = Container(
                    content = Text(value="pasta 01"), alignment=alignment.center
                ),
            ),
            Tab(
                text="Adicionar",
                content = Container(
                    content = Text(value="pasta 02"), alignment=alignment.center
                ),
            ),
        ],
        expand=1,
    )
    page.add(table)
app(main)