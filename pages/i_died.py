import flet as ft

class dead(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.expand = True

        self.place_option = ft.TextField(
            hint_text="Neuer Ort",
            hint_style= ft.TextStyle(font_family="Times New Roman", color="#EE4540"),
            text_style=ft.TextStyle(font_family= "Times New Roman", color="#EE4540"),
            bgcolor="#510A32",
            border_color="#510A32",
            cursor_color='#C72C42',
            width=190,
            height=50,
            border_radius=10,
            selection_color='#510A32',
            autofocus=True
        )
       
        self.place_of_death_dropdown = ft.Dropdown(
            label="Todesort",
            hint_text="Ort Auswählen",
            label_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540"),
            text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540"),
            bgcolor="#510A32",
            border_color="#EE4540",
            width=300,
            height=50,
            border_radius=10,
            on_change= self.enable_submit_button,
        )
 
        self.add_new_place = ft.ElevatedButton(
            text= "Hinzufügen",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color="#C72C42",
                bgcolor="#510A32",
                text_style=ft.TextStyle(size= 15, font_family= "Times New Roman", weight= "bold"),
                overlay_color="#2D142C"
            ),
            on_click= self.add_clicked,
            width=100,
            height=50,
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

        self.submit_button.on_click = self.submit


    def add_clicked(self, e):
        self.place_of_death_dropdown.options.append(ft.dropdown.Option(self.place_option.value))
        self.place_of_death_dropdown.value = self.place_option.value
        self.place_option.value = ""
        self.update()

    def enable_submit_button(self, e):
         self.submit_button.disabled = False
         self.update()

    def submit(self, e: ft.ControlEvent) -> None:
        print("Place of death:", self.place_of_death_dropdown.value)
        self.page.go("/role")


    def build(self):
        page = ft.Stack([
            # ------ BACKGROUND ------
            ft.Container(   
                width=self.page.width,
                height=self.page.height,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#2D142C","#510A32"]),
                border_radius=10,
                alignment=ft.alignment.center
                ),
            
            # ------ CONTENT ------
            ft.Column(
                controls=[
                    ft.Container(),
                    ft.Container(
                        content=ft.Text(value="Wo bist du gestorben?", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                    ),
                    ft.Container(
                        content=self.place_of_death_dropdown,
                        margin=ft.margin.only(top= 30)
                    ),

                    ft.Row(
                        controls=[
                            self.place_option,
                            self.add_new_place
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    
                    ft.Container(
                        content=self.submit_button,
                        margin=ft.margin.only(top= 10)
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),

            # ------ HEADER ------
            ft.Container(
                content=ft.Row(
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
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                margin=10
            )
        ])
        return page