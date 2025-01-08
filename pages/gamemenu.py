import flet as ft

#name ändern zu "home"
class gamemenu(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    # ------ SAFETY CHECK -------
    def show_dialog(self, e):
        dialog = ft.AlertDialog(
            title=ft.Text("Achtung!", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
            content=ft.Text("Bist du sicher, dass niemand deinen Bildschirm sehen kann?", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
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

    def build(self):
        days = 10
        alive = 75 #percent
        dead = 25 #percent

        head_container = ft.Column(
            controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                            ft.Container(
                                content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),
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
                                        ft.PopupMenuItem(text="Home", on_click=lambda _: self.page.go("/")), #neuer name: "startseite"
                                        #weiteres element einfügen für "home", war vorher "gamemenu"
                                        ft.PopupMenuItem(text="Rollenübersicht", on_click=self.show_dialog), #hier muss eigtl /rollenuebersicht hin & nicht der alert dialog, noch ändern!
                                        ft.PopupMenuItem(text="Spielregeln", on_click=lambda _: self.page.go("/spielregeln"))
                                    ]
                                ),
                                alignment=ft.alignment.top_right
                            )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_AROUND,
                ),
                ft.Container(
                    content=ft.Text(value=f"Runde läuft seit {days} Tagen", size= 15, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                    margin=0,
                    alignment=ft.alignment.center,
                ),
            ]
        )

        body_container = ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                        content=ft.PieChart(
                            sections=[
                                ft.PieChartSection(alive, title="Lebende", title_style=ft.TextStyle(size=12), color="#C72C42", radius=80),
                                ft.PieChartSection(dead, title="Tote", title_style=ft.TextStyle(size=12), color="#EE4540", radius=80)
                            ],
                            sections_space=1,
                            center_space_radius=0
                        ),
                        margin=-40,
                        on_click=lambda _: self.page.go("/")
                    ),

                    ft.Container(
                        content=ft.Text(value="Meine Rolle", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        on_click=lambda _: self.page.go("/gameslots")
                    ),

                    ft.Container(
                        content=ft.Text(value="Voting", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        on_click=lambda _: self.page.go("/")
                    ),

                    ft.Container(
                        content=ft.Text(value="Emergency", size= 20, font_family= "Times New Roman", weight= "bold", color="#510A32"),
                        margin=10,
                        alignment=ft.alignment.center,
                        bgcolor="#C72C42",
                        width=250,
                        height=50,
                        border_radius=10,
                        on_click=lambda _: self.page.go("/emergencycalled")
                    )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page_container = ft.Container(
            ft.Column(
                spacing=50,
                controls=[
                    head_container,
                    body_container
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C","#510A32"]),
            border_radius=10,
            alignment=ft.alignment.center
            )

        page = ft.Stack(
            controls=[
                page_container
            ]
        )

        return page