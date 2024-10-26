from flet import *
import sqlite3

conexao = sqlite3.connect("dados.db", check_same_thread=False)
cursor = conexao.cursor()

def tabela_base():
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT)""")

class App(UserControl):
    def __init__(self):
        super().__init__()
        tabela_base()
        self.todos_dados = Column(auto_scroll=True)
        self.add_dados = TextField(label="Nome do dado")
        self.editar_dado = TextField(label="Editar dado")
    
    def deletar(self, x, y):
        cursor.execute("DELETE FROM clientes WHERE id = ?", [x])
        y.open = False
        
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()
    
    def atualizar(self, x, y, z):
        cursor.execute('UPDATE clientes SET nome = ? WHERE id = ?', (y, x))
        conexao.commit()
        
        z.open = False
        
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()
    
    def abrir_acoes(self, e):
        id = e.control.subtitle.value
        self.editar_dado.value = e.control.title.value
        self.update()
        
        alert_dialogo = AlertDialog(
            title=Text(f"Editar ID {id}"),
            content=self.editar_dado,
            
            actions=[
                ElevatedButton(
                    'Deletar',
                    color='white', bgcolor='red',
                    on_click=lambda e:self.deletar(id, alert_dialogo)
                ),
                ElevatedButton(
                    'Atualizar',
                    on_click=lambda e:self.atualizar(id, self.editar_dado.value, alert_dialogo)
                )
            ],
            actions_alignment='spaceBetween'
        )
        
        self.page.dialog = alert_dialogo
        alert_dialogo.open = True
        
        self.page.update()
        
    def renderizar_todos(self):
        cursor.execute("SELECT * FROM clientes")
        conexao.commit()
        
        meus_dados = cursor.fetchall()
        
        for dado in meus_dados:
            self.todos_dados.controls.append(
                ListTile(
                    subtitle=Text(dado[0]),
                    title=Text(dado[1]),
                    on_click=self.abrir_acoes
                )
            )
        self.update()
        
    def ciclo(self):
        self.renderizar_todos()
        
    def adicionar_dado(self, e):
        cursor.execute("INSERT INTO clientes (nome) VALUES (?)", [self.add_dados.value])
        conexao.commit()
        
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()

        
    def build(self):
        return Column(
            [
                Text("Lista:", size=20, weight='bold'),
                self.add_dados,
                ElevatedButton(
                    'Adicionar dado', on_click=self.adicionar_dado,
                ),
                self.todos_dados
            ]
        )

def main(page: Page):
    page.update()
    minha_aplicacao = App()
    
    page.add(
        minha_aplicacao,
    )

app(target=main)