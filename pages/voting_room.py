import flet as ft
from pages.extras import extras

class voting_room(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.names = ["Malena", "Anna-Lena", "Jasmin", "Anna-Lotta"]
        self.suspects = []
        self.main_suspect = ""

        self.name_column = ft.Column(controls=[self.create_name_item(name) for name in self.names])

        self.all_players = "15"
        self.active_players = len(self.names)

        self.button_start_voting = ft.ElevatedButton(
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
            disabled=True
        )

        self.button_start_voting.on_click = self.show_dialog



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
        ft.Container(
            ft.Column(
                spacing=0,
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
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
                    self.button_start_voting                    
                ],
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
            ),
            height=600,
            margin=ft.margin.only(top=50)
        ),
        

        # ------ HEADER ------
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
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            margin=10
        )
        
        ])
        return page
    

    # ------ choosing suspects ------
    def create_name_item(self, name):
        text = ft.Text(name, weight=ft.FontWeight.NORMAL, font_family= "Times New Roman", color= "#C72C42", size=20)
        container = ft.Container(content=text, on_click=lambda e: self.toggle_bold(e, text))
        return container

    def toggle_bold(self, e, text):
        if text.weight == ft.FontWeight.NORMAL:
            text.weight = ft.FontWeight.BOLD
            self.suspects.append(text.value)
        else:
            text.weight = ft.FontWeight.NORMAL
            self.suspects.remove(text.value)
        
        if len(self.suspects) > 0:
            self.button_start_voting.disabled = False
        else: 
            self.button_start_voting.disabled = True
        text.update()
        self.update()


    # ------ choosing your vote ------
    def create_suspect_item(self, name):
        text = ft.Text(name, weight=ft.FontWeight.NORMAL, font_family= "Times New Roman", color= "#C72C42", size=20)
        container = ft.Container(content=text, on_click=lambda e: self.toggle_vote(e, text))
        return container
    
    def toggle_vote(self, e, text):
        if text.weight == ft.FontWeight.NORMAL:
            for control in self.suspect_column.controls:
                control.content.weight = ft.FontWeight.NORMAL
                control.content.update()
            text.weight = ft.FontWeight.BOLD
            self.main_suspect = text.value
        else:
            text.weight = ft.FontWeight.NORMAL
            self.main_suspect = ""
        text.update()
        self.update()


    # ------ VOTING DIALOGUE ------
    def show_dialog(self, e):
        self.suspect_column = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            height= 100,
            controls=[self.create_suspect_item(name) for name in self.suspects]
        )
        dialog = ft.AlertDialog(
            title=ft.Text("Wer ist der Mörder?", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
            content=ft.Container(
                self.suspect_column
            ),
            bgcolor="#801336",
            actions=[
                ft.TextButton(
                    text="Stimme abgeben",
                    on_click=self.close_dialog,
                    #disabled= True,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            font_family="Times New Roman",
                            color="#EE4540", size=20
                        ),
                        overlay_color= ft.Colors.with_opacity(0.1, "#EE4540")
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
        print(self.main_suspect)
        self.page.go("/vote_result")
        self.page.update()
