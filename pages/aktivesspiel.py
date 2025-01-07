import flet as ft

class aktivesspiel(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Stack([
            ft.Container(
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C", "#510A32"]
            ),
            border_radius=10,
            alignment=ft.alignment.center
        ),

         ft.Column(
            spacing=10,
            controls=[
                ft.Container(height=190),

                ft.TextField(
                    label="Code",
                    color="#EE4540",
                    border="underline",
                    hint_text="Code eingeben",
                    hint_style=ft.TextStyle(font_family= "Times New Roman", color= "#EE4540"),
                    label_style=ft.TextStyle(font_family= "Times New Roman", color= "#EE4540"),
                    border_color="#EE4540",
                    width=250,
                    height=50,
                    border_radius=20,
                ),

                ft.Container(
                    content=ft.Text(value="Spiel beitreten", size=20, font_family="Times New Roman", weight="bold", color="#510A32"),
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
            alignment=ft.MainAxisAlignment.CENTER,  
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        ft.Column(
            controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                            ft.Container(
                                content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/neuesspiel")),
                            ),
 
                            ft.Container(
                                content=ft.Text(value="Slot 1", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                                #margin=10,
                                alignment=ft.alignment.center,
                            ),
 
                            # ------ SIDE MENU -------
                            ft.Container(
                                content=ft.PopupMenuButton(
                                    icon=ft.Icons.MENU_SHARP,
                                    icon_color="#EE4540",
                                    bgcolor="#C72C42",
                                    items=[
                                        ft.PopupMenuItem(text="Home", on_click=lambda _: self.page.go("/")),
                                        #ft.PopupMenuItem(text="Rollenübersicht", on_click=self.show_dialog),
                                        ft.PopupMenuItem(text="Spielregeln", on_click=lambda _: self.page.go("/"))
                                    ]
                                ),
                                alignment=ft.alignment.top_right
                            )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_AROUND,
                ),
            ]
        ),
        ])

        return page