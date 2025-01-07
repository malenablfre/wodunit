import flet as ft

class erstelltesspiel(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def show_dialog(self, e):
            dialog = ft.AlertDialog(
                title=ft.Text("Deine Rolle", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=18,)),
                content=ft.Text("Rolle", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=30,)),
                bgcolor="#801336",
                actions=[
                    ft.TextButton(text="OK", on_click=self.close_dialog, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=20), overlay_color="#EE4540")),
                ],
                actions_alignment="end"
            )
            self.page.dialog = dialog
            dialog.open = True
            self.page.update()
 
    def close_dialog(self, e):
        self.page.dialog.open = False
        self.page.go("/erstelltesspiel")
        self.page.update(),

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
                ft.Container(height=80),

                ft.Container(
                    content=ft.Row([
                        ft.Text(value="Dein Code:", size=20, font_family="Times New Roman", weight="bold", color="#510A32", expand=True),
                        ft.Text(value="xyz123", size=20, font_family="Times New Roman", weight="bold", color="#510A32", expand=True)
                    ],
                    alignment=ft.alignment.center
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#C72C42",
                    #border_color="#EE4540",
                    width=250,
                    height=50,
                    border_radius=10,
                ),

                ft.Container(height=5),

                ft.Container(
                    content=ft.Text(value="warten auf Mitspieler...", size=20, font_family="Times New Roman", weight="bold", color="#C72C42"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#510A32",
                    border=ft.border.all(2, "#C72C42"),
                    width=300,
                    height=330,
                    border_radius=10,
                    ink=True,
                    #on_click=lambda _: self.page.go("/spieleinstellungen")
                ),

                ft.Container(
                    content=ft.Text(value="Fertig", size=20, font_family="Times New Roman", weight="bold", color="#510A32"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#C72C42",
                    width=200,
                    height=50,
                    border_radius=20,
                    ink=True,
                    on_click=self.show_dialog,
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
                                content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/spieleinstellungen")),
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
                                        ft.PopupMenuItem(text="Rollenübersicht", on_click=self.show_dialog),
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