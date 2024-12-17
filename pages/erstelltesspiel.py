import flet as ft
import random
import string

class erstelltesspiel(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.modal_container = None

    def generate_code(self):
        characters = string.ascii_uppercase + string.digits  
        code = ''.join(random.choice(characters) for _ in range(5)) 
        return code

    def show_modal(self):
        code = self.generate_code() 
        code_text = ft.Text(value=f"Generierter Code: {code}", size=20, weight="bold", color="#EE4540")

        self.modal_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=code_text,
                        padding=20,
                        bgcolor="#510A32",
                        border_radius=10,
                        alignment=ft.alignment.center,
                        width=300,
                        height=150,
                    ),
                    ft.ElevatedButton(
                        content=ft.Text("Schließen"),
                        on_click=self.close_modal,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=400,
            height=300,
            bgcolor="rgba(0, 0, 0, 0.7)", 
            alignment=ft.alignment.center,
        )

        self.page.add(self.modal_container)
        self.page.update() 

    def close_modal(self, e):
        self.page.remove(self.modal_container)
        self.page.update()

    def build(self):
        container = ft.Container(
            content=ft.Text(value="Klicke hier, um Code zu generieren!", size=20, weight="bold", color="#C72C42"),
            width=300,
            height=100,
            bgcolor="#510A32",
            border_radius=10,
            alignment=ft.alignment.center,
            ink=True, 
            on_click=lambda _: self.show_modal(), 
        )

        background_container = ft.Container(
            content=container,
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C", "#510A32"]
            ),
            border_radius=10,
            alignment=ft.alignment.center
        )

        page = ft.Stack(
            controls=[background_container] 
        )

        return page
