import flet as ft

class home(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Container(
                ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        content=ft.Text(value="Whodunit?", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        margin=10,
                        padding=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Das Spiel des Mörders", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                        padding=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Emergency2", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        on_click=lambda _: self.page.go("/Emergency2")
                    ),

                    ft.Container(
                        content=ft.Text(value="Spiel beitreten", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=
                    ),

                    ft.Container(
                        content=ft.Text(value="Emergency", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        on_click=lambda _: self.page.go("/Emergency")
                    ),
                ],
                alignment = ft.MainAxisAlignment.CENTER,
            ),
            width=400,
            height=700,
            #bgcolor="#2D142C",
            #gradient=ft.RadialGradient(["#2D142C","#510A32"]),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C","#510A32"]),
            border_radius=10,
            alignment=ft.alignment.center
            )
        return page