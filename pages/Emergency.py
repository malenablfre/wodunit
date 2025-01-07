import flet as ft

class Emergency(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

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
                ft.Container(height=100),
            ft.Container(    
                ft.Column(
                    spacing=0,
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                    ft.Container(),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                ),
            height=600,
            alignment=ft.alignment.center, 
            ),
                ]
             
            ), 
    
            ft.Column(
                controls=[
                    ft.Container(),
                    ft.Row(
                        controls=[  
                            ft.Container(
                                    content=ft.IconButton( ft.Icons.ARROW_BACK , icon_color="#EE4540", hover_color= '#3f1c3d',splash_color= '#3f1c3d', highlight_color= '#3f1c3d',  on_click=lambda _: self.page.go("/")),
                                ),
    
                                ft.Container(
                                    content=ft.Text(
                                        value="Emergency", 
                                        size= 30, 
                                        font_family= "Times New Roman", 
                                        weight= "bold", color="#EE4540"),
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
                                            ft.PopupMenuItem(text="Home", on_click=lambda _: self.page.go("/")),
                                            ft.PopupMenuItem(text="Rollenübersicht", on_click=lambda _: self.page.go("/")),
                                            ft.PopupMenuItem(text="Spielregeln", on_click=lambda _: self.page.go("/"))
                                        ]
                                    ),
                                    alignment=ft.alignment.top_right
                                )
                            ],
                            alignment = ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ]
                ),
                # ---- Schrift -----
            ft.Column(   
                controls=[ 
                ft.Container(
                        content=ft.Text(value="Emergency Meeting ausrufen ?!", size= 25, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        margin=ft.margin.only(left=50, top= 100, right=25),
                        alignment=ft.alignment.center,
                    )
                ]
            ),
                # ------ Emergency Button -------
            ft.Column(
                controls=[
                    ft.Container(
                        content= ft.IconButton(
                            ft.Icons.CIRCLE_ROUNDED, 
                            icon_size= 200, 
                            icon_color='#ff0000',
                            hover_color= '#ff0000', 
                            on_click= self.show_dialog
                            ),

                        alignment= ft.alignment.center,
                        margin= ft.margin.only(left=10,top= 250, right=10,bottom= 100 )
                    )
                ]
            ),
            
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(value="Es sind noch __ Emergency Meetings verfügbar.", size= 25, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(left= 50, top= 500, right=50)
                    )
                ]
            )

        ])   

        return page

 
    def show_dialog(self, e):
        dialog = ft.AlertDialog(
            title=ft.Text("Möchtest du wirlich eine Emergency Meeting ausrufen?!", style=ft.TextStyle(font_family="Times New Roman", color="#EE4540",)),
            bgcolor="#801336",
            actions=[
                ft.TextButton(text="Ja", on_click=self.yes_close_dialog, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=20), overlay_color="#EE4540")),
                ft.TextButton(text="Nein", on_click=self.no_close_dialog, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Times New Roman", color="#EE4540", size=20), overlay_color="#EE4540"))
            ],
            actions_alignment="end"
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
 
    def yes_close_dialog(self, e):
        self.page.dialog.open = False
        self.page.go("/Emergency2")
        self.page.update()
 
    def no_close_dialog(self, e):
        self.page.dialog.open = False
        self.page.go("/Emergency")
        self.page.update() 
