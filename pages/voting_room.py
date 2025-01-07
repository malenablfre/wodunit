import flet as ft

class voting_room(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        self.suspects = []

        self.name_column = ft.Column(controls=[self.create_name_item(name) for name in self.names])

        self.suspect_column = ft.Column(controls=[self.create_suspect_item(name) for name in self.suspects])

        self.all_players = "15"
        self.active_players = len(self.names)
        
    def build(self):
        page = ft.Stack([
        # ------ BACKGROUND ------
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
        
        # ------ CONTENT ------
        ft.Column(
            controls=[
                ft.Container(height=50),
                ft.Container(
                    ft.Column(
                        spacing=0,
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            ft.Container(),
                            ft.Container(
                                content=ft.Text(
                                    value=f"({self.active_players}/{self.all_players} aktiv)",
                                    size=15,
                                    font_family="Times New Roman",
                                    color="#EE4540"
                                ),
                                margin=ft.margin.only(left=260, top=25),
                                width=200,

                            ),
                            ft.Container(
                                content=ft.Text(
                                    value="Alle Teilnehmer",
                                    size= 25,
                                    font_family= "Times New Roman",
                                    weight= "bold",
                                    color="#EE4540"
                                ),
                                margin=ft.margin.only(left=50, right=50),
                                padding=10,
                            ),
                            ft.Container(
                                content=self.name_column,
                                bgcolor=ft.colors.TRANSPARENT,
                                border=ft.border.all(width=1, color="#C72C42"),
                                border_radius=10,
                                padding=ft.padding.only(left=20, top=10, bottom=10),
                                width=300
                            ),
                            ft.Container(
                                content=ft.Text(
                                    value="(Tippe auf die Verdächtigen)",
                                    size=10,
                                    font_family= "Times New Roman",
                                    color= "#EE4540"
                                ),
                                margin=ft.margin.only(top=10, bottom=20)
                            ),
                            ft.ElevatedButton(
                                text="Jetzt voten!",
                                style=ft.ButtonStyle(
                                    color="#EE4540",
                                    bgcolor="#510A32",
                                    text_style=ft.TextStyle(
                                        font_family= "Times New Roman",
                                        color="#EE4540",
                                        size=20
                                    ),
                                    overlay_color="#801336",
                                ),
                                width=200,
                                on_click=self.show_dialog
                            )                    
                        ],
                        #alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment= ft.CrossAxisAlignment.CENTER
                    ),
                    height=600,
                    #alignment=ft.alignment.center,
                ),
            ]
        ),
        

        # ------ HEADER ------
        ft.Column(
            controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                            ft.Container(
                                content=ft.IconButton(
                                    ft.Icons.ARROW_BACK,
                                    icon_color="#EE4540",
                                    on_click=lambda _: self.page.go("/")
                                ),
                            ),
 
                            ft.Container(
                                content=ft.Text(
                                    value="Voting",
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
    
    def create_name_item(self, name):
        text = ft.Text(name, weight=ft.FontWeight.NORMAL, font_family= "Times New Roman", color= "#C72C42", size=20)
        container = ft.Container(content=text, on_click=lambda e: self.toggle_bold(e, text))
        return container

    def toggle_bold(self, e, text):
        if text.weight == ft.FontWeight.NORMAL:
            text.weight = ft.FontWeight.BOLD
            self.suspects.append(text.value)
            print(self.suspects)
        else:
            text.weight = ft.FontWeight.NORMAL
            self.suspects.remove(text.value)
            print(self.suspects)
        text.update()



    def create_suspect_item(self, name):
        text = ft.Text(name, weight=ft.FontWeight.NORMAL, font_family= "Times New Roman", color= "#C72C42", size=15)
        container = ft.Container(content=text, on_click=lambda e: self.toggle_vote(e, text))
        return container
    
    def toggle_vote(self, e, text):
        if text.weight == ft.FontWeight.NORMAL:
            text.weight = ft.FontWeight.BOLD
            # self.suspects.append(text.value)
            # print(self.suspects)
        else:
            text.weight = ft.FontWeight.NORMAL
            # self.suspects.remove(text.value)
            # print(self.suspects)
        text.update()


    def show_dialog(self, e):
        dialog = ft.AlertDialog(
            title=ft.Text("Wer ist der Mörder?", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
            content=ft.Container(
                self.suspect_column
            ),
            bgcolor="#801336",
            actions=[
                ft.TextButton(
                    text="Vote",
                    on_click=self.close_dialog,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            font_family="Times New Roman",
                            color="#EE4540", size=20
                        ),
                        overlay_color="#EE4540"
                    )
                ),
            ],
            actions_alignment="end"
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()


    def close_dialog(self, e):
        self.page.dialog.open = False
        self.page.go("/vote_result")
        self.page.update()
