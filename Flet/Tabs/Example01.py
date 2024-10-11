from flet import *

def main(page: Page):
    table = Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            Tab(
                text="Contatos"
            ),
            Tab(
                text="Adicionar"
            )
        ]        
    )
    page.add(table)

app(main)