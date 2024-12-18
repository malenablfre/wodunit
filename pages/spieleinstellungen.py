import flet as ft

class spieleinstellungen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        other_containers = ft.Column(
            spacing=10,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(),
                        ft.Row(
                            controls=[
                                ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/neuesspiel")),),
                                ft.Container(content=ft.Text(value="Einstellungen", size=35, font_family="Times New Roman", weight="bold", color="#EE4540"),),
                                ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/neuesspiel")),),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        )
                    ]
                ),

                ft.Container(
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Dropdown(
                                label="Anzahl der Spieler",
                                hint_text="Anzahl auswählen",
                                options=[ft.dropdown.Option(str(i)) for i in range(1, 21)],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="Anzahl der Emergency Meetings",
                                hint_text="Anzahl auswählen",
                                options=[ft.dropdown.Option(str(i)) for i in range(1, 6)],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="Mörder töten Mörder",
                                hint_text="Auswählen",
                                options=[ft.dropdown.Option("Ja"), ft.dropdown.Option("Nein")],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="Veröffentlichung Todesliste",
                                hint_text="Uhrzeit auswählen",
                                options=[ft.dropdown.Option(f"{i}:00") for i in range(12, 21)],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="öffentliche Votes",
                                hint_text="Auswählen",
                                options=[ft.dropdown.Option("Ja"), ft.dropdown.Option("Nein")],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="Anzahl Mörder",
                                hint_text="Anzahl auswählen",
                                options=[ft.dropdown.Option("1"), ft.dropdown.Option("2")],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="test",
                                hint_text="Anzahl auswählen",
                                options=[ft.dropdown.Option("1"), ft.dropdown.Option("2")],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="test",
                                hint_text="Anzahl auswählen",
                                options=[ft.dropdown.Option("1"), ft.dropdown.Option("2")],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="test",
                                hint_text="Anzahl auswählen",
                                options=[ft.dropdown.Option("1"), ft.dropdown.Option("2")],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),

                            ft.Dropdown(
                                label="test",
                                hint_text="Anzahl auswählen",
                                options=[ft.dropdown.Option("1"), ft.dropdown.Option("2")],
                                autofocus=True,
                                alignment=ft.alignment.center,
                                color="#EE4540",
                                bgcolor="#510A32",
                                border_color="#EE4540",
                                width=250,
                                height=50,
                                border_radius=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.ALWAYS
                    ),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=250,
                height=400,
                border_radius=10,
                ),

                ft.Container(
                    content=ft.Text(value="Spiel erstellen", size=20, font_family="Times New Roman", weight="bold", color="#510A32"),
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
        )

        background_container = ft.Container(
            content=other_containers,
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C", "#510A32"]
            ),
            border_radius=10,
            alignment=ft.alignment.center
        )

        page = ft.Stack(
            controls=[
                background_container,
            ]
        )

        return page
