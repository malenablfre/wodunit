import flet as ft

class voting_result(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        self.suspects = []

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
                                    on_click=lambda _: self.page.go("/vote")
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