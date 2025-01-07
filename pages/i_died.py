import flet as ft

class dead(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.place_of_death: ft.TextField = ft.TextField(
            autofocus= True,
            hint_text="Tippe den Ort...",
            hint_style=ft.TextStyle(
                font_family= "Times New Roman",
                color="#C72C42"
            ),
            text_style=ft.TextStyle(
                font_family= "Times New Roman",
                color="#EE4540"
            ),
            text_align=ft.TextAlign.LEFT,
            width=300,
            border_color="#510A32",
            border_radius=10,
            cursor_color="#EE4540"
            )
        self.submit_button = ft.ElevatedButton(text='Abschicken',
            style=ft.ButtonStyle(
                color="#EE4540",
                bgcolor="#510A32",
                text_style=ft.TextStyle(
                    font_family= "Times New Roman",
                    color="#EE4540"
                ),
                overlay_color="#801336",
            ),
            width=200,
            disabled=True
        )

        self.place_of_death.on_change = self.validate
        self.submit_button.on_click = self.submit

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
                ft.Container(height=250),
                ft.Container(
                    content=ft.Text(value="Wo bist du gestorben?", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        #margin=ft.margin.only(left=50, right=50),
                        padding=10,
                ),
                ft.Container(
                    content=self.place_of_death
                ),
                ft.Container(
                    content=self.submit_button
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
                            ft.Container(
                                content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/role")),
                            ),
 
                            ft.Container(
                                content=ft.Text(value="Todesort", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
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
                            )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_AROUND,
                ),
            ]
        )
        
        ])
        return page
    
    def validate(self, e: ft.ControlEvent) -> None:
        if self.place_of_death.value:
            self.submit_button.disabled = False
        else:
            self.submit_button.disabled = True

        self.update()

    def submit(self, e: ft.ControlEvent) -> None:
        print("Place of death:", self.place_of_death.value)
        self.page.go("/role")