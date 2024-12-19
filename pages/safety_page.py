import flet as ft

class safety(ft.UserControl):
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
                colors=["#2D142C","#510A32"]),
            border_radius=10,
            alignment=ft.alignment.center
            ),
        
        ft.Column(
            controls=[
                ft.Container(height=200),
                ft.Container(
                    content=ft.Text(value="Bist du sicher, dass niemand auf deinen Bildschirm schauen kann?", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        margin=ft.margin.only(left=50, right=50),
                        padding=10,
                ),
                ft.Container(
                    content=
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Ja",
                                    style=ft.ButtonStyle(
                                    color="#EE4540",
                                    bgcolor="#510A32",
                                    text_style=ft.TextStyle(
                                        font_family= "Times New Roman",
                                        size=20,
                                        color="#EE4540"
                                    ),
                                    overlay_color="#801336",),
                                    on_click=lambda _: self.page.go("/role")),
                                ft.ElevatedButton(
                                    text="Nein",
                                    style=ft.ButtonStyle(
                                    color="#EE4540",
                                    bgcolor="#510A32",
                                    text_style=ft.TextStyle(
                                        font_family= "Times New Roman",
                                        size=20,
                                        color="#EE4540"
                                    ),
                                    overlay_color="#801336"),
                                    on_click=lambda _: self.page.go("/"))
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        ),
                        margin=ft.margin.only(left=50, right=50),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),

        ft.Column(
            controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                        ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),),
                        ft.Container(width=150),
                        ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        
        
        ])
        return page
    

    # alert dialog als safety check
    def show_dialog(self, e):
        dialog = ft.AlertDialog(
            title=ft.Text("Achtung!", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
            content=ft.Text("Bist du sicher, dass niemand deine Bildschirm sehen kann?", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
            bgcolor="#801336",
            actions=[
                ft.TextButton(text="Ja", on_click=self.yes_close_dialog, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=20), overlay_color="#EE4540")),
                ft.TextButton("Nein", on_click=self.no_close_dialog, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=20), overlay_color="#EE4540"))
            ],
            actions_alignment="end"
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def yes_close_dialog(self, e):
        self.page.dialog.open = False
        self.page.go("/role")
        self.page.update()

    def no_close_dialog(self, e):
        self.page.dialog.open = False
        self.page.update()