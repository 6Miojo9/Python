from flet import *

def main(page:Page):
    page.add(
        Text("Ola mundo", size=30, color="red"),
        Container(
            width=400,
            height=200,
            bgcolor=colors.AMBER
        ),
        TextField()
    )
    pass

app(target=main)