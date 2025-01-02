import flet as ft

class Emergency(ft.UserControl):
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
                ft.Container(height=50),
            ft.Container(    
                ft.Column(
                    spacing=0,
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                    ft.Container(),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                ), 
            height=600,
            alignment=ft.alignment.center, 
            ),
                ]
            ), 
            ft.Column(
                controls=[
                    ft.Container(),
                    ft.Row(
                        controls=[
                                ft.Container(
                                    content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),
                                ),
    
                                ft.Container(
                                    content=ft.Text(value="Emergency", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
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
                                            ft.PopupMenuItem(text="Rollenübersicht", on_click=lambda _: self.page.go("/")),
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

            # ft.Column(
            #     controls=[
            #         ft.Container(),
            #         ft.Row(
            #             controls=[
            #                 ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),),
            #                 ft.Container(content=ft.Text(value="Emergency", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
            #                 ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),),
            #             ],
            #             alignment=ft.MainAxisAlignment.SPACE_AROUND,
            #         ),
            #     ]
            #     )
            #     ]
            # )
 

    
    # def show_dialog(self, e):
    #     dialog = ft.AlertDialog(
    #         title=ft.Text("Bist du gestorben?", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
    #         # content=ft.Text("Bist du gestorben?"),
    #         bgcolor="#801336",
    #         actions=[
    #             ft.TextButton(text="Ja", on_click=self.yes_close_dialog, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=20), overlay_color="#EE4540")),
    #             ft.TextButton("Nein", on_click=self.no_close_dialog, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=20), overlay_color="#EE4540"))
    #         ],
    #         actions_alignment="end"
    #     )
    #     self.page.dialog = dialog
    #     dialog.open = True
    #     self.page.update()
 
    # def yes_close_dialog(self, e):
    #     self.page.dialog.open = False
    #     self.page.go("/dead")
    #     self.page.update()

    # def no_close_dialog(self, e):
    #     self.page.dialog.open = False
    #     self.page.update()