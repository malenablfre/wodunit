import flet as ft

class gameslots(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Stack(
            controls=[
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
                                    # ----- ZWEIE ÜBERSCHRIFT -----
                                    ft.Container(
                                        content=ft.Text(value="Spiel beitreten:", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                                        margin=0,
                                        alignment=ft.alignment.center
                                    ),

                                    # ----- SPIELSLOTS -----
                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            text="Slot 1", 
                                            style=ft.ButtonStyle(
                                                alignment=ft.alignment.center,
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                color="#EE4540", 
                                                bgcolor="#510A32", 
                                                text_style=ft.TextStyle(size= 20, font_family= "Times New Roman", weight= "bold"), 
                                                overlay_color="#801336"
                                            ),
                                            width=250,
                                            height=50,
                                            on_click=lambda e: self.page.go("/home")
                                        ),
                                        margin=10
                                    ),

                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            text="Slot 2", 
                                            style=ft.ButtonStyle(
                                                alignment=ft.alignment.center,
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                color="#EE4540", 
                                                bgcolor="#510A32", 
                                                text_style=ft.TextStyle(size= 20, font_family= "Times New Roman", weight= "bold"), 
                                                overlay_color="#801336"
                                            ),
                                            width=250,
                                            height=50,
                                            on_click=lambda e: self.page.go("/home")
                                        ),
                                        margin=10
                                    ),

                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            text="Slot 3", 
                                            style=ft.ButtonStyle(
                                                alignment=ft.alignment.center,
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                color="#EE4540", 
                                                bgcolor="#510A32", 
                                                text_style=ft.TextStyle(size= 20, font_family= "Times New Roman", weight= "bold"), 
                                                overlay_color="#801336"
                                            ),
                                            width=250,
                                            height=50,
                                            on_click=lambda e: self.page.go("/home")
                                        ),
                                        margin=10
                                    )
                                    
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            height=600,
                            alignment=ft.alignment.center,
                        )
                    ],
                ),

                # ----- HEADER -----
                ft.Column(
                    controls=[
                        ft.Container(
                            content=
                                ft.Row(
                                    controls=[
                                            ft.Container(
                                                content=ft.IconButton(
                                                    ft.Icons.ARROW_BACK,
                                                    icon_color="#EE4540",
                                                    hover_color= ft.Colors.with_opacity(0.1, "#C72C42"),
                                                    highlight_color= ft.Colors.with_opacity(0.5, "#C72C42"),
                                                    on_click=lambda _: self.page.go("/"),  
                                                ),
                                            ),
                
                                            ft.Container(
                                                content=ft.Text(
                                                    value="Deine Spiele",
                                                    size= 30,
                                                    font_family= "Times New Roman",
                                                    weight= "bold",
                                                    color="#EE4540"
                                                ),
                                            ),
                
                                            # ------ SIDE MENU ------
                                            ft.Container(
                                                content=ft.PopupMenuButton(
                                                    icon=ft.Icons.MENU_SHARP,
                                                    icon_color="#EE4540",
                                                    bgcolor="#C72C42",
                                                    items=[
                                                        ft.PopupMenuItem(text="Startseite", on_click=lambda _: self.page.go("/")),
                                                        ft.PopupMenuItem(text="Home", on_click=lambda _: self.page.go("/home")),
                                                        ft.PopupMenuItem(text="Rollenübersicht", on_click=lambda _: self.page.go("/rollenuebersicht")),
                                                        ft.PopupMenuItem(text="Spielregeln", on_click=lambda _: self.page.go("/spielregeln"))
                                                    ]
                                                ),
                                            )
                                    ],
                                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            margin=10,
                            #alignment=ft.alignment.top_center
                        ),
                    ]
                ),
            ]
        )

        return page