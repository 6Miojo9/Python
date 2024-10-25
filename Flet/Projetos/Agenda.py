from flet import *

def main(page: Page):
    
    def Adicionar(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor, preencha o nome!"
            page.update()
    
    def apagar_erro(e):
        entrada_nome.error_text = ""
        page.update()
    
    entrada_nome = TextField(label="Nome:", on_focus=apagar_erro)
    entrada_sobrenome = TextField(label="Sobrenome:")
    entrada_numero = TextField(label="Número:", on_focus=apagar_erro)
    aprovar = ElevatedButton("Adicionar", on_click=Adicionar)
    
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
                    Column(
                        [
                            Container(
                                content = entrada_nome, alignment=alignment.center,
                            ),
                            Container(
                                content = entrada_sobrenome, alignment=alignment.center,
                            ),
                            Container(
                                content = entrada_numero, alignment=alignment.center,
                            ),
                            Container(
                                content = aprovar, alignment=alignment.center,
                            ),
                        ],
                    ),
                )
            ),
        ],
        expand=1,
    )
    
    page.add(table)

app(main)