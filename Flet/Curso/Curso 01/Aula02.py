import flet as ft

def main(page):
    
    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor, preencha o seu nome!"
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Por favor, preencha a sua senha!"
            page.update()
        elif entrada_nome.value != "Gadyel" and entrada_senha.value != "1234":
            saida.value = "Credenciais invalidas"
            page.add(saida)
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")
            
            page.clean()
            page.add(ft.Text(f"Ola {nome}\nSeja bem vindo a nossa aplicação"))
    
    def apagar_erro(e):
        entrada_nome.error_text = ""
        entrada_senha.error_text = ""
        page.update()
    
    entrada_nome = ft.TextField(label="Digite o seu nome:", on_focus=apagar_erro)
    entrada_senha = ft.TextField(label="Digite a sua senha:", on_focus=apagar_erro)
    saida = ft.Text()
    
    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Logar", on_click=login),
    )
    
ft.app(target=main)