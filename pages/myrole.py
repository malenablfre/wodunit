import flet as ft

class role(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.role = "Unschuldig"
        self.description = "Du bist ein normaler Teilnehmer ohne besondere Fähigkeiten. Dein Ziel ist es, die Mörder zu entlarven und zu eliminieren."

    def build(self):
        page = ft.Stack([
        ft.Container(
                ft.Column(
                spacing=0,
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    
                    ft.Container(
                        content=ft.Text(value=self.role, size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                        padding=10,
                    ),

                    ft.Container(
                        content=ft.Text(value=self.description, size= 15, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.TRANSPARENT,
                        border=ft.border.all(width=1, color="#C72C42"),
                        width=250,
                        height=110,
                        border_radius=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Notizen", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                        padding=10,
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
                    ),

                    ft.Container(
                        content=ft.Text(value="Übersicht", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=
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
            ),

            # ft.AppBar(
            #     leading=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),
            #     leading_width=40,
            #     title=ft.Text(value="Meine Rolle", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
            #     center_title=True
            # ),
        ft.Column(
            controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                        ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),),
                        ft.Container(content=ft.Text(value="Meine Rolle", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
                        ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        )
        ])
        

        return page