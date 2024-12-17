import flet as ft

class spieleinstellungen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        back_container = ft.Container(
            content=ft.Text(value="↩", size=20, font_family="Times New Roman", weight="bold", color="#C72C42"),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor="#510A32",
            width=50,
            height=50,
            border_radius=10,
            ink=True,
            on_click=lambda _: self.page.go("/neuesspiel")
        )

        other_containers = ft.Column(
              spacing=10,
              controls=[
                   ft.Container(
                        content=ft.Text(value="Einstellungen", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        margin=10,
                        padding=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Anzahl der Spieler", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=lambda _: self.page.go("/spieleinstellungen")
                    ),

                    ft.Container(
                        content=ft.Text(value="...", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=lambda _: self.page.go("/spieleinstellungen")
                    ),

                    ft.Container(
                        content=ft.Text(value="Spiel erstellen", size= 20, font_family= "Times New Roman", weight= "bold", color="#510A32"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#C72C42",
                        width=250,
                        height=50,
                        border_radius=20,
                        ink=True,
                        on_click=lambda _: self.page.go("/erstelltesspiel")
                    ),
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        
        background_container = ft.Container(
            content=other_containers,
            width=400,
            height=700,
            #bgcolor="#2D142C",
            #gradient=ft.RadialGradient(["#2D142C","#510A32"]),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C","#510A32"]
            ),
            border_radius=10,
            alignment=ft.alignment.center
        )

        page = ft.Stack(
            controls=[
                background_container,  
                back_container,
            ]
        )

        return page