import flet as ft

class role(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.expand = True
        self.role = "Unschuldig"
        self.description = "Du bist ein normaler Teilnehmer ohne besondere Fähigkeiten. Dein Ziel ist es, die Mörder zu entlarven und zu eliminieren."


    def show_dialog(self, e):
        dialog = ft.AlertDialog(
            title=ft.Text("Bist du gestorben?", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
            bgcolor="#801336",
            actions=[
                ft.TextButton(
                    text="Ja",
                    on_click=self.yes_close_dialog,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            font_family="Times New Roman",
                            color="#EE4540",
                            size=20
                        ),
                        overlay_color="#EE4540"
                    )
                ),
                ft.TextButton(
                    "Nein",
                    on_click=self.no_close_dialog,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            font_family="Times New Roman",
                            color="#EE4540",
                            size=20
                        ),
                        overlay_color="#EE4540"
                    )
                )
            ],
            actions_alignment="end"
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def yes_close_dialog(self, e):
        self.page.dialog.open = False
        self.page.go("/dead")
        self.page.update()

    def no_close_dialog(self, e):
        self.page.dialog.open = False
        self.page.update()


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
            ft.Container(
                ft.Column(
                    spacing=0,
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Container(),
                        ft.Container(
                            content=ft.Text(value=self.role, size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                            padding=10
                        ),

                        ft.Container(
                            content=ft.Text(value=self.description, size= 15, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.TRANSPARENT,
                            border=ft.border.all(width=1, color="#C72C42"),
                            width=300,
                            height=150,
                            border_radius=10
                        ),

                        ft.Container(
                            content=ft.Text(value="Notizen", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                            margin=ft.margin.only(top=25),
                            padding=10
                        ),

                        ft.Container(
                            content=ft.TextField(
                                multiline=True,
                                autofocus= True,
                                border="none",
                                cursor_color="#C72C42",
                                hint_text="...",
                                hint_style=ft.TextStyle(
                                    font_family= "Times New Roman",
                                    color="#C72C42"
                                ),
                                text_style=ft.TextStyle(
                                    font_family= "Times New Roman",
                                    color="#C72C42"
                                )
                            ),
                            padding=ft.padding.only(left=10, right=10),
                            bgcolor=ft.colors.TRANSPARENT,
                            border=ft.border.all(width=1, color="#C72C42"),
                            width=300,
                            height=150,
                            border_radius=10
                        )                  
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                ),
                height=600,
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=20)     
            ),
            

            ft.Container(
                content=ft.FloatingActionButton(icon=ft.Icons.DANGEROUS_OUTLINED, bgcolor="#EE4540", on_click=self.show_dialog),
                alignment=ft.alignment.bottom_right,
                margin=ft.margin.only(right=20, bottom=20, top=550),
                height= 70
            ),

            # ------ HEADER ------
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.IconButton(
                                ft.Icons.ARROW_BACK,
                                icon_color="#EE4540",
                                hover_color= ft.Colors.with_opacity(0.1, "#C72C42"),
                                highlight_color= ft.Colors.with_opacity(0.5, "#C72C42"),
                                on_click=lambda _: self.page.go("/")
                            )
                        ),

                        ft.Container(
                            content=ft.Text(
                                value="Meine Rolle",
                                size= 30,
                                font_family= "Times New Roman",
                                weight= "bold",
                                color="#EE4540")
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
                            )
                        )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                margin=10
            )
        ])
        return page