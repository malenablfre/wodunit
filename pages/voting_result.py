import flet as ft
from pages.voting_room import voting_room

class voting_result(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        vote_name = voting_room(page)
        self.name = vote_name.main_suspect # funktioniert noch nicht richtig (übernimmt nur leeren str aus init)
        
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
        # ft.Column(
        #     controls=[
                ft.Container(
                    ft.Column(
                        spacing=0,
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    value="Ihr habt rausgevotet:",
                                    size= 25,
                                    font_family= "Times New Roman",
                                    color="#EE4540"
                                ),
                                margin=ft.margin.only(left=50, right=50, bottom=10),
                            ), 
                            ft.Container(
                                content=ft.Text(
                                    value=self.name,
                                    size= 30,
                                    font_family= "Times New Roman",
                                    weight= "bold",
                                    color="#EE4540"
                                ),
                                margin=ft.margin.only(left=50, right=50, bottom=5),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    value='"Rolle"',
                                    size= 20,
                                    font_family= "Times New Roman",
                                    color="#EE4540"
                                ),
                                margin=ft.margin.only(left=50, right=50),
                            ),              
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment= ft.CrossAxisAlignment.CENTER
                    ),
                    height=600,
                    alignment=ft.alignment.center,
                ),
        #     ]
        # ),
        

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
        ),

        ft.Container(
            ft.ElevatedButton(
                text="Zurück zum Home",
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
                on_click=lambda e: self.page.go("/")
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=550)
        )
        
        ])
        return page